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

class GCIEventsAndTimeline(FunctionalTestCase):
  """ This test case checks the functionality 
      of GCI Events and Timeline Page.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGCIEventsAndTimeline(self):
    #Load test data.
    self.getParameters(self.Data_source, "GCI_Timeline")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Click on "Events & Timeline".
    self.clickOn("xpath", "Events_and_Timeline")
    self.wait(3)

    frame=self.Browser.find_element_by_tag_name("iframe")
    self.Browser.switch_to_frame(frame)

    #Check previous events.
    self.wait(5)
    self.clickOn("xpath", "Previous_period")

    #Ckeck whats today.
    self.clickOn("xpath", "Today")

    #Check Next events.
    self.clickOn("xpath", "Next_period")

    #Check weekly events.
    self.clickOn("xpath", "week")

    #Check weekly events.
    self.clickOn("xpath", "week")

    #Check agenda.
    self.clickOn("xpath", "Agenda")
    self.Browser.switch_to_default_content()
    self.scrollDown()

  def tearDown(self):
    self.teardown()
