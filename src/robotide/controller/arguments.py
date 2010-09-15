#  Copyright 2008-2010 Nokia Siemens Networks Oyj
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import re


def parse_arguments_to_var_dict(args):
    result = {}
    for arg in args:
        parsed = parse_argument(arg)
        if parsed:
            result[parsed[0]] = parsed[1]
    return result

default_val_regexp = re.compile(r'([$@]\{.*\})\s*=\s*(.*)')

looks_like_var_regexp = re.compile(r'([$@]\{.*\})')

def parse_argument(argument):
    match = default_val_regexp.match(argument)
    if match:
        return (match.group(1), match.group(2))
    if looks_like_var_regexp.match(argument):
        return (argument, None)
    return None