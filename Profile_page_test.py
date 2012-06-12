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

""" This test case test the functionality of Profile Page.
"""

import unittest

from melange_functional_actions import *

class ProfilePageTest(unittest.TestCase, FunctionalTests):

  def setUp(self):
    functest.getParameters("/home/syed/Desktop/testdata_melange.xls", "GSOC_Profile_test")
  
  def test_ProfilePage(self):

    #Test Url, Change it according to your local dev environment.
    functest.Browser.get(functest.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", functest.Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    functest.assertText("How Google Summer of Code Works")
  
    #Click on Login.
    functest.wait(3)
    functest.clickOn("xpath", "Login")
    
     
    #Login to your account on melange.
    functest.login()
    functest.wait(2)

    #Check your profile.
    functest.clickOn("xpath", "Profile")
    functest.wait(2)

    #Clear Public name and enter new public name.
    functest.clearField("id", "Public_name")
    functest.wait(2)
    functest.writeTextField("id", "New_public_name")
   
  def tearDown(self):
    functest.tearDown()

functest = FunctionalTests()
if __name__ == "__main__":
  unittest.main()
  


