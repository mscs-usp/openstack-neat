#!/bin/sh

# Contribution by Albert De La Fuente
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

sudo yum install -y scipy nfs-common nfs-utils
#sudo pip install --upgrade SQLAlchemy 
sudo pip install --upgrade pyqcy PyContracts bottle requests Sphinx python-novaclient
sudo pip install mocktest
