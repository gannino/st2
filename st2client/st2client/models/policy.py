# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import

import logging

from st2client.models import core


LOG = logging.getLogger(__name__)


class PolicyType(core.Resource):
    _alias = 'Policy-Type'
    _display_name = 'Policy type'
    _plural = 'PolicyTypes'
    _plural_display_name = 'Policy types'
    _repr_attributes = ['ref', 'enabled', 'description']


class Policy(core.Resource):
    _plural = 'Policies'
    _repr_attributes = ['name', 'pack', 'enabled', 'policy_type', 'resource_ref']
