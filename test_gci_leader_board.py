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

class GCILeaderboardTest(FunctionalTestCase):
  """GCI Leaderboard: This test script checks the functionality of Leaderboard.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGCILeaderboard(self):
    #Load test data.
    self.getParameters(self.Data_source, "GCI_Leaderboard_Test")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Code In Contest", self.Browser.title)
    self.wait(3)

    #Scroll down.
    self.scrollDown()

    #Click On leader board.
    self.clickOn("xpath", "Leader_board")
    self.wait(3)

    #Assert leader board text.
    self.assertText("Leader_board_text")
    self.wait(3)

    #Click to refresh.
    self.clickOn("xpath", "Refresh")
    self.wait(3)

    #Click on columns.
    self.clickOn("xpath", "Columns")
    self.wait(3)

    #Select one more column value.
    self.clickOn("xpath", "Add_key")
    self.wait(3)

    #Click OK.
    self.clickOn("xpath", "OK")
    self.wait(3)

    #Click on CSV export.
    self.clickOn("xpath", "CSV_export")
    self.wait(3)

    #Click on close.
    self.clickOn("xpath", "Close")

  def tearDown(self):
    self.teardown()

