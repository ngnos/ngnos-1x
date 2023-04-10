# Copyright 2018-2023 VyOS maintainers and contributors <maintainers@vyos.io>
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

import os

base_dir = '/usr/libexec/ngnos/'

directories = {
  'base' : base_dir,
  'data' : '/usr/share/ngnos/',
  'conf_mode' : f'{base_dir}/conf_mode',
  'op_mode' : f'{base_dir}/op_mode',
  'services' : f'{base_dir}/services',
  'config' : '/opt/vyatta/etc/config',
  'current' : '/opt/vyatta/etc/config-migrate/current',
  'migrate' : '/opt/vyatta/etc/config-migrate/migrate',
  'log' : '/var/log/vyatta',
  'templates' : '/usr/share/ngnos/templates/',
  'certbot' : '/config/auth/letsencrypt',
  'api_schema': f'{base_dir}/services/api/graphql/graphql/schema/',
  'api_client_op': f'{base_dir}/services/api/graphql/graphql/client_op/',
  'api_templates': f'{base_dir}/services/api/graphql/session/templates/',
  'ngnos_udev_dir' : '/run/udev/ngnos'
}

config_status = '/tmp/ngnos-config-status'

cfg_group = 'vyattacfg'

cfg_vintage = 'ngnos'

commit_lock = '/opt/vyatta/config/.lock'

component_version_json = os.path.join(directories['data'], 'component-versions.json')

https_data = {
    'listen_addresses' : { '*': ['_'] }
}

api_data = {
    'listen_address' : '127.0.0.1',
    'port' : '8080',
    'socket' : False,
    'strict' : False,
    'debug' : False,
    'api_keys' : [ {'id' : 'testapp', 'key' : 'qwerty'} ]
}

ngnos_cert_data = {
    'conf' : '/etc/nginx/snippets/ngnos-cert.conf',
    'crt' : '/etc/ssl/certs/ngnos-selfsigned.crt',
    'key' : '/etc/ssl/private/ngnos-selfsign',
    'lifetime' : '365',
}
