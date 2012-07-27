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

class StudentRegistrationTest(FunctionalTestCase):
  """ Student Registration Test: Test Cases to test the student registration
      process for GSoC on melange.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGSoCRegisterAsAStudent(self):
    #Load test data.
    self.getParameters(self.Data_source ,"GSOC_Student")

    #Test url, Change it according to your environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present on home page.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on Register.
    self.clickOn("xpath", "Register_Button")
  
    #For local environment. Clear the field, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Wait for the page load completely, then fill the user name field.
    self.waitAndEnterText(5, "xpath", "User_name")
    
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

    #Enter residential street address.
    self.writeTextField("id", "Residential_street")

    #Enter extra residential address.
    self.writeTextField("id", "Residential_street_extra")

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

    #Unset the check box for notification to new comments.
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

  def testGSoCRequiredFieldsToRegisterAsAStudent(self):
    self.getParameters(self.Data_source, "GSOC_Student_TC02")
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on Register.
    self.wait(3)
    self.clickOn("xpath", "Register_Button")
  
    #For local environment, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Submit.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "Submit_button")

    #Assert that student registration has failed as required fields are empty.
    self.assertText("Message_from_melange")

    #Assert message "This field is required" and enter a user name.
    self.assertMessageAndEnterText("Username_required", "Username")

    #Assert message "This field is required" and enter a public name.
    self.assertMessageAndEnterText("Public_name_required", "Public_name")

    #Assert message "This field is required" and enter a first name.
    self.assertMessageAndEnterText("First_name_required","First_name")

    #Assert message "This field is required" and enter a last name.
    self.assertMessageAndEnterText("Last_name_required", "Last_name")

    #Assert message "This field is required" and enter an email address.
    self.assertMessageAndEnterText("Email_required", "Email")

    #Assert message "This field is required" and enter a street address.
    self.assertMessageAndEnterText("Street_address_required", "Res_street")

    #Assert message "This field is required" and enter a city.
    self.assertMessageAndEnterText("City_required", "City")

    #Assert message "This field is required" and enter a country.
    self.assertTextIn("Country_required")
    self.setDropDownList("Country")

    #Assert message "This field is required" and enter a postal code.
    self.assertMessageAndEnterText("Postal_code_required", "Postal_code")

    #Assert message "This field is required" and enter a phone number.
    self.assertMessageAndEnterText("Phone_number_required", "Phone")

    #Assert message "This field is required" and enter a date of birth".
    self.assertMessageAndEnterText("Birth_date_required", "Birth_date")

    #Assert message "This field is required" and enter a school name.
    self.assertMessageAndEnterText("School_name_required", "School_name")

    #Assert message "This field is required" and enter the school country.
    self.assertTextIn("School_country_required")
    self.setDropDownList("School_country")

    #Assert message "This field is required" enter expected graduation year.
    self.assertMessageAndEnterText("Expected_graduation_required", 
                                   "Expected_graduation")

    #Assert message "This field is required" and enter school homepage url.
    self.assertMessageAndEnterText("School_homepage_required", 
                                   "School_homepage")

    #Submit.
    self.scrollDown()
    self.clickOn("xpath", "Submit_button")

    #Check if data saved successfully after filling all required fields.
    self.checkRegistrationSuccess("Message_from_melange")

  def testGSoCStudentRegistrationFailsOnInvalidInputs(self):
    #Load test data.
    self.getParameters(self.Data_source ,"GSOC_Student_TC03")

    #Test url, Change it according to your environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present on home page.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.scrollDown()
  
    #Click on Register.
    self.clickOn("xpath", "Register_Button")
  
    #For local environment. Clear the field, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Wait for the page load completely, then fill the user name field.
    self.waitAndEnterText(5, "xpath", "User_name")
    
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

    #Enter residential street address.
    self.writeTextField("id", "Residential_street")

    #Enter extra residential address.
    self.writeTextField("id", "Residential_street_extra")

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

    #Unset the check box for notification to new comments.
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

    #Assert that student registration has failed.
    self.wait(3)
    self.assertText("Message_from_melange")    

  def tearDown(self):
    self.teardown()
