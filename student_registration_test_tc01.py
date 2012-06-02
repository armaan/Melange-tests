#!/usr/bin/env python
from melange_functional_actions import *

class StudentRegistrationTest(unittest.TestCase, FunctionalTests):

  def setUp(self):
    super(StudentRegistrationTest, self).setUp()
    functest.getParameters('/home/syed/Desktop/testdata_melange.xls', 'Objects')
    
  def testForTryingToRegisterAsAStudent(self):
 
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
    functest.wait(2)
  
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

    #Unset the checkbox for Notification to new comments
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
    

  def tearDown(self):
    functest.tearDown()

if __name__ == "__main__":
  unittest.main()

