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

""" Student registration: A student registers himfunctest/herfunctest by entering all
                          correct values in the registration form.
"""

import unittest

from melange_functional_actions import *


class StudentRegistrationTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):
    functest.setup()
    functest.getParameters('/home/syed/Desktop/testdata_melange.xls', 'TC01')    
     
  def testForTryingToRegisterAsAStudent(self):

    #Test Url, Change it according to your local dev environment.
    functest.Browser.get(functest.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", functest.Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    functest.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    functest.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register 
    functest.clickOn("xpath", 'Register_Button')
  
    #Test env asks for email id, clear the field, enter email and click on login.
    functest.wait(3) 
    functest.login()

    #Wait for the page load completely, then fill the user name field
    functest.waitAndEnterText(5, "xpath", "Username")
    
    #Fill the public name field  
    functest.writeTextField("id", "Public_name")
    functest.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Fill IM network field
    functest.writeTextField("id", "Im_network")

    #Fill IM handle field
    functest.writeTextField("id", "Im_handle")
  
    #Enter a valid home page address
    functest.writeTextField("id", "Home_page_url")
  
    #Enter a valid blog address
    functest.writeTextField("id", "Blog_url")
  
    #Enter photo url
    functest.writeTextField("id", "Thumbnail_photo_url")

    #Enter Given Name
    functest.writeTextField("id", "First_name")

    #Enter Surname
    functest.writeTextField("id", "Last_name")

    #Enter Email
    functest.writeTextField("id", "Email")

    #Enter Resedential Street Adress
    functest.writeTextField("id", "Res_street")

    #Enter Extra Residential Adress
    functest.writeTextField("id", "Res_street_extra")

    #Enter the City
    functest.writeTextField("id", "City")

    #Enter State
    functest.writeTextField("id", "State")

    #Traverse through all the country names and select India From the List
    functest.setDropDownList("Country")
    functest.wait(2)

    #Enter Postal code
    functest.writeTextField("xpath", "Postal_code")    

    #Enter phone nuumber
    functest.writeTextField("xpath", "Phone")
    
    #Select publish location
    functest.toggleCheckBox("xpath", "Publish_my_location")

    #Enter Full recipient name  
    functest.writeTextField("xpath", "Full_recepient_name")

    #Enter Shipping Street Adress
    functest.writeTextField("xpath", "Shipping_street")

    #Enter Extra Shipping Street Adress
    functest.writeTextField("xpath", "Shipping_street_extra")

    #Enter the city name for shipment
    functest.writeTextField("xpath", "Shipping_city")

    #Enter State
    functest.writeTextField("xpath", "Shipping_state")
  
    #Traverse through all the country names and select a country From the List
    functest.setDropDownList("Shipping_country")    

    #Enter postal code
    functest.writeTextField("xpath", "Shipping_postal_code")

    #Enter the date of birth
    functest.writeTextField("xpath", "Birth_date")
  
    #Traverse through the list and select T-shirt Style
    functest.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a T-shirt size
    functest.setDropDownList("T_shirt_size")

    #Select Gender as female   
    functest.setDropDownList("Gender")

    #Fill the text area
    functest.writeTextField("xpath", "How_did_you_hear_about_gsoc")

    #Unset the checkbox for Notification to new comments
    functest.toggleCheckBox("xpath", "Notify_to_new_public_comments")
 
    #Enter School Name
    functest.writeTextField("xpath", "School_name")   

    #Select School Country
    functest.setDropDownList("School_country")
  
    #Enter Major Subject
    functest.writeTextField("xpath", "Major_subject")
  
    #Select Degree
    functest.setDropDownList("Degree")
  
    #Enter Expected Graduation  
    functest.writeTextField("xpath", "Expected_graduation")
  
    #Enter School Homepage URL
    functest.writeTextField("xpath", "School_homepage")
 
    #Submit
    functest.clickOn("xpath", "Submit_button")
    
    """ Check if a student has already registered with this user name.
        if true change the user name and submit the form again.
    """
    if functest.isElementDisplayed(5, "Already_registered") is True:
      functest.fillRandomValue("Username")
      functest.clickOn("xpath", "Submit_button")
    elif functest.isElementDisplayed(5, "Data_can_not_be_saved") is True:
      raise
    else:
      pass
      
    

  def tearDown(self):
    functest.teardown()

functest = FunctionalTestCase()

if __name__ == "__main__":
  unittest.main()

