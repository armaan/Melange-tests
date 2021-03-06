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

""" Student registration: A student registers himself/herself by entering all
                          correct values in the registration form.
"""

import unittest

from base import FunctionalTestCase

class StudentRegistrationTest(unittest.TestCase, FunctionalTestCase):
  """Test GSoC Student Registration Process.
  """

  def setUp(self):
    FunctionalTestCase.__init__(self)
    self.setup()
    self.getParameters("./syed/soc/tests/functional/testdata_melange.xls", \
                                                                "GSOC_Student")

  def testForTryingToRegisterAsAStudent(self):
    #Test url, Change it according to your environment.
    self.Browser.get(self.obj_id['Url'])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

    #Check if "How Google Summer of Code Works" is present on home page.
    self.assertText("How Google Summer of Code Works")
  
    #Scroll down.
    self.Browser.execute_script("window.scrollTo(0, \
                                                  document.body.scrollHeight);")
  
    #Click on Register.
    self.clickOn(id=None, xpath=True, click_element="Register_Button")
  
    #For local environment. Clear the field, enter email and click on login.
    self.wait(3) 
    self.loginOnLocalhost()

    #For melange app on appengine.
    #self.wait(3) 
    #self.loginByGoogleAccount()

    #Wait for the page load completely, then fill the user name field.
    self.waitAndEnterText(5, id=None, xpath=True, element="User_name")
    
    #Fill the public name field.
    self.writeTextField(id=True, xpath=None, element="Public_name")
    self.Browser.execute_script("window.scrollTo(0, \
                                                  document.body.scrollHeight);")

    #Fill IM network field.
    self.writeTextField(id=True, xpath=None, element="Im_network")

    #Fill IM handle field.
    self.writeTextField(id=True, xpath=None, element="Im_handle")
  
    #Enter a valid home page address.
    self.writeTextField(id=True, xpath=None, element="Home_page_url")
  
    #Enter a valid blog address.
    self.writeTextField(id=True, xpath=None, element="Blog_url")
  
    #Enter photo url.
    self.writeTextField(id=True, xpath=None, element="Thumbnail_photo_url")

    #Enter Given Name.
    self.writeTextField(id=True, xpath=None, element="First_name")

    #Enter Surname.
    self.writeTextField(id=True, xpath=None, element="Last_name")

    #Enter Email.
    self.writeTextField(id=True, xpath=None, element="Email")

    #Enter Residential Street Address.
    self.writeTextField(id=True, xpath=None, element="Residential_street")

    #Enter Extra Residential Address.
    self.writeTextField(id=True, xpath=None, element="Residential_street_extra")

    #Enter the City.
    self.writeTextField(id=True, xpath=None, element="City")

    #Enter State.
    self.writeTextField(id=True, xpath=None, element="State")

    #Traverse through all the country names and select a country from the list.
    self.setDropDownList("Country")
    self.wait(2)

    #Enter Postal code.
    self.writeTextField(id=None, xpath=True, element="Postal_code")    

    #Enter phone number.
    self.writeTextField(id=None, xpath=True, element="Phone")
    
    #Select publish location.
    self.toggleCheckBox(id=None, xpath=True, chk_box="Publish_my_location")

    #Enter Full recipient name. 
    self.writeTextField(id=None, xpath=True, element="Full_recipient_name")

    #Enter Shipping Street Address.
    self.writeTextField(id=None, xpath=True, element="Shipping_street")

    #Enter Extra Shipping Street Address.
    self.writeTextField(id=None, xpath=True, element="Shipping_street_extra")

    #Enter the city name for shipment.
    self.writeTextField(id=None, xpath=True, element="Shipping_city")

    #Enter State.
    self.writeTextField(id=None, xpath=True, element="Shipping_state")
  
    #Traverse through all the country names and select a country From the List.
    self.setDropDownList("Shipping_country")    

    #Enter postal code.
    self.writeTextField(id=None, xpath=True, element="Shipping_postal_code")

    #Enter the date of birth.
    self.writeTextField(id=None, xpath=True, element="Birth_date")
  
    #Traverse through the list and select T-shirt Style.
    self.setDropDownList("T_shirt_style")    

    #Traverse through the list and select a T-shirt size.
    self.setDropDownList("T_shirt_size")

    #Select Gender as female.
    self.setDropDownList("Gender")

    #Fill the text area.
    self.writeTextField(id=None, xpath=True, element="How_did_you_hear_about_gsoc")

    #Unset the check box for Notification to new comments.
    self.toggleCheckBox(id=None, xpath=True, chk_box="Notify_to_new_public_comments")
 
    #Enter School Name.
    self.writeTextField(id=None, xpath=True, element="School_name")   

    #Select School Country.
    self.setDropDownList("School_country")
  
    #Enter Major Subject.
    self.writeTextField(id=None, xpath=True, element="Major_subject")
  
    #Select Degree.
    self.setDropDownList("Degree")
  
    #Enter Expected Graduation.
    self.writeTextField(id=None, xpath=True, element="Expected_graduation")
  
    #Enter School Homepage URL.
    self.writeTextField(id=None, xpath=True, element="School_homepage")
 
    #Submit.
    self.clickOn(id=None, xpath=True, click_element="Submit_button")

    #Check if data saved successfully.
    self.checkRegistrationSuccess("Message_from_melange")
    
  def tearDown(self):
    self.teardown()

if __name__=="__main__":
  unittest.main()
