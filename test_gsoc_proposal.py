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

from selenium.webdriver.common.keys import Keys

from melange_functional_actions import FunctionalTestCase

class GSoCProposal(FunctionalTestCase):
  """ This test case checks the functionality 
      of GSoC Proposal Page.
  """
  def setUp(self):
    self.init()
    self.setup()    
     
  def testGSoCProposal(self):
    #Load test data.
    self.getParameters(self.Data_source, "GSoC_Proposal")
    
    #Test Url, Change it according to your local dev environment.
    self.Browser.get(self.obj_id["Url"])

    #Check for the correct browser title.
    self.assertIn("Google Summer of Code", self.Browser.title)

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

    #Click on participating orgs.
    self.wait(5)
    self.Browser.get(self.obj_id["Url"])
    self.wait(5)
    self.clickOn("xpath", "Participating_orgs")

    #Select an org.
    self.wait(3)
    self.clickOn("xpath", "Select_org")

    #Submit a proposal.
    self.wait(3)
    self.scrollDown()
    self.wait(3)
    self.Browser.find_element_by_link_text("Submit proposal").click()

    #Enter a project title.
    self.wait(3)
    self.writeTextField("xpath", "Project_title")

    #Enter short description.
    self.wait(3)
    self.writeTextField("xpath", "Project_short_description")

    self.Browser.switch_to_frame("melange-content-textarea_ifr")

    #Write Proposal Description.
    self.wait(3)
    self.writeTextField("xpath", "Content")

    #Select All.
    self.wait(3)
    content="//*[@id='tinymce']"
    self.Browser.find_element_by_xpath(content).send_keys(Keys.CONTROL, 'a')
    self.scrollDown()

    #Make the proposal contents bold.
    self.Browser.switch_to_default_content()
    self.wait(3)
    self.clickOn("xpath", "Content_bold")

    #Enter additional info.
    self.writeTextField("xpath", "Additional_info")
     
    #Make the proposal contents italic.
    self.wait(3)
    self.clickOn("xpath", "Content_italic")

    #Underline the text.
    self.wait(3)
    self.clickOn("xpath", "Content_underline")

    #Select font family.
    self.wait(3)
    self.clickOn("id", "Content_font")
    self.wait(3)
    self.clickOn("xpath", "Content_font_family")

    #Select format.
    self.wait(3)
    self.clickOn("id", "Content_format")
    self.wait(3)
    self.clickOn("xpath", "Content_format_type")

    #Select font size.
    self.wait(3)
    self.clickOn("id", "Content_font_size_type")
    self.wait(3)
    self.clickOn("xpath", "Content_font_size")

    #Select content color.
    self.wait(3)
    self.clickOn("id", "Content_text_color")
    self.wait(3)
    self.clickOn("xpath", "Content_color")

    #Align Right.
    self.wait(3)
    self.clickOn("xpath", "Content_align_right")

    #Align Center.
    self.wait(3)
    self.clickOn("xpath", "Content_align_center")

    #Align Left.
    self.wait(3)
    self.clickOn("xpath", "Content_align_left")

    #bulleted list.
    self.wait(3)
    self.clickOn("xpath", "Content_insert_remove_bullet_list")

    #Numbered bulleted list.
    self.wait(3)
    self.clickOn("xpath", "Content_insert_remove__numbered_bullet_list")

    #Increase indent.
    self.wait(3)
    self.clickOn("xpath", "Content_increase_indent")

    #Decrease indent.
    self.wait(3)
    self.clickOn("xpath", "Content_decrease_indent")

    #Strike through the text.
    self.wait(3)
    self.clickOn("xpath", "Content_strikethrough")

    #Insert horizontal rule.
    self.wait(3)
    self.clickOn("xpath", "Content_insert_horizontal_rule")

    #Publicly visible.
    self.wait(3)
    self.toggleCheckBox("xpath", "Publicly_visible")

    #Submit the proposal.
    self.wait(3)
    self.clickOn("xpath", "Submit_a_proposal")
    
    #Comment on proposal.
    self.wait(3)
    self.Browser.switch_to_frame("melange-content-textarea_ifr")
    self.writeTextField("xpath", "Comment")
    self.Browser.switch_to_default_content()

    #Submit comment.
    self.scrollDown()
    self.wait(3)
    self.clickOn("xpath", "Submit_comment")

  def tearDown(self):
    self.teardown()
