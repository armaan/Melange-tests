#To check all the functionality provided by Registeration page. we fill the
#various input fields with wrong values as well as leave blank some mandatory
#fields, It will generate various error messages, On submitting the form, we see
#a message " Sorry, we could not save your data. Please fix the errors mentioned
#below." and various error messages on the input fields. In the function #Test_error_messages_and_register_with_correct_inputs(), we check various error
#messages and enter correct values to successfully submit our registration form.

import unittest
import random
import string

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class Student_Registration_Test(unittest.TestCase):

  def setUp(self):
    self.Browser = webdriver.Firefox()
 

  def test_for_trying_to_register_with_wrong_inputs(self):

    Browser = self.Browser

    #Test Url, Change it according to your local dev environment
    Browser.get("http://localhost:8080/gsoc/homepage/google/gsoc2009")

    #Check for the correct browser title
    self.assertIn("Google Summer of Code", Browser.title)

    #Check if "How Google Summer of Code Works" is present.
    self.assertIn("How Google Summer of Code Works", \
    Browser.find_element_by_xpath("//*[@id='title-section-how-it-works']").text)
  
    #Scroll down
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
  
    #Click on Register
    WebDriverWait(Browser, timeout=3).until(lambda x:\
     x.find_element_by_xpath("//*[@id='block-apply-text-action']/a[2]")).click()
  
	
    #Test env asks for email id, clear the field, enter email and click on login
    self.login()

    #Wait for the page load completely, then fill the user name field
    try:
      WebDriverWait(Browser, timeout=3).until(lambda x1:\
          x1.find_element_by_xpath("//*[@id='link_id']")).send_keys("user@")
    except TimeoutException :
      print " A user is already registered with this mail id"
      while (Browser.find_element_by_xpath\
          ("//*[@id='form_row_public_name']/label").is_displayed()):
        Browser.back()
        self.login()
        
    #Assert if "Register as a student message" is present
    self.assertIn("Register as a Student",\
        Browser.find_element_by_xpath("//*[@id='form-register-title']").text)
  
    #Fill the public name field  
    Browser.find_element_by_id("public_name").send_keys("user@")
    Browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    #Fill IM network field
    Browser.find_element_by_id("im_network").send_keys("irc")

    #Fill IM handle field
    Browser.find_element_by_id("im_handle").send_keys("exampleHandle")
  
    #Enter a valid blog address
    Browser.find_element_by_id("blog").send_keys("sk")
  
    #Enter photo url
    Browser.find_element_by_id("photo_url").send_keys("kj")
    #Enter Given Name
    Browser.find_element_by_xpath("//*[@id='given_name']").send_keys("user@")
    #Enter Surname
    Browser.find_element_by_xpath("//*[@id='surname']").send_keys("user@")
    #Enter Email
    Browser.find_element_by_xpath("//*[@id='email']").send_keys("user")
    #Enter Resedential Street Adress
    Browser.find_element_by_xpath("//*[@id='res_street']").send_keys("user@")
    #Enter Extra Residential Adress
    Browser.find_element_by_xpath("//*[@id='res_street_extra']").send_keys("user@")
    #Enter the City
    Browser.find_element_by_xpath("//*[@id='res_city']").send_keys("")
    #Enter State
    Browser.find_element_by_xpath("//*[@id='res_state']").send_keys("user@")
  
    #Traverse through all the country names and select India From the List
    select = Browser.find_element_by_xpath("//*[@id='res_country']")
    all_options = select.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == "India"):
        option.click() 

    #Enter Postal code
    Browser.find_element_by_id("res_postalcode").send_keys("user@")
    #Enter phone nuumber
    Browser.find_element_by_id("phone").send_keys("user@")
    #Select publish location
    Browser.find_element_by_id("publish_location").click()
    #Enter Full recipient name  
    Browser.find_element_by_xpath("//*[@id='ship_name']").\
        send_keys("Example Recipient Name")
    #Enter Shipping Street Adress
    Browser.find_element_by_xpath("//*[@id='ship_street']").send_keys("user@")
    #Enter Extra Shipping Street Adress
    Browser.find_element_by_xpath("//*[@id='ship_street_extra']").send_keys("user@")
    #Enter the city name for shipment
    Browser.find_element_by_xpath("//*[@id='ship_city']").send_keys("user@")
    #Enter State
    Browser.find_element_by_xpath("//*[@id='ship_state']").send_keys("user@")
  
    #Traverse through all the country names and select India From the List
    select1 = Browser.find_element_by_xpath("//*[@id='ship_country']")
    all_options1 = select1.find_elements_by_tag_name("option")
    for option in all_options1:
      if (option.get_attribute("value") == "India"):
        option.click() 

    #Enter postal code
    Browser.find_element_by_xpath("//*[@id='ship_postalcode']").send_keys("user@")
    #Enter the date of birth
    Browser.find_element_by_xpath("//*[@id='birth_date']").send_keys("1990-09-08")
  
    #Traverse through the list and select T-shirt Style
    select2 = Browser.find_element_by_xpath("//*[@id='tshirt_style']")
    all_options2 = select2.find_elements_by_tag_name("option")
    for option in all_options2:
      if (option.get_attribute("value") == "male"):
        option.click() 

    #Traverse through the list and select T-shirt size "XL"
    select3 = Browser.find_element_by_xpath("//*[@id='tshirt_size']")
    all_options3 = select3.find_elements_by_tag_name("option")
    for option in all_options3:
      if (option.get_attribute("value") == "XL"):
        option.click()

    #Select Gender as male   
    Browser.find_element_by_xpath("//*[@id='gender']").send_keys(Keys.DOWN)
    Browser.find_element_by_xpath("//*[@id='gender']").send_keys(Keys.RETURN)
    #Fill the text area
    Browser.find_element_by_xpath\
        ("//*[@id='melange-program_knowledge-textarea']").send_keys("Friends")
    #Enter School Name
    Browser.find_element_by_xpath("//*[@id='school_name']")\
        .send_keys("Dronacharya College of Engineering")
  

    #Select School Country
    select4 = Browser.find_element_by_xpath("//*[@id='school_country']")
    all_options4 = select4.find_elements_by_tag_name("option")
    for option in all_options4:
      if (option.get_attribute("value") == "India"):
        option.click()
  
    #Enter Major Subject
    Browser.find_element_by_xpath("//*[@id='major']").send_keys("Computer Science")
  
    #Select Degree
    select5 = Browser.find_element_by_xpath("//*[@id='degree']")
    all_options5 = select5.find_elements_by_tag_name("option")
    for option in all_options5:
      if (option.get_attribute("value") == "Undergraduate"):
        option.click()
  
    #Enter Expected Graduation  
    Browser.find_element_by_xpath("//*[@id='expected_graduation']").send_keys("kl")
  
    #Enter School Homepage URL
    Browser.find_element_by_xpath("//*[@id='school_home_page']").send_keys("user@")  
    WebDriverWait(Browser, timeout=5)  
    #Submit
    Browser.find_element_by_xpath("//*[@id='form-register-submit']").click()
    self.Test_error_messages_and_register_with_correct_inputs()

  def Test_error_messages_and_register_with_correct_inputs(self):
    Browser = self.Browser  

    #Sorry, we could not save your data. Please fix the errors mentioned below.
    sorry_msg = WebDriverWait(Browser, timeout=5).until\
	(lambda x: x.find_element_by_xpath("//*[@id='flash-message']/p")).text
    self.assertIn("Sorry, we could not save your data", sorry_msg)

    #Check the error message , Clear username field and enter correct name.
    self.clear_field_and_enter_new_data("This link ID is in wrong format.",\
        "//*[@id='form_row_link_id']/div", "//*[@id='link_id']", "Lucy123")
  
    #Check the error message and Edit Blog URL
    self.clear_field_and_enter_new_data("Enter a valid URL.", "//*[@id=\
        'form_row_blog']/div", "//*[@id='blog']", "syedarmani.blogspot.com")

    #Check the error message and Edit photo URL
    self.clear_field_and_enter_new_data("Enter a valid URL.", "//*[@id=\
        'form_row_photo_url']/div", "//*[@id='photo_url']", "flickr.com/lucy")

    #Check the error message , Clear field and enter correct Given Name
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_given_name']/div", "//*[@id='given_name']", "Lucy")

    #Check the error message , Clear field and enter correct Surname
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_surname']/div", "//*[@id='surname']", "Miller")

    #Check the error message , Clear field and enter correct Email
    self.clear_field_and_enter_new_data("Enter a valid email", "//*[@id=\
        'form_row_email']/div", "//*[@id='email']", "lucy.miller@gmail.com")

    #Check the error message
    #Clear field and enter correct Residential Street Adress
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_res_street']/div", "//*[@id='res_street']", "abcd")

    #Check the error message
    #Clear field and enter correct Residential Street Adress
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
       'form_row_res_street_extra']/div", "//*[@id='res_street_extra']", "abcd")

    #Check the error message , Clear field and enter correct City
    self.clear_field_and_enter_new_data("This field is required.", "//*[@id=\
        'form_row_res_city']/div", "//*[@id='res_city']", "abcd")

    #Check the error message , Clear field and enter correct State
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_res_state']/div", "//*[@id='res_state']", "abcd")

    #Check the error message , Clear field and enter correct Postal code
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_res_postalcode']/div", "//*[@id='res_postalcode']", "246545")

    #Check the error message , Clear field and enter correct phone nuumber
    self.clear_field_and_enter_new_data("Only numerical characters", "//*[@id=\
        'form_row_phone']/div", "//*[@id='phone']", "987654321")

    #Check the error message , Clear field and enter correct Shipping Street Adress
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_ship_street']/div", "//*[@id='ship_street']", "abcd")

    #Check the error message 
    #Clear field and enter correct Extra Shipping Street Adress
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
       'form_row_ship_street_extra']/div", "//*[@id='ship_street_extra']", "abcd")

    #Check the error message , Clear field and enter correct city name for shipment
    self.clear_field_and_enter_new_data("Invalid characters", "//*\
        [@id='form_row_ship_city']/div", "//*[@id='ship_city']", "abcd")

    #Check the error message , Clear field and enter correct State
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_ship_state']/div", "//*[@id='ship_state']", "abcd")
	
    #Check the error message , Clear field and enter correct Shipping Postal Code
    self.clear_field_and_enter_new_data("Invalid characters", "//*[@id=\
        'form_row_ship_state']/div", "//*[@id='ship_postalcode']", "abcd")

    #Check the error message , Clear field and enter correct Expected Graduation  
    self.clear_field_and_enter_new_data("Enter a whole number.", "//*[@id=\
     'form_row_expected_graduation']/div","//*[@id='expected_graduation']","2012")
  
    #Check the error message , Clear field and enter correct School Homepage URL
    self.clear_field_and_enter_new_data("Enter a valid URL.", "//*[@id=\
	'form_row_school_home_page']/div", "//*[@id='school_home_page']", "www.abc.com")
    #Submit the form
    Browser.find_element_by_xpath("//*[@id='form-register-submit']").click()
	
    # There is already a user with this link id.
    if WebDriverWait(Browser, timeout=5).until(lambda x: \
        x.find_element_by_xpath("//*[@id='form_row_link_id']/div")).is_displayed():
      N=5
      username = "Lucy"+''.join(random.choice(string.ascii_lowercase\
                                             + string.digits) for x in range(N))
      Browser.find_element_by_xpath("//*[@id='link_id']").clear()
      Browser.find_element_by_xpath("//*[@id='link_id']").send_keys(username)
      Browser.find_element_by_xpath("//*[@id='form-register-submit']").click()
  
   
  def tearDown(self):
    self.Browser1.close()

  def login(self):
    N=6
    Browser = self.Browser
    id = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(N)) + "@gmail.com"
    WebDriverWait(Browser, timeout=10).until(lambda x: x.find_element_by_xpath("//*[@id='email']")).clear()
    Browser.find_element_by_xpath("//*[@id='email']").send_keys(id)
    Browser.find_element_by_xpath("//*[@id='submit-login']").click()

  def clear_field_and_enter_new_data(self, msg, path, fieldpath, value):
    Browser = self.Browser
    self.assertIn(msg, Browser.find_element_by_xpath(path).text)
    Browser.find_element_by_xpath(fieldpath).clear()
    Browser.find_element_by_xpath(fieldpath).send_keys(value)   

  
  def tearDown(self):
    self.Browser.close()

  
if __name__ == "__main__":
  unittest.main()

