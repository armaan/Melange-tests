#!/usr/bin/env python

from melange_functional_actions import *

class StudentRegistrationTest(unittest.TestCase, FunctionalTests):

  def setUp(self):
    super(StudentRegistrationTest, self).setUp()
    functest.getParameters('/home/syed/Desktop/testdata_melange.xls', 'TC03')
    
  def testForTryingToRegisterWithEmptyFields(self):
 
    Browser = self.Browser
    #Test Url, Change it according to your local dev environment
    Browser.get(functest.obj_id['Url'])

    #Check for the correct browser title
    self.assertIn("Google Summer of Code", Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    functest.assertText("How Google Summer of Code Works")
  
    #Scroll down
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register
    functest.waitAndClick(3, 'Register_Button')
     
    #Test env asks for email id, clear the field, enter email and click on login
    functest.login()

    #Submit
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    functest.clickOn("Submit_button")

    #Assert message "This field is required" and enter a user name.
    functest.assertMessageAndEnterText("Username_required", "Username")

    #Assert message "This field is required" and enter a public name.
    functest.assertMessageAndEnterText("Public_name_required", "Public_name")

    #Assert message "This field is required" and enter a First Name.
    functest.assertMessageAndEnterText("First_name_required","First_name")

    #Assert message "This field is required" and enter a Last Name.
    functest.assertMessageAndEnterText("Last_name_required", "Last_name")

    #Assert message "This field is required" and enter an email address.
    functest.assertMessageAndEnterText("Email_required", "Email")

    #Assert message "This field is required" and enter a street address.
    functest.assertMessageAndEnterText("Street_address_required", "Res_street")

    #Assert message "This field is required" and enter a city
    functest.assertMessageAndEnterText("City_required", "City")

    #Assert message "This field is required" and enter a country.
    functest.assertTextIn("Country_required")
    functest.setDropDownList("Country")

    #Assert message "This field is required" and enter a postal code.
    functest.assertMessageAndEnterText("Postal_code_required", "Postal_code")

    #Assert message "This field is required" and enter a phone number.
    functest.assertMessageAndEnterText("Phone_number_required", "Phone")

    #Assert message "This field is required" and enter a date of birth"
    functest.assertMessageAndEnterText("Birth_date_required", "Birth_date")

    #Assert message "This field is required" and enter a school name
    functest.assertMessageAndEnterText("School_name_required", "School_name")

    #Assert message "This field is required" and enter the school country
    functest.assertTextIn("School_country_required")
    functest.setDropDownList("School_country")

    #Assert message "This field is required" and enter expected graduation year.
    functest.assertMessageAndEnterText("Expected_graduation_required", "Expected_graduation")

    #Assert message "This field is required" and enter school hom page url.
    functest.assertMessageAndEnterText("School_homepage_required", "School_homepage")

    #Submit
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    functest.clickOn("Submit_button")

    """ Check if a student has already registered with this user name.
        if true change the user name and submit the form again.
    """
    if functest.waitAndCheckIfDisplayed(5, "Already_registered") is True:
      functest.fillRandomValue("Username")
      functest.clickOn("Submit_button") 


  def tearDown(self):
    functest.tearDown()

if __name__ == "__main__":
  unittest.main()
