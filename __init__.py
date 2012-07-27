#!/usr/bin/env python2.5
#
# Copyright 2012 the Melange authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from selenium import webdriver
os.system("nohup thirdparty/google_appengine/dev_appserver.py\
           --datastore_path=/tmp/my_app_datastore build &")
Browser = webdriver.Firefox()
Browser.get("http://localhost:8080/seed_db")
Browser.close()

