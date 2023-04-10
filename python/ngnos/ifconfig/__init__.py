# Copyright 2019-2022 VyOS maintainers and contributors <maintainers@vyos.io>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library.  If not, see <http://www.gnu.org/licenses/>.

from ngnos.ifconfig.section import Section
from ngnos.ifconfig.control import Control
from ngnos.ifconfig.interface import Interface
from ngnos.ifconfig.operational import Operational
from ngnos.ifconfig.vrrp import VRRP

from ngnos.ifconfig.bond import BondIf
from ngnos.ifconfig.bridge import BridgeIf
from ngnos.ifconfig.dummy import DummyIf
from ngnos.ifconfig.ethernet import EthernetIf
from ngnos.ifconfig.geneve import GeneveIf
from ngnos.ifconfig.loopback import LoopbackIf
from ngnos.ifconfig.macvlan import MACVLANIf
from ngnos.ifconfig.input import InputIf
from ngnos.ifconfig.vxlan import VXLANIf
from ngnos.ifconfig.wireguard import WireGuardIf
from ngnos.ifconfig.vtun import VTunIf
from ngnos.ifconfig.vti import VTIIf
from ngnos.ifconfig.pppoe import PPPoEIf
from ngnos.ifconfig.tunnel import TunnelIf
from ngnos.ifconfig.wireless import WiFiIf
from ngnos.ifconfig.l2tpv3 import L2TPv3If
from ngnos.ifconfig.macsec import MACsecIf
from ngnos.ifconfig.veth import VethIf
from ngnos.ifconfig.wwan import WWANIf
from ngnos.ifconfig.sstpc import SSTPCIf
