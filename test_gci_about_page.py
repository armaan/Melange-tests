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

""" This test case test the functionality of GSoC About Page.
"""

import unittest

from melange_functional_actions import *

class GCIAboutPageTest(unittest.TestCase, FunctionalTestCase):
  
  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters("/home/syed/Desktop/testdata_melange.xls", "GCI_About_Test")

  def test_GCI_About_Page(self):
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Code-In", self.Browser.title)

    #Click on About Page.
    self.clickOn("xpath", "About")

    #Check for the browser title.
    self.wait(5)
    self.assertIn("About Google Code-In", self.Browser.title)

    #Assert message about GCI.
    self.assertText("About_GCI")

    #Assert Links.
    self.assertLink("contest announcement list")
    self.assertLink("Google Open Source Blog")


  def tearDown(self):
    self.teardown()


if __name__ == "__main__":
  unittest.main()    
