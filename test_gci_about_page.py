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

from melange_functional_actions import FunctionalTestCase

class GCIAboutPageTest(FunctionalTestCase):
  """ This test case checks links and text present on GCI About Page.
  """
  def setUp(self):
    self.init()
    self.setup()

  def testGCIAboutPage(self):
    #Load test data.
    self.getParameters(self.Data_source, "GCI_About_Test")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Code-In", self.Browser.title)

    #Click on About page.
    self.clickOn("xpath", "About")

    #Assert browser title.
    self.wait(5)
    self.assertIn("About Google Code-In", self.Browser.title)

    #Assert message on About GCI page.
    self.assertText("About_GCI")

    #Assert link "contest announcement list".
    self.assertLink("contest announcement list")

    #Assert link "Google Open Source Blog".
    self.assertLink("Google Open Source Blog")

  def tearDown(self):
    self.teardown()

