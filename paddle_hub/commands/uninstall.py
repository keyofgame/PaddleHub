# Copyright (c) 2019  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
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

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from paddle_hub.tools.logger import logger
from paddle_hub.commands.base_command import BaseCommand
from paddle_hub.tools import utils
from paddle_hub.module.manager import default_module_manager


class UninstallCommand(BaseCommand):
    name = "uninstall"

    def __init__(self, name):
        super(UninstallCommand, self).__init__(name)
        self.show_in_help = True
        self.description = "Uninstall the specify module from current environment."

    def exec(self, argv):
        module_name = argv[0]
        result, tips = default_module_manager.uninstall_module(
            module_name=module_name)
        print(tips)
        return result


command = UninstallCommand.instance()
