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

""" Student registration: A student try to registers himself/herself on melange.
                          But he entered some invalid inputs. This test case
                          assert all those error messages and enter valid data in
                          the registration form to successfully create a profile.
"""

import unittest

from melange_functional_actions import FunctionalTestCase

class NewStudentRegistrationTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters('./tests/functional/testdata_melange.xls', 'TC02')
    
  def testForTryingToRegisterWithWrongInputs(self):    
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
    
    #Clear invalid user name, assert error message and enter a valid user name.
    self.clearFieldAssertErrorMessageAndEnterData("Wrong_username", "Correct_username")

    #Clear invalid Home Page url, assert error message and enter a valid url.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_home_url", "Valid_home_url")

    #Clear invalid blog url, assert error message and enter valid blog url. 
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_blog_url", "Valid_blog_url")

    #Clear invalid photo url, assert error message and enter a valid photo url.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_photo_url", "Valid_photo_url")

    #Clear invalid First Name, assert error message and enter a valid name.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_given_name", "Valid_given_name")

    #Clear invalid Last name, assert error message and enter a valid last name.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_surname", "Valid_surname")

    #Clear invalid email, assert error message and enter a valid email address.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_email", "Valid_email")

    """Clear invalid residential address, assert error message and enter a valid 
       residential address.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_residential_address",\
                                         "Valid_residential_address")
    """Clear invalid extra street address, assert error message and enter a 
       valid extra street address.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_extra_street_address",\
                                        "Valid_extra_street_address")
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Clear invalid city name, assert error message and enter a valid city name.
    self.clearFieldAssertErrorMessageAndEnterData("City_name_is_required", "Valid_city_name")

    #Clear invalid state name,assert error message and enter a valid state name.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_state_name", "Valid_state_name")

    #Clear invalid postal code, assert error message and enter a valid code.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_postal_code", "Valid_postal_code")

    #Clear invalid phone contact, assert error message and enter a valid number.
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_phone", "Valid_phone")

    """Clear invalid shipping street address, assert error message and enter a 
    valid last name.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_shipping_street", \
                                             "Valid_shipping_street")

    """Clear invalid extra shipping street address, assert error message and
       enter a valid extra shipping street address. 
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_extra_shipping_address",\
                                         "Valid_extra_shipping_address")

    """Clear invalid city name, assert error message and enter a valid 
       city name for shipment."""
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_shipment_city",\
                                          "Valid_shipment_city")

    """Clear invalid state name, assert error message and enter a valid 
       state name for shipment."""
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_shipment_state",\
                                          "Valid_shipment_state")

    """Clear invalid postal code, assert error message and enter a valid 
       postal code."""
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_shipment_postal_code",\
                                           "Valid_shipment_postal_code")

    """Clear invalid date of birth, assert error message and enter a valid 
       date of birth.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_date_of_birth",\
                                           "Valid_date_of_birth")

    """Clear invalid graduation year, assert error message and enter a valid 
       graduation year.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_graduation_year",\
                                          "Valid_graduation_year")

    """Clear invalid school home page url, assert error message and enter a 
       valid graduation year.
    """
    self.clearFieldAssertErrorMessageAndEnterData("Invalid_school_homepage_url",\
                                           "Valid_school_homepage_url")

    #Submit
    self.clickOn("xpath", "Submit_button")
    self.wait(5)
    
    """ Check if a student has already registered with this user name.
        if true change the user name and submit the form again.
    """
    if self.isElementDisplayed(5, "Data_can_not_be_saved") is True:
      text = self.Browser.find_element_by_xpath("//*[@id='flash-message']/p").text
      if text == "Sorry, we could not save your data. Please fix the errors mentioned below.":  
        self.assertError(text)
      if text == "Data saved successfully.":
        pass 

  def tearDown(self):
    self.teardown()
