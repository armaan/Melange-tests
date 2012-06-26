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

""" GSoC Dashboard: This test case test the functionality of GSoC Dashboard.
"""

import unittest

from melange_functional_actions import *

class GsocDashboardTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters('/home/syed/Desktop/testdata_melange.xls', 'GSOC_Dashboard')    
     
  def testForGsocDashboard(self):
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register 
    self.clickOn("xpath", 'Register_Button')
  
    #For local environment. Clear the field, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Wait for the page load completely, then fill the user name field
    self.waitAndEnterText(5, "xpath", "Username")
    
    #Fill the public name field  
    self.writeTextField("id", "Public_name")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Fill IM network field
    self.writeTextField("id", "Im_network")

    #Fill IM handle field
    self.writeTextField("id", "Im_handle")
  
    #Enter a valid home page address
    self.writeTextField("id", "Home_page_url")
  
    #Enter a valid blog address
    self.writeTextField("id", "Blog_url")
  
    #Enter photo url
    self.writeTextField("id", "Thumbnail_photo_url")

    #Enter Given Name
    self.writeTextField("id", "First_name")

    #Enter Surname
    self.writeTextField("id", "Last_name")

    #Enter Email
    self.writeTextField("id", "Email")

    #Enter Resedential Street Adress
    self.writeTextField("id", "Res_street")

    #Enter Extra Residential Adress
    self.writeTextField("id", "Res_street_extra")

    #Enter the City
    self.writeTextField("id", "City")

    #Enter State
    self.writeTextField("id", "State")

    #Traverse through all the country names and select India From the List
    self.setDropDownList("Country")
    self.wait(2)

    #Enter Postal code
    self.writeTextField("xpath", "Postal_code")    

    #Enter phone nuumber
    self.writeTextField("xpath", "Phone")
    
    #Select publish location
    self.toggleCheckBox("xpath", "Publish_my_location")

    #Enter Full recipient name  
    self.writeTextField("xpath", "Full_recepient_name")

    #Enter Shipping Street Adress
    self.writeTextField("xpath", "Shipping_street")

    #Enter Extra Shipping Street Adress
    self.writeTextField("xpath", "Shipping_street_extra")

    #Enter the city name for shipment
    self.writeTextField("xpath", "Shipping_city")

    #Enter State
    self.writeTextField("xpath", "Shipping_state")
  
    #Traverse through all the country names and select a country From the List
    self.setDropDownList("Shipping_country")    

    #Enter postal code
    self.writeTextField("xpath", "Shipping_postal_code")

    #Enter the date of birth
    self.writeTextField("xpath", "Birth_date")
  
    #Traverse through the list and select T-shirt Style
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a T-shirt size
    self.setDropDownList("T_shirt_size")

    #Select Gender as female   
    self.setDropDownList("Gender")

    #Fill the text area
    self.writeTextField("xpath", "How_did_you_hear_about_gsoc")

    #Unset the checkbox for Notification to new comments
    self.toggleCheckBox("xpath", "Notify_to_new_public_comments")
 
    #Enter School Name
    self.writeTextField("xpath", "School_name")   

    #Select School Country
    self.setDropDownList("School_country")
  
    #Enter Major Subject
    self.writeTextField("xpath", "Major_subject")
  
    #Select Degree
    self.setDropDownList("Degree")
  
    #Enter Expected Graduation  
    self.writeTextField("xpath", "Expected_graduation")
  
    #Enter School Homepage URL
    self.writeTextField("xpath", "School_homepage")
 
    #Submit
    self.clickOn("xpath", "Submit_button")

    if self.isElementDisplayed(5, "Data_can_not_be_saved") is True:
      text = self.Browser.find_element_by_xpath("//*[@id='flash-message']/p").text
      if text == "Sorry, we could not save your data. Please fix the errors mentioned below.":  
        self.assertError(text)
      if text == "Data saved successfully.":
        pass

    #Click on GSoC Dashboard.
    self.wait(5)
    self.clickOn("xpath", "GSoC_dashboard")

    #Click on "Invites to me" link.
    self.wait(3)
    self.clickOn("xpath", "GSoC_proposal")

    #Click on Filter
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter")

    #Add a rule.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_add_rule")

    #Select filter.
    self.wait(3)
    self.setDropDownList("Proposal_filter_name")

    #Click to Reset Filters.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_reset")

    #Click to close the filter menu.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_close")

    #Click on Refresh to reload the grid.
    self.wait(3)
    self.clickOn("xpath", "Proposal_refresh")

    #Click on Column.
    self.wait(3)
    self.clickOn("xpath", "Proposal_columns")

    #Click to add key.
    self.wait(3)
    self.clickOn("xpath", "Proposal_columns_add_key")

    #Click OK.
    self.wait(3)
    self.clickOn("xpath", "Proposal_OK_button")

    #Go back to dashboard.
    self.wait(3)
    self.clickOn("xpath", "GSoC_dashboard")

    #Click on My Todos.
    self.wait(3)
    self.clickOn("xpath", "My_todos")

    #Click on My Todos filter.
    self.wait(3)
    self.clickOn("xpath", "My_todos_filter")

    #Add a rule.
    self.wait(3)
    self.clickOn("xpath", "My_todos_filter_add_rule")

    #Set a value for filter.
    self.wait(3)
    self.setDropDownList("My_todos_name")

    #Reset filter.
    self.wait(3)
    self.clickOn("xpath", "My_todos_filter_reset")

    #Close filter.
    self.wait(3)
    self.clickOn("xpath", "My_todos_filter_close")

    #Reload the grid.
    self.wait(3)
    self.clickOn("xpath", "My_todos_refresh")

    #Click on Column.
    self.wait(3)
    self.clickOn("xpath", "My_todos_columns")

    #Select one more column value.
    self.wait(3)
    self.clickOn("xpath", "My_todos_columns_add_field")

    #Click on OK.
    self.wait(3)
    self.clickOn("xpath", "My_todos_ok_button")  
    
  def tearDown(self):
    self.teardown()

if __name__ == "__main__":
  unittest.main()
