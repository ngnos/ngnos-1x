#!/usr/bin/env python3
#
# Copyright (C) 2022 VyOS maintainers and contributors
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 or later as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import json

from tabulate import tabulate
from ngnos.configquery import ConfigTreeQuery
from ngnos.util import rc_cmd

import ngnos.opmode


occtl        = '/usr/bin/occtl'
occtl_socket = '/run/ocserv/occtl.socket'


def _get_raw_data_sessions():
    rc, out = rc_cmd(f'sudo {occtl} --json --socket-file {occtl_socket} show users')
    if rc != 0:
        raise ngnos.opmode.DataUnavailable(out)

    sessions = json.loads(out)
    return sessions


def _get_formatted_sessions(data):
    headers = ["Interface", "Username", "IP", "Remote IP", "RX", "TX", "State", "Uptime"]
    ses_list = []
    for ses in data:
        ses_list.append([
            ses["Device"], ses["Username"], ses["IPv4"], ses["Remote IP"], 
            ses["_RX"], ses["_TX"], ses["State"], ses["_Connected at"]
        ])
    if len(ses_list) > 0:
        output = tabulate(ses_list, headers)
    else:
        output = 'No active openconnect sessions'
    return output


def show_sessions(raw: bool):
    config = ConfigTreeQuery()
    if not config.exists('vpn openconnect'):
        raise ngnos.opmode.UnconfiguredSubsystem('Openconnect is not configured')

    openconnect_data = _get_raw_data_sessions()
    if raw:
        return openconnect_data
    return _get_formatted_sessions(openconnect_data)


if __name__ == '__main__':
    try:
        res = ngnos.opmode.run(sys.modules[__name__])
        if res:
            print(res)
    except (ValueError, ngnos.opmode.Error) as e:
        print(e)
        sys.exit(1)
