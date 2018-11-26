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

__all__ = [
    'ACTION_NAME',
    'ACTION_ID',

    'LIBS_DIR',

    'LIVEACTION_STATUS_REQUESTED',
    'LIVEACTION_STATUS_SCHEDULED',
    'LIVEACTION_STATUS_DELAYED',
    'LIVEACTION_STATUS_POLICY_DELAYED',
    'LIVEACTION_STATUS_RUNNING',
    'LIVEACTION_STATUS_SUCCEEDED',
    'LIVEACTION_STATUS_FAILED',
    'LIVEACTION_STATUS_TIMED_OUT',
    'LIVEACTION_STATUS_CANCELING',
    'LIVEACTION_STATUS_CANCELED',
    'LIVEACTION_STATUS_PENDING',
    'LIVEACTION_STATUS_PAUSING',
    'LIVEACTION_STATUS_PAUSED',
    'LIVEACTION_STATUS_RESUMING',

    'LIVEACTION_STATUSES',
    'LIVEACTION_RUNNABLE_STATES',
    'LIVEACTION_CANCELABLE_STATES',
    'LIVEACTION_FAILED_STATES',
    'LIVEACTION_COMPLETED_STATES',

    'ACTION_OUTPUT_RESULT_DELIMITER',
    'ACTION_CONTEXT_KV_PREFIX',
    'ACTION_PARAMETERS_KV_PREFIX',
    'ACTION_RESULTS_KV_PREFIX',

    'WORKFLOW_RUNNER_TYPES'
]


ACTION_NAME = 'name'
ACTION_ID = 'id'
ACTION_PACK = 'pack'

LIBS_DIR = 'lib'

LIVEACTION_STATUS_REQUESTED = 'requested'
LIVEACTION_STATUS_SCHEDULED = 'scheduled'
LIVEACTION_STATUS_DELAYED = 'delayed'
LIVEACTION_STATUS_POLICY_DELAYED = 'policy-delayed'
LIVEACTION_STATUS_RUNNING = 'running'
LIVEACTION_STATUS_SUCCEEDED = 'succeeded'
LIVEACTION_STATUS_FAILED = 'failed'
LIVEACTION_STATUS_TIMED_OUT = 'timeout'
LIVEACTION_STATUS_ABANDONED = 'abandoned'
LIVEACTION_STATUS_CANCELING = 'canceling'
LIVEACTION_STATUS_CANCELED = 'canceled'
LIVEACTION_STATUS_PENDING = 'pending'
LIVEACTION_STATUS_PAUSING = 'pausing'
LIVEACTION_STATUS_PAUSED = 'paused'
LIVEACTION_STATUS_RESUMING = 'resuming'

LIVEACTION_STATUSES = [
    LIVEACTION_STATUS_REQUESTED,
    LIVEACTION_STATUS_SCHEDULED,
    LIVEACTION_STATUS_DELAYED,
    LIVEACTION_STATUS_POLICY_DELAYED,
    LIVEACTION_STATUS_RUNNING,
    LIVEACTION_STATUS_SUCCEEDED,
    LIVEACTION_STATUS_FAILED,
    LIVEACTION_STATUS_TIMED_OUT,
    LIVEACTION_STATUS_ABANDONED,
    LIVEACTION_STATUS_CANCELING,
    LIVEACTION_STATUS_CANCELED,
    LIVEACTION_STATUS_PENDING,
    LIVEACTION_STATUS_PAUSING,
    LIVEACTION_STATUS_PAUSED,
    LIVEACTION_STATUS_RESUMING
]

ACTION_OUTPUT_RESULT_DELIMITER = '%%%%%~=~=~=************=~=~=~%%%%'
ACTION_CONTEXT_KV_PREFIX = 'action_context'
ACTION_PARAMETERS_KV_PREFIX = 'action_parameters'
ACTION_RESULTS_KV_PREFIX = 'action_results'

LIVEACTION_RUNNABLE_STATES = [
    LIVEACTION_STATUS_REQUESTED,
    LIVEACTION_STATUS_SCHEDULED,
    LIVEACTION_STATUS_PAUSING,
    LIVEACTION_STATUS_PAUSED,
    LIVEACTION_STATUS_RESUMING
]

LIVEACTION_CANCELABLE_STATES = [
    LIVEACTION_STATUS_REQUESTED,
    LIVEACTION_STATUS_SCHEDULED,
    LIVEACTION_STATUS_DELAYED,
    LIVEACTION_STATUS_POLICY_DELAYED,
    LIVEACTION_STATUS_RUNNING,
    LIVEACTION_STATUS_PAUSING,
    LIVEACTION_STATUS_PAUSED,
    LIVEACTION_STATUS_RESUMING
]

LIVEACTION_COMPLETED_STATES = [
    LIVEACTION_STATUS_SUCCEEDED,
    LIVEACTION_STATUS_FAILED,
    LIVEACTION_STATUS_TIMED_OUT,
    LIVEACTION_STATUS_CANCELED,
    LIVEACTION_STATUS_ABANDONED
]

LIVEACTION_FAILED_STATES = [
    LIVEACTION_STATUS_FAILED,
    LIVEACTION_STATUS_TIMED_OUT,
    LIVEACTION_STATUS_ABANDONED
]

LIVEACTION_PAUSE_STATES = [
    LIVEACTION_STATUS_PAUSING,
    LIVEACTION_STATUS_PAUSED
]

LIVEACTION_CANCEL_STATES = [
    LIVEACTION_STATUS_CANCELING,
    LIVEACTION_STATUS_CANCELED
]

WORKFLOW_RUNNER_TYPES = [
    'action-chain',
    'mistral-v2',
    'orquesta'
]

# Linux's limit for param size
_LINUX_PARAM_LIMIT = 131072
# Overhead for `--parameters=` + 2 to grow on.
_ST2_PARAM_BUFFER = 15
MAX_PARAM_LENGTH = _LINUX_PARAM_LIMIT - _ST2_PARAM_BUFFER
