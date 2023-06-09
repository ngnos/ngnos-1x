#!/usr/bin/env python3
#
# Copyright (C) 2019-2022 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from sys import exit
from netifaces import interfaces

from ngnos.config import Config
from ngnos.configdict import get_interface_dict
from ngnos.configdict import is_node_changed
from ngnos.configverify import verify_address
from ngnos.configverify import verify_mtu_ipv6
from ngnos.configverify import verify_bridge_delete
from ngnos.configverify import verify_mirror_redirect
from ngnos.configverify import verify_bond_bridge_member
from ngnos.ifconfig import GeneveIf
from ngnos import ConfigError

from ngnos import airbag
airbag.enable()

def get_config(config=None):
    """
    Retrive CLI config as dictionary. Dictionary can never be empty, as at least the
    interface name will be added or a deleted flag
    """
    if config:
        conf = config
    else:
        conf = Config()
    base = ['interfaces', 'geneve']
    ifname, geneve = get_interface_dict(conf, base)

    # GENEVE interfaces are picky and require recreation if certain parameters
    # change. But a GENEVE interface should - of course - not be re-created if
    # it's description or IP address is adjusted. Feels somehow logic doesn't it?
    for cli_option in ['remote', 'vni', 'parameters']:
        if is_node_changed(conf, base + [ifname, cli_option]):
            geneve.update({'rebuild_required': {}})

    return geneve

def verify(geneve):
    if 'deleted' in geneve:
        verify_bridge_delete(geneve)
        return None

    verify_mtu_ipv6(geneve)
    verify_address(geneve)
    verify_bond_bridge_member(geneve)
    verify_mirror_redirect(geneve)

    if 'remote' not in geneve:
        raise ConfigError('Remote side must be configured')

    if 'vni' not in geneve:
        raise ConfigError('VNI must be configured')

    return None


def generate(geneve):
    return None

def apply(geneve):
    # Check if GENEVE interface already exists
    if 'rebuild_required' in geneve or 'delete' in geneve:
        if geneve['ifname'] in interfaces():
            g = GeneveIf(geneve['ifname'])
            # GENEVE is super picky and the tunnel always needs to be recreated,
            # thus we can simply always delete it first.
            g.remove()

    if 'deleted' not in geneve:
        # Finally create the new interface
        g = GeneveIf(**geneve)
        g.update(geneve)

    return None


if __name__ == '__main__':
    try:
        c = get_config()
        verify(c)
        generate(c)
        apply(c)
    except ConfigError as e:
        print(e)
        exit(1)
