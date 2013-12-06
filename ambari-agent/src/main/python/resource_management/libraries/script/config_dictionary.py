#!/usr/bin/env python2.6

'''
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
from resource_management.core.exceptions import Fail

class ConfigDictionary(dict):
  """
  Immutable config dictionary
  """
  
  def __init__(self, dictionary):
    """
    Recursively turn dict to ConfigDictionary
    """
    for k, v in dictionary.iteritems():
      if isinstance(v, dict):
        dictionary[k] = ConfigDictionary(v)
        
    super(ConfigDictionary, self).__init__(dictionary)

  def __setitem__(self, name, value):
    raise Fail("Configuration dictionary is immutable!")

  def __getitem__(self, name):
    """
    Use Python types
    """
    value = super(ConfigDictionary, self).__getitem__(name)
    
    if value == "true":
      value = True
    elif value == "false":
      value = False
    else: 
      try:
        value = int(value)
      except (ValueError, TypeError):
        try:
          value =  float(value)
        except (ValueError, TypeError):
          pass
    
    return value