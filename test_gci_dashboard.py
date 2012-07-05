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

class GCIDashboardTest(FunctionalTestCase):
  """ GCI Dasboard: This test script test all the functionality
  provided to a GCI student from Dashboard Page.
  """
  def setUp(self):
    self.init()
    self.setup()  
     
  def testGCIDashboard(self):
    #Load test data.
    self.getParameters(self.Data_source, "GCI_Dashboard_Test")

    #Test url, change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Code In Contest", self.Browser.title)

    #Check if "How Google Code In Works" is present.
    self.assertText("How Google Code-In Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on register.
    self.clickOn("xpath", "Register_Button")

    #Age check.
    self.wait(3)
    self.writeTextField("xpath", "Age_check")

    #Click on submit.
    self.clickOn("xpath", "Submit_age")
  
    #Test env asks for email id, enter email and click on login.
    self.wait(5) 
    self.loginOnLocalhost()
    self.wait(3)
    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount() 

    #Wait for the page to load completely, fill the user name field.
    self.waitAndEnterText(5, "xpath", "Username")

    #Fill the public name field.  
    self.writeTextField("id", "Public_name")
    self.scrollDown()

    #Fill IM network field.
    self.writeTextField("id", "Im_network")

    #Fill IM handle field.
    self.writeTextField("id", "Im_handle")
  
    #Enter a valid home page address.
    self.writeTextField("id", "Home_page_url")
  
    #Enter a valid blog address.
    self.writeTextField("id", "Blog_url")
  
    #Set avatar Color.
    self.wait(2)
    self.setDropDownList("Avatar")

    #Enter given Name.
    self.writeTextField("id", "First_name")

    #Enter surname.
    self.writeTextField("id", "Last_name")

    #Enter email.
    self.writeTextField("id", "Email")

    #Enter resedential street adress.
    self.writeTextField("id", "Res_street")

    #Enter extra residential adress.
    self.writeTextField("id", "Res_street_extra")

    #Enter the city.
    self.writeTextField("id", "City")

    #Enter state.
    self.writeTextField("id", "State")

    #Traverse through country names and select a country from the list.
    self.setDropDownList("Country")
    self.wait(2)

    #Enter postal code.
    self.writeTextField("xpath", "Postal_code")    

    #Enter phone number.
    self.writeTextField("xpath", "Phone")
    
    #Enter full recipient name.  
    self.writeTextField("xpath", "Full_recepient_name")

    #Enter shipping street adress.
    self.writeTextField("xpath", "Shipping_street")

    #Enter extra shipping street adress.
    self.writeTextField("xpath", "Shipping_street_extra")

    #Enter the city name for shipment.
    self.writeTextField("xpath", "Shipping_city")

    #Enter state.
    self.writeTextField("xpath", "Shipping_state")
  
    #Traverse through country names and select a country from the list.
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
 
    #Enter school name.
    self.writeTextField("xpath", "School_name")   

    #Select school country.
    self.setDropDownList("School_country")
   
    #Enter expected graduation.  
    self.writeTextField("xpath", "Expected_graduation")

    #Enter grade.  
    self.writeTextField("xpath", "Grade")

    #Submit.
    self.clickOn("xpath", "Submit_button")
    
    #Check if data saved successfully.
    self.checkRegistrationSuccess("Message_from_melange")
    
    #Click on GCI Dashboard.
    self.wait(5)
    self.clickOn("xpath", "Dashboard")

    #Click on "Invites to me" link.
    self.wait(3)
    self.clickOn("xpath", "Invites_to_me")

    #Click on filter.
    self.wait(3)
    self.clickOn("xpath", "Filter_records")

    #Add a rule.
    self.wait(3)
    self.clickOn("xpath", "Filter_plus")

    #Select filter.
    self.wait(3)
    self.setDropDownList("Filter_by")

    #Click to reset filters.
    self.wait(3)
    self.clickOn("xpath", "Reset")

    #Click to close the filter menu.
    self.wait(3)
    self.clickOn("xpath", "Close")

    #Click on Refresh to reload the grid.
    self.wait(3)
    self.clickOn("xpath", "Refresh")

    #Click on column.
    self.wait(3)
    self.clickOn("xpath", "Column")

    #Click to add key.
    self.wait(3)
    self.clickOn("xpath", "Add_key")

    #Click ok.
    self.wait(3)
    self.clickOn("xpath", "OK")

    #Go back to dashboard.
    self.wait(3)
    self.clickOn("xpath", "Dashboard")

    #Click on my requests link.
    self.wait(3)
    self.clickOn("xpath", "My_requests")

    #Click on filter.
    self.wait(3)
    self.clickOn("xpath", "Requests_filter")

    #Set a value for filter.
    self.wait(3)
    self.setDropDownList("Requests_key")

    #Reset filter.
    self.wait(3)
    self.clickOn("xpath", "Request_filter_reset")

    #Close filter.
    self.wait(3)
    self.clickOn("xpath", "Requests_filter_close")

    #Reload the grid.
    self.wait(3)
    self.clickOn("xpath", "Requests_refresh")

    #Click on column.
    self.wait(3)
    self.clickOn("xpath", "Requests_column")

    #Select one more column value.
    self.wait(3)
    self.clickOn("xpath", "Request_column_key")

    #Click on OK.
    self.wait(3)
    self.clickOn("xpath", "Request_OK")  
    
  def tearDown(self):
    self.teardown()
