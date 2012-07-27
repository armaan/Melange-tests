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

class GSoCAboutPageTest(FunctionalTestCase):
  """ This test case test the functionality of GSoC Connect with us Page.
  """  
  def setUp(self):
    self.init()
    self.setup()

  def testConnectWithUsPage(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSoC_connect_with_us")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Click on Connect With Us Link.
    self.clickOn("xpath", "connect_with_us")

    #Check timeline link.
    self.wait(3)
    self.clickOn("xpath", "Timeline_link")
    self.wait(3)
    self.Browser.back()

    #Check FAQ link.
    self.wait(3)
    self.clickOn("xpath", "FAQ_link")
    self.wait(3)
    self.Browser.back()

    #Check Google open source blog link.
    self.wait(3)
    self.clickOn("xpath", "Google_open_source_blog_link")
    self.wait(3)
    self.Browser.back()

  def tearDown(self):
    self.teardown()

