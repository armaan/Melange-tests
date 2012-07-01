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

class AboutPageTest(unittest.TestCase, FunctionalTestCase):
  
  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters("/home/syed/Desktop/testdata_melange.xls", "GSOC_About_Test")

  def test_About_Page(self):
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Click on About Page.
    self.clickOn("xpath", "About")

    #Check for the browser title.
    self.wait(5)
    self.assertIn("About Google Summer of Code", self.Browser.title)

    #Assert message about GSoC.
    self.assertText("About_GSoC")

    #Assert "Timeline" link.
    self.assertLink("Timeline")

    #Assert "Frequently Asked Questions" link.
    self.assertLink("Frequently Asked Questions")

    #Assert "Internet Relay Chat (IRC)" link.
    self.assertLink("Internet Relay Chat (IRC)")

    #Assert "mailing lists" link.
    self.assertLink("mailing lists")

    #Assert "social networking sites" link.
    self.assertLink("social networking sites")

    #Assert "Google Open Source Blog" link.    
    self.assertLink("Google Open Source Blog")

  def tearDown(self):
    self.teardown()
