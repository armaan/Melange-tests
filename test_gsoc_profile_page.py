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

class ProfilePageTest(FunctionalTestCase):
  """ This test case test the functionality of GSoC Profile Page.
  """
  def setUp(self):
    self.init()
    self.setup()
    
  def testProfileNoRegisteredUser(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSOC_Profile_test")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Scroll down.
    self.scrollDown()

    #Click on Register 
    self.clickOn("xpath", "Register_Button")

    #Test env asks for email id, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()
    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()
    self.wait(3)

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

    #Enter given Name.
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

    #Traverse the country names and select India From the List.
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
  
    #Traverse the country names and select a country from list.
    self.setDropDownList("Shipping_country")    

    #Enter postal code.
    self.writeTextField("xpath", "Shipping_postal_code")

    #Enter the date of birth.
    self.writeTextField("xpath", "Birth_date")
  
    #Traverse through the list and select t-shirt Style.
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a t-shirt size.
    self.setDropDownList("T_shirt_size")

    #Select gender as female.
    self.setDropDownList("Gender")

    #Fill the text area.
    self.writeTextField("xpath", "How_did_you_hear_about_gsoc")

    #Unset the checkbox for Notification to new comments.
    self.toggleCheckBox("xpath", "Notify_to_new_public_comments")
 
    #Enter school Name.
    self.writeTextField("xpath", "School_name")   

    #Select school Country.
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

    #Clear old public name and enter new public name.
    self.wait(2)
    self.clearField("id", "Public_name")
    self.wait(2) 
    self.writeTextField("id", "New_public_name")
    
    #Clear old IM handle and enter new IM handle.
    self.wait(2)     
    self.clearField("id", "Im_handle")
    self.wait(2)     
    self.writeTextField("id", "New_im_handle")

    #Enter new IM network name.
    self.wait(2)
    self.scrollDown() 
    self.clearField("id", "Im_network")
    self.wait(2)     
    self.writeTextField("id", "New_im_network")

    #Clear old homepage url and enter new homepage url.
    self.wait(2)     
    self.clearField("id", "Home_page_url")
    self.wait(3)     
    self.writeTextField("id", "New_homepage_url")
    self.wait(3)

    #Clear old blog url and enter new blog url.     
    self.clearField("id", "Blog_url")
    self.wait(3) 
    self.writeTextField("id", "New_blog_url")
    self.wait(3)
    self.scrollDown()

    #Select new t-shirt size.   
    self.wait(3) 
    self.setDropDownList("New_t_shirt_size")

    #Clear old phone number and enter new phone number.
    self.wait(3) 
    self.clearField("xpath", "Phone")
    self.wait(3) 
    self.writeTextField("xpath", "New_phone_number")

    #Submit.
    self.clickOn("xpath", "Submit_button")
    
    #Check if data saved successfully.
    self.checkRegistrationSuccess("Message_from_melange")

  def testProfileRegisteredUser(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSOC_Profile_test")

    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Scroll down.
    self.scrollDown()

    #Click on Register 
    self.clickOn("xpath", "Register_Button")

    #Test env asks for email id, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()
    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()
    self.wait(3)

    #Clear old public name and enter new public name.
    self.wait(2)
    self.clearField("id", "Public_name")
    self.wait(2) 
    self.writeTextField("id", "New_public_name")
    
    #Clear old IM handle and enter new IM handle.
    self.wait(2)     
    self.clearField("id", "Im_handle")
    self.wait(2)     
    self.writeTextField("id", "New_im_handle")

    #Enter new IM network name.
    self.wait(2)
    self.scrollDown() 
    self.clearField("id", "Im_network")
    self.wait(2)     
    self.writeTextField("id", "New_im_network")

    #Clear old homepage url and enter new homepage url.
    self.wait(2)     
    self.clearField("id", "Home_page_url")
    self.wait(3)     
    self.writeTextField("id", "New_homepage_url")
    self.wait(3)

    #Clear old blog url and enter new blog url.     
    self.clearField("id", "Blog_url")
    self.wait(3) 
    self.writeTextField("id", "New_blog_url")
    self.wait(3)
    self.scrollDown()

    #Select new t-shirt size.   
    self.wait(3) 
    self.setDropDownList("New_t_shirt_size")

    #Clear old phone number and enter new phone number.
    self.wait(3) 
    self.clearField("xpath", "Phone")
    self.wait(3) 
    self.writeTextField("xpath", "New_phone_number")

    #Clear old public name and enter new public name.
    self.wait(2)
    self.clearField("id", "Public_name")
    self.wait(2) 
    self.writeTextField("id", "New_public_name")
    
    #Clear old IM handle and enter new IM handle.
    self.wait(2)     
    self.clearField("id", "Im_handle")
    self.wait(2)     
    self.writeTextField("id", "New_im_handle")

    #Enter new IM network name.
    self.wait(2)
    self.scrollDown() 
    self.clearField("id", "Im_network")
    self.wait(2)     
    self.writeTextField("id", "New_im_network")

    #Clear old homepage url and enter new homepage url.
    self.wait(2)     
    self.clearField("id", "Home_page_url")
    self.wait(3)     
    self.writeTextField("id", "New_homepage_url")
    self.wait(3)

    #Clear old blog url and enter new blog url.     
    self.clearField("id", "Blog_url")
    self.wait(3) 
    self.writeTextField("id", "New_blog_url")
    self.wait(3)
    self.scrollDown()

    #Select new t-shirt size.   
    self.wait(3) 
    self.setDropDownList("New_t_shirt_size")

    #Clear old phone number and enter new phone number.
    self.wait(3) 
    self.clearField("xpath", "Phone")
    self.wait(3) 
    self.writeTextField("xpath", "New_phone_number")

    #Submit.
    self.clickOn("xpath", "Submit_button")
    
    #Check if data saved successfully.
    self.checkRegistrationSuccess("Message_from_melange")
   
  def tearDown(self):
    self.teardown()
