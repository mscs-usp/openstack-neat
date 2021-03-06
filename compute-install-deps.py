#!/usr/bin/python2

# Copyright 2012 Anton Beloglazov
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from neat.config import *
import neat.common as common

config = read_and_validate_config([DEFAILT_CONFIG_PATH, CONFIG_PATH],
                                  REQUIRED_FIELDS)
compute_hosts = common.parse_compute_hosts(config['compute_hosts'])

common.execute_on_hosts(
    compute_hosts,
    ['./openstack-neat/setup/deps-fedora-devstack.sh'])
