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

""" This test case test the functionality of Search Page.
"""

import unittest

from melange_functional_actions import *

class SearchPageTest(unittest.TestCase, FunctionalTestCase):
  
  def setUp(self):
    functest.setup()
    functest.getParameters("/home/syed/Desktop/testdata_melange.xls", "GSOC_Search_Test")

  def test_Search_Page(self):
 
    #Go to the url where melange is hosted.
    functest.Browser.get(functest.obj_id['Url'])
    #Click on Search in the menu.
    functest.clickOn("xpath", "Search")
    functest.wait(10)
    #Enter the search item.
    functest.writeTextField("xpath", "Search_item")
    functest.wait(5)
    #Click on Search
    functest.clickOn("xpath", "Search_button")
    functest.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    functest.wait(5)
    #Enter new search item.
    functest.clearField("xpath", "Search_item")
    functest.writeTextField("xpath", "New_search_item")
    functest.clickOn("xpath", "Search_button")
    functest.wait(5)    
    functest.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")




  def tearDown(self):
    functest.teardown()

functest = FunctionalTestCase()
if __name__ == "__main__":
  unittest.main()
     
