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

"""Base module for writing functional test scripts.
"""

import random
import string
import time
import sys
import unittest

from selenium import webdriver
from selenium.common import exceptions

import xlrd

class FunctionalTestCase(unittest.TestCase):  
  """ Base Class for all the Melange Functional Tests.
      Contains actions which will be used in writing Test scripts.
  """
  def init(self):
    self.obj_id = {}
    self.obj_val = {}

  def getParameters(self, name_of_workbook, name_of_sheet):
    """ Read the test data from excel sheets.

    Args:
      name_of_workbook: Workbook from which the test data will be imported.
      name_of_sheet: Particular sheet whose contents will be imported.
    """
    try:
      workbook = xlrd.open_workbook(name_of_workbook)              
    except IOError:
      self.teardown()
      sys.exit("Workbook \"%s\" not found" % name_of_workbook)
    #Get a sheet by name.
    sheet = workbook.sheet_by_name(name_of_sheet)                        
    #Pulling all the element values from spreadsheet.
    for x in range(1, sheet.nrows):
      for y in range(0,1):
        obj = sheet.cell_value(x,y)
        id = sheet.cell_value(x,y+1)
        value = sheet.cell_value(x,y+2)
        self.obj_id[obj] = id
        self.obj_val[obj] = value

  def wait(self, sec):
    """ Delay the execution of script for specified number of seconds.

    Args:
      sec: Number of seconds for which the script should wait.
    """
    time.sleep(sec)

  def writeTextField(self, id_type=None, element=None):
    """ Write text field in a form.

    Args:
      id_type: Type of identification used to uniquely identify an element.
      element: Particular text field which will be written.
    """    
    web_element=self.obj_id[element]
    value=self.obj_val[element]
    if id_type == "id":
      self.Browser.find_element_by_id(web_element).send_keys(value)
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(web_element).send_keys(value)
    else:
      raise KeyError 

  def toggleCheckBox(self, id_type=None, chk_box=None):
    """ Toggle a check box.

    Args:
      id_type: Type of identification used to uniquely identify an element.
      chk_box: particular check box which will be selected/not selected.
    """
    if id_type == "id":
      self.Browser.find_element_by_id(self.obj_id[chk_box]).click()
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(self.obj_id[chk_box]).click()
    else:
      raise KeyError

  def setDropDownList(self, select_opt=None):
    """ Selects one option from the drop down list.

    Args:
      select_opt: The option which should be selected from the drop down list.       
    """
    selection = self.Browser.find_element_by_xpath(self.obj_id[select_opt])
    all_options = selection.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == self.obj_val[select_opt]):
        option.click()
    
  def waitAndEnterText(self, sec, id_type=None, element=None):
    """ Wait and enter text in a particular field.

    Args:
      sec: Number of seconds script should wait.
      id_type: Type of identification used to uniquely identify an element.
      element: The field in which we we want to enter some text.      
    """
    web_element=self.obj_id[element]
    value=self.obj_val[element]
    self.wait(sec)
    if id_type == "id":
      self.Browser.find_element_by_id(web_element).send_keys(value)
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(web_element).send_keys(value)
    else:
      raise KeyError   

  def clearFieldAssertMessageEnterData(self, error_element=None, element=None):
    """Assert the error message , clear the input field and enter a new value.

    Args:
      error_element: It is the element which is showing error message.
      element: The correct value for the input field.                 
    """
    self.assertTextIn(error_element)
    self.clearField("xpath", element)
    self.writeTextField("xpath", element)
 
  def clearField(self, id_type=None, clear_element=None):
    """ Wait and clear a particular field.

    Args:
      clear_element: The field which we want to clear.
      id_type: Type of identification used to uniquely identify an element.
    """
    if id_type == "id":
      self.Browser.find_element_by_id(self.obj_id[clear_element]).clear()
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(self.obj_id[clear_element]).clear()
    else:
      raise KeyError   
 
  def clickOn(self, id_type=None, click_element=None):
    """ Click on the specified element.

    Args:
      click_element: The element which will be clicked.
      id_type: Type of identification used to uniquely identify an element.
    """
    if id_type == "id":
      self.Browser.find_element_by_id(self.obj_id[click_element]).click()
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(self.obj_id[click_element]).click()
    else:
      raise KeyError

  def assertError(self, msg):
    """Print the message and raise assertion error.

    Args:
      msg: The message which should be printed.  
    """
    raise AssertionError(msg)

  def assertLink(self, link_text=None):
    """Assert if a link is there.

    Args:
      link_text: The link which will be tested.  
    """
    try:
      self.Browser.find_element_by_link_text(link_text)      
    except exceptions.NoSuchElementException:
      msg = "The text %s is not part of a Link" % link_text
      self.assertError(msg)

  def assertText(self, text_element=None):
    """Assert a particular text.

    Args:
      text_element: The text which will be checked. 
    """
    txt = self.Browser.find_element_by_xpath(self.obj_id[text_element]).text
    text_value = self.obj_val[text_element]
    if txt is None:
        msg = "Element %s has no text %s " % (text_element, txt)
        self.assertError(msg)
    if txt != self.obj_val[text_element]:
        msg = "Element text should be %s. It is %s."% (text_value, txt)
        self.assertError(msg)

  def assertMessageAndEnterText(self, error_element=None, input_field=None):
    """Assert a message and enter value in the text field.

    Args:
      error_element : error message from the application which will be checked.
      input_field : input box in which a value will be entered.
    """
    self.assertText(error_element)
    self.writeTextField("xpath", input_field)

  def assertTextIn(self, text_element):
    """check for the contents present in a text message.

    Args:
      text_element : the message content which will be checked with the
                     message from the application.      
    """
    text_object = self.obj_id[text_element]
    text_value = self.obj_val[text_element]
    text_msg = self.Browser.find_element_by_xpath(text_object).text
    if text_msg is None:
        msg = "Element %s has no text %s " % (text_element, text_msg)
        self.assertError(msg)
    if text_msg not in text_value:
        msg = "Element text should be %s. It is %s." % (text_value, text_msg)
        self.assertError(msg)
    if text_msg in self.obj_val[text_element]:
      return True

  def isElementDisplayed(self, sec, element_displayed=None):
    """ Wait and check if a particular element is displayed.

    Args:
      sec: Number of seconds script should wait.
      element_displayed: A particular element which we want to check if it is 
      displayed.Return True if it is present else return false. if it is not 
      displayed just pass and continue the execution.
    """   
    self.wait(sec)
    display_element = self.obj_id[element_displayed]
    try:
      if self.Browser.find_element_by_xpath(display_element).is_displayed():
        return True        
    except exceptions.NoSuchElementException:
      msg = "The element %s is not displayed" % display_element
      self.assertError(msg)
      

  def fillRandomValue(self, element=None):
    """ It takes a value , add random string at the end and fill it in the form.

    Args:
      element: The element whose value will be changed by adding a random string 
               at the end.
    """
    N=5
    val = self.obj_val[element] + ''.join(random.choice(string.ascii_lowercase\
                                             + string.digits) for x in range(N))
    self.wait(1)
    self.clearField("xpath", element)
    self.Browser.find_element_by_xpath(self.obj_id[element]).send_keys(val)

  def waitAndClick(self, sec=None, id_type=None, click_element=None):
    """ wait and click on a particular element.

    Args:
      sec: Number of seconds script should wait.
      id_type: Type of identification used to uniquely identify an element.
      click_element: The element which we want to click.
    """    
    self.wait(sec)
    if id_type == "id":
      self.Browser.find_element_by_id(self.obj_id[click_element]).click()
    elif id_type == "xpath":
      self.Browser.find_element_by_xpath(self.obj_id[click_element]).click()
    else:
      raise KeyError

  def checkRegistrationSuccess(self, flash_message=None):
    """Check Message from the melange if student data is saved successfully.

    Args:
      flash_message: This is the web element which gets displayed and show
                     message if data is saved successfully.
    """
    if self.isElementDisplayed(5, flash_message) is True:
      text = self.Browser.find_element_by_xpath(self.obj_id[flash_message]).text
      if text == self.obj_val[flash_message]:  
        self.assertError(text)
      if text == "Data saved successfully.":
        pass
    
  def takeScreenshot(self, path=None):
    """Take screenshot.
    """
    self.Browser.save_screenshot(path)

  def scrollDown(self):
    """Sroll Down.
    """
    self.Browser.execute_script("window.\
                                 scrollTo(0, document.body.scrollHeight);")

  def setup(self):
    """Create a Browser Instance.
    """    
    self.Data_source = "./tests/functional/testdata_melange.xls"
    self.screenshot_dir = "./tests/functional/Melange.png"
    self.Browser = webdriver.Firefox()

  def teardown(self):
    """Take a screenshot and close the browser.
    """
    self.wait(2)
    self.takeScreenshot(self.screenshot_dir)
    self.Browser.close()

  def loginOnLocalhost(self):
    """ Logs in to the melange on localhost.
    """
    self.clearField("xpath", "Login_email_localhost")
    self.writeTextField("xpath", "Login_email_localhost")
    self.clickOn("xpath", "Sign_in_button_localhost")

  def loginByGoogleAccount(self):
    """ Logs in to the melange using Google Account.
    """
    self.wait(30)
    self.clearField("xpath", "Google_account")
    self.writeTextField("xpath", "Google_account")
    self.wait(2)
    self.writeTextField("xpath", "Password_for_google_account")
    self.wait(2)    
    self.clickOn("xpath", "Sign_in")

