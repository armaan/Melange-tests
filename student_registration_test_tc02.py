#!/usr/bin/env python
from melange_functional_actions import *

class StudentRegistrationTest(unittest.TestCase, FunctionalTests):

  def setUp(self):
    super(StudentRegistrationTest, self).setUp()
    functest.getParameters('/home/syed/Desktop/testdata_melange.xls', 'TC02')
    
  def testForTryingToRegisterWithWrongInputs(self):
 
    #Test Url, Change it according to your local dev environment
    Browser.get(objId['Url'])

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

    #Wait for the page load completely, then fill the user name field
    functest.waitAndEnterText(5, 'Username')
    
    #Fill the public name field  
    functest.writeTextField("id", "Public_name")
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

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
    functest.toggleCheckBox("Publish_my_location")

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

    #Traverse through the list and select T-shirt size "XL"
    functest.setDropDownList("T_shirt_size")

    #Select Gender as female   
    functest.setDropDownList("Gender")

    #Fill the text area
    functest.writeTextField("xpath", "How_did_you_hear_about_gsoc")

    #Set the checkbox for Notification to new comments
    functest.toggleCheckBox("Notify_to_new_public_comments")
 
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
    functest.clickOn("Submit_button")
    functest.wait(5)
    
    #Clear invalid user name, assert error message and enter a valid user name.
    functest.clearFieldAndEnterData("Wrong_username", "Correct_username")

    #Clear invalid Home Page url, assert error message and enter a valid url.
    functest.clearFieldAndEnterData("Invalid_home_url", "Valid_home_url")

    #Clear invalid blog url, assert error message and enter valid blog url. 
    functest.clearFieldAndEnterData("Invalid_blog_url", "Valid_blog_url")

    #Clear invalid photo url, assert error message and enter a valid photo url.
    functest.clearFieldAndEnterData("Invalid_photo_url", "Valid_photo_url")

    #Clear invalid First Name, assert error message and enter a valid name.
    functest.clearFieldAndEnterData("Invalid_given_name", "Valid_given_name")

    #Clear invalid Last name, assert error message and enter a valid last name.
    functest.clearFieldAndEnterData("Invalid_surname", "Valid_surname")

    #Clear invalid email, assert error message and enter a valid email address.
    functest.clearFieldAndEnterData("Invalid_email", "Valid_email")

    """Clear invalid residential address, assert error message and enter a valid 
       residential address.
    """
    functest.clearFieldAndEnterData("Invalid_residential_address",\
                                         "Valid_residential_address")
    """Clear invalid extra street address, assert error message and enter a 
       valid extra street address.
    """
    functest.clearFieldAndEnterData("Invalid_extra_street_address",\
                                        "Valid_extra_street_address")
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Clear invalid city name, assert error message and enter a valid city name.
    functest.clearFieldAndEnterData("City_name_is_required", "Valid_city_name")

    #Clear invalid state name,assert error message and enter a valid state name.
    functest.clearFieldAndEnterData("Invalid_state_name", "Valid_state_name")

    #Clear invalid postal code, assert error message and enter a valid code.
    functest.clearFieldAndEnterData("Invalid_postal_code", "Valid_postal_code")

    #Clear invalid phone contact, assert error message and enter a valid number.
    functest.clearFieldAndEnterData("Invalid_phone", "Valid_phone")

    """Clear invalid shipping street address, assert error message and enter a 
    valid last name.
    """
    functest.clearFieldAndEnterData("Invalid_shipping_street", \
                                             "Valid_shipping_street")

    """Clear invalid extra shipping street address, assert error message and
       enter a valid extra shipping street address. 
    """
    functest.clearFieldAndEnterData("Invalid_extra_shipping_address",\
                                         "Valid_extra_shipping_address")

    """Clear invalid city name, assert error message and enter a valid 
       city name for shipment."""
    functest.clearFieldAndEnterData("Invalid_shipment_city",\
                                          "Valid_shipment_city")

    """Clear invalid state name, assert error message and enter a valid 
       state name for shipment."""
    functest.clearFieldAndEnterData("Invalid_shipment_state",\
                                          "Valid_shipment_state")

    """Clear invalid postal code, assert error message and enter a valid 
       postal code."""
    functest.clearFieldAndEnterData("Invalid_shipment_postal_code",\
                                           "Valid_shipment_postal_code")

    """Clear invalid date of birth, assert error message and enter a valid 
       date of birth.
    """
    functest.clearFieldAndEnterData("Invalid_date_of_birth",\
                                           "Valid_date_of_birth")

    """Clear invalid graduation year, assert error message and enter a valid 
       graduation year.
    """
    functest.clearFieldAndEnterData("Invalid_graduation_year",\
                                          "Valid_graduation_year")

    """Clear invalid school home page url, assert error message and enter a 
       valid graduation year.
    """
    functest.clearFieldAndEnterData("Invalid_school_homepage_url",\
                                           "Valid_school_homepage_url")

    #Submit
    functest.clickOn("Submit_button")
    functest.wait(5)
    
    if functest.waitAndCheckIfDisplayed(5, "Already_registered") is True:
      functest.fillRandomValue("Correct_username")
      functest.clickOn("Submit_button") 

  def tearDown(self):
    functest.tearDown()

if __name__ == "__main__":
  unittest.main()
