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

""" Accepted Organisations: This test case checks the functionality on Accepted
                            Organisations Page.
"""

import unittest

from melange_functional_actions import FunctionalTestCase

class AcceptedOrganisationsTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters('./tests/functional/testdata_melange.xls', 'Accepted_Orgs')    
     
  def testForAcceptedOrgs(self):
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Click on Accepted Orgs
    self.clickOn("xpath", "Accepted_Orgs")

    #Search For a Organisation.
    self.wait(10)
    self.writeTextField("xpath", "Search_organisation")
    self.wait(10)

    #Check csv export.
    self.clickOn("xpath", "Csv_export")
    self.wait(3)
    self.clickOn("xpath", "Csv_textarea")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.clickOn("xpath", "Csv_close")
    self.clearField("xpath", "Search_organisation")

    #Check Filters.
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.clickOn("xpath", "Filter")
    self.wait(3)
    self.setDropDownList("Filter_and_or")
    self.clickOn("xpath", "Filter_plus")
    self.setDropDownList("Filter_type1")
    self.writeTextField("xpath", "Enter_filter1_value")
    self.setDropDownList("Filter_type2")
    self.writeTextField("xpath", "Enter_filter2_value")
    self.clickOn("xpath", "Find")

    #Reload Grid.
    self.clickOn("xpath", "Reload_grid")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Check column functionality.
    self.clickOn("xpath", "Column")
    self.wait(3)
    self.clickOn("xpath", "Remove_all")
    self.wait(3)
    self.clickOn("xpath", "Name")
    self.clickOn("xpath", "Tag")
    self.clickOn("xpath", "Ideas")
    self.wait(3)
    self.clickOn("xpath", "OK")

    #Search an organisation.
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.wait(3)
    self.clearField("xpath", "Search_organisation")
    self.writeTextField("xpath", "Search_organisation")
    self.wait(3)
    self.clickOn("xpath", "Select_org")
    self.wait(20)
    self.Browser.get(self.obj_id['Accepted_orgs_url'])
    self.clearField("xpath", "Search_organisation")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  def tearDown(self):
    self.teardown()
