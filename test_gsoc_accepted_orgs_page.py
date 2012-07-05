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

class AcceptedOrganisationsTest(FunctionalTestCase):
  """ Accepted Organisations: This test case checks the functionality 
      of GSoC Accepted Organisations Page.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testForAcceptedOrgs(self):
    #Load test data.
    self.getParameters(self.Data_source, "Accepted_Orgs")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Click on Accepted Orgs.
    self.clickOn("xpath", "Accepted_Orgs")

    #Search for a organisation.
    self.wait(10)
    self.writeTextField("xpath", "Search_organisation")
    self.wait(10)

    #Check csv export.
    self.clickOn("xpath", "Csv_export")
    self.wait(3)
    self.clickOn("xpath", "Csv_textarea")
    self.scrollDown()

    #Click to close csv export area.
    self.clickOn("xpath", "Csv_close")
    self.clearField("xpath", "Search_organisation")

    #Check Filters.
    self.scrollDown()

    #Click on filter
    self.clickOn("xpath", "Filter")
    self.wait(3)

    #Select AND or OR.
    self.setDropDownList("Filter_and_or")

    #Click on plus to add a filter.
    self.clickOn("xpath", "Filter_plus")

    #Set filter type.
    self.setDropDownList("Filter_type1")

    #Set Filter value.
    self.writeTextField("xpath", "Enter_filter1_value")

    #Set second filter.
    self.setDropDownList("Filter_type2")

    #Set second filters value.
    self.writeTextField("xpath", "Enter_filter2_value")

    #Click to start finding results on the basis of filters.
    self.clickOn("xpath", "Find")
    self.wait(3)

    #Reload Grid.
    self.clickOn("xpath", "Reload_grid")
    self.scrollDown()

    #Check column functionality, click on column.
    self.clickOn("xpath", "Column")
    self.wait(3)

    #Click on remove all to remove all options.
    self.clickOn("xpath", "Remove_all")
    self.wait(3)

    #Click to add "Name" column.
    self.clickOn("xpath", "Name")
    self.wait(3)

    #Click to add "Tags" column.
    self.clickOn("xpath", "Tag")
    self.wait(3)

    #Click to add "Ideas" column.
    self.clickOn("xpath", "Ideas")
    self.wait(3)

    #Click on OK.
    self.clickOn("xpath", "OK")

    #Search an organisation.
    self.scrollDown()
    self.wait(3)

    #Clear Organisation search field.
    self.clearField("xpath", "Search_organisation")

    #Write an Organisations name, say "Melange".
    self.writeTextField("xpath", "Search_organisation")
    self.wait(3)

    #Click on Organisations name, say "Melange".
    self.clickOn("xpath", "Select_org")
    self.wait(20)

    #Go back to accepted organisations main page.
    self.Browser.get(self.obj_id['Accepted_orgs_url'])
    self.clearField("xpath", "Search_organisation")
    self.scrollDown()

  def tearDown(self):
    self.teardown()
