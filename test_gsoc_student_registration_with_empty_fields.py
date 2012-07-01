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

import unittest

from melange_functional_actions import FunctionalTestCase

""" Student registration: Click on submit button and try to submit an empty form.
                          Assert error messages. Fill in mandatory fields and
                          successfully register on melange.
"""

class GSoCStudentRegistrationTest(unittest.TestCase, FunctionalTestCase):

  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters('./tests/functional/testdata_melange.xls', 'TC03')    
     
  def testForTryingToRegisterAsAStudent(self):

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

    #Submit
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.clickOn("xpath", "Submit_button")

    #Assert message "This field is required" and enter a user name.
    self.assertMessageAndEnterText("Username_required", "Username")

    #Assert message "This field is required" and enter a public name.
    self.assertMessageAndEnterText("Public_name_required", "Public_name")

    #Assert message "This field is required" and enter a First Name.
    self.assertMessageAndEnterText("First_name_required","First_name")

    #Assert message "This field is required" and enter a Last Name.
    self.assertMessageAndEnterText("Last_name_required", "Last_name")

    #Assert message "This field is required" and enter an email address.
    self.assertMessageAndEnterText("Email_required", "Email")

    #Assert message "This field is required" and enter a street address.
    self.assertMessageAndEnterText("Street_address_required", "Res_street")

    #Assert message "This field is required" and enter a city
    self.assertMessageAndEnterText("City_required", "City")

    #Assert message "This field is required" and enter a country.
    self.assertTextIn("Country_required")
    self.setDropDownList("Country")

    #Assert message "This field is required" and enter a postal code.
    self.assertMessageAndEnterText("Postal_code_required", "Postal_code")

    #Assert message "This field is required" and enter a phone number.
    self.assertMessageAndEnterText("Phone_number_required", "Phone")

    #Assert message "This field is required" and enter a date of birth"
    self.assertMessageAndEnterText("Birth_date_required", "Birth_date")

    #Assert message "This field is required" and enter a school name
    self.assertMessageAndEnterText("School_name_required", "School_name")

    #Assert message "This field is required" and enter the school country
    self.assertTextIn("School_country_required")
    self.setDropDownList("School_country")

    #Assert message "This field is required" and enter expected graduation year.
    self.assertMessageAndEnterText("Expected_graduation_required", "Expected_graduation")

    #Assert message "This field is required" and enter school hom page url.
    self.assertMessageAndEnterText("School_homepage_required", "School_homepage")

    #Submit
    self.Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    self.clickOn("xpath", "Submit_button")


  def tearDown(self):
    self.teardown()
