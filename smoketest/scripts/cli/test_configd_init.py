#!/usr/bin/env python3
#
# Copyright (C) 2021 VyOS maintainers and contributors
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

import unittest
from time import sleep

from ngnos.util import cmd, is_systemd_service_running

class TestConfigdInit(unittest.TestCase):
    def setUp(self):
        self.running_state = is_systemd_service_running('ngnos-configd.service')

    def test_configd_init(self):
        if not self.running_state:
            cmd('sudo systemctl start ngnos-configd.service')
            # allow time for init to succeed/fail
            sleep(2)
            self.assertTrue(is_systemd_service_running('ngnos-configd.service'))

    def tearDown(self):
        if not self.running_state:
            cmd('sudo systemctl stop ngnos-configd.service')

if __name__ == '__main__':
    unittest.main(verbosity=2)
