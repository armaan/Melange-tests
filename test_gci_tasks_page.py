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

class GCITasksTest(FunctionalTestCase):
  """This script test the functionality of GCI Tasks Page.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGCITasks(self):
    #Load test data.
    self.getParameters(self.Data_source, "GCI_Tasks")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Code In Contest", self.Browser.title)

    #Check if "How Google Code-In Works" is present.
    self.assertText("How Google Code-In Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on Register. 
    self.clickOn("xpath", "Register_Button")

    #Age Check.
    self.wait(3)
    self.writeTextField("xpath", "Age_check")

    #Click on submit.
    self.clickOn("xpath", "Submit_age")
  
    #Test env asks for email id, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()
    self.wait(3)
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
  
    #Set Avatar color.
    self.wait(2)
    self.setDropDownList("Avatar")

    #Enter given name.
    self.writeTextField("id", "First_name")

    #Enter surname.
    self.writeTextField("id", "Last_name")

    #Enter email.
    self.writeTextField("id", "Email")

    #Enter residential street address.
    self.writeTextField("id", "Residential_street")

    #Enter extra residential address.
    self.writeTextField("id", "Residential_street_extra")

    #Enter the city.
    self.writeTextField("id", "City")

    #Enter state.
    self.writeTextField("id", "State")

    #Traverse through country names and select country from the list.
    self.setDropDownList("Country")
    self.wait(2)

    #Enter postal code.
    self.writeTextField("xpath", "Postal_code")    

    #Enter phone number.
    self.writeTextField("xpath", "Phone")
    
    #Enter Full recipient name. 
    self.writeTextField("xpath", "Full_recipient_name")

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

    #Traverse through the list and select t-shirt Style.
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a t-shirt size.
    self.setDropDownList("T_shirt_size")

    #Select gender as female.  
    self.setDropDownList("Gender")

    #Fill the text area.
    self.writeTextField("xpath", "How_did_you_hear_about_gci")

    #Unset the checkbox for Automatic_task_subscription.
    self.toggleCheckBox("xpath", "Automatic_task_subscription")
 
    #Enter school Name.
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

    #Go to main page.
    self.wait(3)
    self.Browser.get(self.obj_id["Url"])

    #Click on Search for tasks.
    self.wait(3)
    self.clickOn("xpath", "Search_for_tasks")

    #Click to select a task.
    self.wait(3)
    self.clickOn("xpath", "Select_task")

    #Claim the task.
    self.wait(3)
    self.clickOn("xpath", "Claim_task")

    #Post comment.
    self.wait(3)
    self.clickOn("xpath", "Post_comment")

    #Enter title.
    self.wait(3)
    self.writeTextField("xpath", "Title")

    #Enter Content.
    self.Browser.switch_to_frame("melange-content-textarea_ifr")
    self.wait(3)
    self.writeTextField("xpath", "Content")
    self.Browser.switch_to_default_content()

    #Submit.
    self.wait(3)
    self.clickOn("xpath", "Submit")
    
  def tearDown(self):
    self.teardown()
