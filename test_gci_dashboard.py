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

""" GCI Dasboard: This test case test all the functionality provided to a GCI
                  student from Dashboard Page.
"""

import unittest

from melange_functional_actions import *


class GCIDashboardTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):

    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters('/home/syed/Desktop/testdata_melange.xls', 'GCI_Dashboard_Test')    
     
  def test_GCI_Dashboard(self):

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Code In Contest", self.Browser.title)

    #Check if "How Google Code In Works" is present.
    self.assertText("How Google Code-In Works")
  
    #Scroll down.
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register.
    self.clickOn("xpath", "Register_Button")

    #Age Check.
    self.wait(3)
    self.writeTextField("xpath", "Age_check")

    #Click on submit.
    self.clickOn("xpath", "Submit_age")
  
    #Test env asks for email id, clear the field, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()
    self.wait(3) 

    #Wait for the page load completely, then fill the user name field.
    self.waitAndEnterText(5, "xpath", "Username")

    #Fill the public name field.  
    self.writeTextField("id", "Public_name")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Fill IM network field.
    self.writeTextField("id", "Im_network")

    #Fill IM handle field.
    self.writeTextField("id", "Im_handle")
  
    #Enter a valid home page address.
    self.writeTextField("id", "Home_page_url")
  
    #Enter a valid blog address.
    self.writeTextField("id", "Blog_url")
  
    #Set Avatar Color.
    self.wait(2)
    self.setDropDownList("Avatar")

    #Enter Given Name.
    self.writeTextField("id", "First_name")

    #Enter Surname.
    self.writeTextField("id", "Last_name")

    #Enter Email.
    self.writeTextField("id", "Email")

    #Enter Resedential Street Adress.
    self.writeTextField("id", "Res_street")

    #Enter Extra Residential Adress.
    self.writeTextField("id", "Res_street_extra")

    #Enter the City.
    self.writeTextField("id", "City")

    #Enter State.
    self.writeTextField("id", "State")

    #Traverse through all the country names and select India From the List.
    self.setDropDownList("Country")
    self.wait(2)

    #Enter Postal code.
    self.writeTextField("xpath", "Postal_code")    

    #Enter phone nuumber.
    self.writeTextField("xpath", "Phone")
    
    #Enter Full recipient name.  
    self.writeTextField("xpath", "Full_recepient_name")

    #Enter Shipping Street Adress.
    self.writeTextField("xpath", "Shipping_street")

    #Enter Extra Shipping Street Adress.
    self.writeTextField("xpath", "Shipping_street_extra")

    #Enter the city name for shipment.
    self.writeTextField("xpath", "Shipping_city")

    #Enter State.
    self.writeTextField("xpath", "Shipping_state")
  
    #Traverse through all the country names and select a country From the List
    self.setDropDownList("Shipping_country")    

    #Enter postal code.
    self.writeTextField("xpath", "Shipping_postal_code")

    #Traverse through the list and select T-shirt Style.
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a T-shirt size.
    self.setDropDownList("T_shirt_size")

    #Select Gender as female.  
    self.setDropDownList("Gender")

    #Fill the text area.
    self.writeTextField("xpath", "How_did_you_hear_about_gci")

    #Unset the checkbox for Automatic_task_subscription.
    self.toggleCheckBox("xpath", "Automatic_task_subscription")
 
    #Enter School Name.
    self.writeTextField("xpath", "School_name")   

    #Select School Country.
    self.setDropDownList("School_country")
   
    #Enter Expected Graduation.  
    self.writeTextField("xpath", "Expected_graduation")

    #Enter Grade.  
    self.writeTextField("xpath", "Grade")

    #Submit.
    self.clickOn("xpath", "Submit_button")
    
    if self.isElementDisplayed(5, "Data_can_not_be_saved") is True:
      text = self.Browser.find_element_by_xpath("//*[@id='flash-message']/p").text
      if text == "Sorry, we could not save your data. Please fix the errors mentioned below.":  
        self.assertError(text)
      if text == "Data saved successfully.":
        pass
    
    #Click on GCI Dashboard.
    self.wait(5)
    self.clickOn("xpath", "Dashboard")

    #Click on Invites to me link.
    self.wait(3)
    self.clickOn("xpath", "Invites_to_me")
    self.wait(3)
    self.clickOn("xpath", "Filter_records")
    self.wait(3)
    self.clickOn("xpath", "Filter_plus")
    self.wait(3)
    self.setDropDownList("Filter_by")
    self.wait(3)
    self.clickOn("xpath", "Reset")
    self.wait(3)
    self.clickOn("xpath", "Close")
    self.wait(3)
    self.clickOn("xpath", "Refresh")
    self.wait(3)
    self.clickOn("xpath", "Column")
    self.wait(3)
    self.clickOn("xpath", "Add_key")
    self.wait(3)
    self.clickOn("xpath", "OK")
    
    self.clickOn("xpath", "Dashboard")
    self.wait(3)
    self.clickOn("xpath", "My_requests")
    self.wait(3)
    self.clickOn("xpath", "Requests_filter")
    self.wait(3)
    self.setDropDownList("Requests_key")
    self.wait(3)
    self.clickOn("xpath", "Request_filter_reset")
    self.wait(3)
    self.clickOn("xpath", "Requests_filter_close")
    self.wait(3)
    self.clickOn("xpath", "Requests_refresh")
    self.wait(3)
    self.clickOn("xpath", "Requests_column")
    self.wait(3)
    self.clickOn("xpath", "Request_column_key")
    self.wait(3)
    self.clickOn("xpath", "Request_OK")
    self.wait(3)
  
    
  def tearDown(self):
    self.teardown()


if __name__ == "__main__":
  unittest.main()

