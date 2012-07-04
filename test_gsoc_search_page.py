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

class SearchPageTest(FunctionalTestCase):
  """ This test case test the functionality of GSoC Search Page.
  """ 
  def setUp(self):
    self.init()
    self.setup()
    self.getParameters(self.Data_source, "GSOC_Search_Test")

  def test_Search_Page(self): 
    #Go to the url where melange is hosted.
    self.Browser.get(self.obj_id['Url'])

    #Click on Search in the menu.
    self.clickOn("xpath", "Search")
    self.wait(10)

    #Enter the search item.
    self.writeTextField("xpath", "Search_item")
    self.wait(5)

    #Click on Search
    self.clickOn("xpath", "Search_button")
    self.scrollDown()
    self.wait(5)

    #Enter new search item.
    self.clearField("xpath", "Search_item")
    self.writeTextField("xpath", "New_search_item")

    #Click to Search.
    self.clickOn("xpath", "Search_button")
    self.wait(5)    
    self.scrollDown()

  def tearDown(self):
    self.teardown()
