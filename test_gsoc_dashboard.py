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

class GsocDashboardTest(FunctionalTestCase):
  """ GSoC Dashboard: This test case test the functionality of
      GSoC Dashboard.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGsocDashboardProposal(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSOC_Dashboard")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on register.
    self.clickOn("xpath", "Register_Button")
  
    #For local environment, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Wait for the page load completely, then fill the user name field.
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
  
    #Enter photo url.
    self.writeTextField("id", "Thumbnail_photo_url")

    #Enter given name.
    self.writeTextField("id", "First_name")

    #Enter surname.
    self.writeTextField("id", "Last_name")

    #Enter email.
    self.writeTextField("id", "Email")

    #Enter resedential street address.
    self.writeTextField("id", "Res_street")

    #Enter extra residential address.
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
    
    #Select publish location.
    self.toggleCheckBox("xpath", "Publish_my_location")

    #Enter full recipient name.
    self.writeTextField("xpath", "Full_recepient_name")

    #Enter shipping street address.
    self.writeTextField("xpath", "Shipping_street")

    #Enter extra shipping street address.
    self.writeTextField("xpath", "Shipping_street_extra")

    #Enter the city name for shipment.
    self.writeTextField("xpath", "Shipping_city")

    #Enter state.
    self.writeTextField("xpath", "Shipping_state")
  
    #Traverse through country names and select a country from the list.
    self.setDropDownList("Shipping_country")    

    #Enter postal code.
    self.writeTextField("xpath", "Shipping_postal_code")

    #Enter the date of birth.
    self.writeTextField("xpath", "Birth_date")
  
    #Traverse through the list and select t-shirt style.
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a t-shirt size.
    self.setDropDownList("T_shirt_size")

    #Select gender as female. 
    self.setDropDownList("Gender")

    #Fill the text area.
    self.writeTextField("xpath", "How_did_you_hear_about_gsoc")

    #Unset the checkbox for notification to new comments.
    self.toggleCheckBox("xpath", "Notify_to_new_public_comments")
 
    #Enter school name.
    self.writeTextField("xpath", "School_name")   

    #Select school country.
    self.setDropDownList("School_country")
  
    #Enter major subject.
    self.writeTextField("xpath", "Major_subject")
  
    #Select degree.
    self.setDropDownList("Degree")
  
    #Enter expected graduation.
    self.writeTextField("xpath", "Expected_graduation")
  
    #Enter school homepage URL.
    self.writeTextField("xpath", "School_homepage")
 
    #Submit.
    self.clickOn("xpath", "Submit_button")

    #Check if data saved successfully.
    self.checkRegistrationSuccess("Message_from_melange")
 
    #Click on GSoC dashboard.
    self.wait(5)
    self.clickOn("xpath", "GSoC_dashboard")

    #Click on "Invites to me" link.
    self.wait(3)
    self.clickOn("xpath", "GSoC_proposal")

    #Click on filter.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter")

    #Add a rule.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_add_rule")

    #Select filter.
    self.wait(3)
    self.setDropDownList("Proposal_filter_name")

    #Click to reset filters.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_reset")

    #Click to close the filter menu.
    self.wait(3)
    self.clickOn("xpath", "Proposal_filter_close")

    #Click on refresh to reload the grid.
    self.wait(3)
    self.clickOn("xpath", "Proposal_refresh")

    #Click on column.
    self.wait(3)
    self.clickOn("xpath", "Proposal_columns")

    #Click to add key.
    self.wait(3)
    self.clickOn("xpath", "Proposal_columns_add_key")

    #Click OK.
    self.wait(3)
    self.clickOn("xpath", "Proposal_OK_button")

  def testGsocDashboardTodo(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSOC_Dashboard")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Clink login on GSoC menu.
    self.clickOn("xpath", "Login_link")
  
    #For local environment, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()
    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

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

    #Click on column.
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
