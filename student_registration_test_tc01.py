from melange_functional_actions import *

class Student_Registration_Test(unittest.TestCase, funcTests):

  def setUp(self):
    super(Student_Registration_Test, self).setUp()
    funcTest.get_parameters('/home/syed/Desktop/testdata_melange.xls')
    
  def test_for_trying_to_register_with_wrong_inputs(self):
 
    #Test Url, Change it according to your local dev environment
    Browser.get(objId['Url'])

    #Check for the correct browser title
    self.assertIn("Google Summer of Code", Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    funcTest.assert_text("How Google Summer of Code Works")
  
    #Scroll down
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register
    funcTest.wait_and_click(3, 'Register_Button')
    
    funcTest.wait(2)
  
    #Test env asks for email id, clear the field, enter email and click on login
    funcTest.login()

    #Wait for the page load completely, then fill the user name field
    funcTest.wait_and_enter_text(5, 'Username')
    
    #Fill the public name field  
    funcTest.write_text_field("id", "Public_name")
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Fill IM network field
    funcTest.write_text_field("id", "Im_network")

    #Fill IM handle field
    funcTest.write_text_field("id", "Im_handle")
  
    #Enter a valid home page address
    funcTest.write_text_field("id", "Home_page_url")
  
    #Enter a valid blog address
    funcTest.write_text_field("id", "Blog_url")
  
    #Enter photo url
    funcTest.write_text_field("id", "Thumbnail_photo_url")

    #Enter Given Name
    funcTest.write_text_field("id", "First_name")

    #Enter Surname
    funcTest.write_text_field("id", "Last_name")

    #Enter Email
    funcTest.write_text_field("id", "Email")

    #Enter Resedential Street Adress
    funcTest.write_text_field("id", "Res_street")

    #Enter Extra Residential Adress
    funcTest.write_text_field("id", "Res_street_extra")

    #Enter the City
    funcTest.write_text_field("id", "City")

    #Enter State
    funcTest.write_text_field("id", "State")

    #Traverse through all the country names and select India From the List
    funcTest.set_dropdown_list("Country")
    funcTest.wait(2)

    #Enter Postal code
    funcTest.write_text_field("xpath", "Postal_code")
    

    #Enter phone nuumber
    #funcTest.write_text_field("xpath", "Phone")
    Browser.find_element_by_id("phone").send_keys("987654321")

    #Select publish location
    funcTest.toggle_checkbox("Publish_my_location")

    #Enter Full recipient name  
    funcTest.write_text_field("xpath", "Full_recepient_name")

    #Enter Shipping Street Adress
    funcTest.write_text_field("xpath", "Shipping_street")

    #Enter Extra Shipping Street Adress
    funcTest.write_text_field("xpath", "Shipping_street_extra")

    #Enter the city name for shipment
    funcTest.write_text_field("xpath", "Shipping_city")

    #Enter State
    funcTest.write_text_field("xpath", "Shipping_state")
  
    #Traverse through all the country names and select a country From the List
    funcTest.set_dropdown_list("Shipping_country")    

    #Enter postal code
    funcTest.write_text_field("xpath", "Shipping_postal_code")

    #Enter the date of birth
    funcTest.write_text_field("xpath", "Birth_date")
  
    #Traverse through the list and select T-shirt Style
    funcTest.set_dropdown_list("T_shirt_style")    

    #Traverse through the list and select T-shirt size "XL"
    funcTest.set_dropdown_list("T_shirt_size")

    #Select Gender as male   
    Browser.find_element_by_xpath("//*[@id='gender']").send_keys(Keys.DOWN)
    Browser.find_element_by_xpath("//*[@id='gender']").send_keys(Keys.RETURN)

    #Fill the text area
    funcTest.write_text_field("xpath", "How_did_you_hear_about_gsoc")

    #Set the checkbox for Notification to new comments
    funcTest.toggle_checkbox("Notify_to_new_public_comments")
 
    #Enter School Name
    funcTest.write_text_field("xpath", "School_name") 
  

    #Select School Country
    funcTest.set_dropdown_list("School_country")
  
    #Enter Major Subject
    funcTest.write_text_field("xpath", "Major_subject")
  
    #Select Degree
    funcTest.set_dropdown_list("Degree")
  
    #Enter Expected Graduation  
    funcTest.write_text_field("xpath", "Expected_graduation")
  
    #Enter School Homepage URL
    funcTest.write_text_field("xpath", "School_homepage")
 
    #Submit
    funcTest.click_on("Submit_button")
    


  def tearDown(self):
    funcTest.tearDown()

if __name__ == "__main__":
  unittest.main()

