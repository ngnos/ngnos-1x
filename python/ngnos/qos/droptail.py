# Copyright 2022 VyOS maintainers and contributors <maintainers@vyos.io>
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

from ngnos.qos.base import QoSBase

class DropTail(QoSBase):
    # https://man7.org/linux/man-pages/man8/tc-pfifo.8.html
    def update(self, config, direction):
        tmp = f'tc qdisc add dev {self._interface} root pfifo'
        if 'queue_limit' in config:
            limit = config["queue_limit"]
            tmp += f' limit {limit}'
        self._cmd(tmp)

        # call base class
        super().update(config, direction)
