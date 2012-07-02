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

import logging
import random
import string
import time

from selenium import webdriver
from selenium.common import exceptions

import xlrd

class FunctionalTestCase(object):  
  """ Base Class for all the Melange Functional Tests.
      Contains actions which will be used in writing Test scripts.
  """
  def __init__(self):
    self.obj_id = {}
    self.obj_val = {}
  
  def getParameters(self, name_of_workbook, name_of_sheet):
    """ Read the test data from excel sheets.

    Args:
      name_of_workbook: Workbook from which the test data will be imported.
      name_of_sheet: Particular sheet whose contents will be imported.
    """
    log = logging.getLogger("melange_functional_actions")
    log.setLevel(logging.DEBUG)
    logging.basicConfig()
    try:
      workbook = xlrd.open_workbook(name_of_workbook)
    except IOError as e:
      log.debug("Workbook %s not found" % (name_of_workbook)) 
      raise e               
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
    print "waiting for page to load for %s seconds " % sec
    time.sleep(sec)

  def writeTextField(self, id=None, xpath=None, element=None):
    """ Write text field in a form.

    Args:
      id: id of the text field. If identification is done using text field id.
      xapth: xpath of text field. if identification is done using xpath.
      element: Particular text field in which a value will be written.
    """
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[element]).send_keys(\
                                                      self.obj_val[element])
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.\
                           obj_id[element]).send_keys(self.obj_val[element])
    else:
      raise KeyError 

  def toggleCheckBox(self, id=None, xpath=None, chk_box=""):
    """ Toggle a check box.

    Args:
      id: id of check box. If identification is done using check box id.
      xapth: xpath of check box. if identification is done using xpath.
      chk_box: particular check box which will be selected/not selected.
    """
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[chk_box]).click()
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.obj_id[chk_box]).click()
    else:
      raise KeyError

  def setDropDownList(self, select_opt=None):
    """ Selects one option from the drop down list.

    Args:
      select_opt: The option which should be selected from the drop down list.       
    """
    selection = self.Browser.find_element_by_xpath\
                                                  (self.obj_id[select_opt])
    all_options = selection.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == self.obj_val[select_opt]):
        option.click()
    
  def waitAndEnterText(self, sec, id=None, xpath=None, element=None):
    """ Wait and enter text in a particular field.

    Args:
      sec: Number of seconds script should wait.
      id: id of element. If identification is done using element id.
      xapth: xpath of element. if identification is done using xpath.
      element: The field in which we we want to enter some text.      
    """
    self.wait(sec)
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[element]).send_keys\
                                                        (self.obj_val[element])
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.obj_id[element]).send_keys\
                                                        (self.obj_val[element])
    else:
      raise KeyError   

  def clearFieldAssertMessageAndEnterData(self, error_element , element=""):
    """Assert the error message , clear the input field and enter a new value.

    Args:
      erro_element: It is the element which is showing error message.
      element: The correct value for the input field.                 
    """
    self.assertTextIn(error_element)
    self.clearField(id=None, xpath=True, clear_element=element)
    self.writeTextField(id=None, xpath=True, textfield=element)
 
  def clearField(self, id=None, xpath=None, clear_element=""):
    """ Wait and clear a particular field.

    Args:
      clear_element: The field which we want to clear.
      id: id of element. If identification is done using element id.
      xapth: xpath of element. if identification is done using xpath.
    """
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[clear_element]).clear()
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.obj_id[clear_element]).clear()
    else:
      raise KeyError   
 
  def clickOn(self, id=None, xpath=None, click_element=""):
    """ Click on the specified element.

    Args:
      click_element: The element which will be clicked.
      id: id of element. If identification is done using element id.
      xapth: xpath of element. if identification is done using xpath.
    """
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[click_element]).click()
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.obj_id[click_element]).click()
    else:
      raise KeyError

  def assertError(self, msg):
    """Print the message and raise assertion error.

    Args:
      msg: The message which should be printed.  
    """
    raise AssertionError(msg)

  def assertLink(self, link_text=""):
    """Assert if a link is there.

    Args:
      link_text: The link which will be tested.  
    """
    try:
      self.Browser.find_element_by_link_text(link_text)      
    except exceptions.NoSuchElementException:
      msg = "The text %s is not part of a Link" % link_text
      self.assertError(msg)

  def assertText(self, text_element=""):
    """Assert a particular text.

    Args:
      text_element: The text which will be checked. 
    """
    txt = self.Browser.find_element_by_xpath(self.obj_id[text_element]).text
    if txt is None:
        msg = "Element %s has no text %s " % (text_element, txt)
        self.assertError(msg)
    if txt != self.obj_val[text_element]:
        msg = "Element text should be %s. It is %s."\
                                            % (self.obj_val[text_element], txt)
        self.assertError(msg)

  def assertMessageAndEnterText(self, error_element="", input_field=""):
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
    text_msg = self.Browser.find_element_by_xpath(\
                                               self.obj_id[text_element]).text
    if text_msg is None:
        msg = "Element %s has no text %s " % (text_element, text_msg)
        self.assertError(msg)
    if text_msg not in self.obj_val[text_element]:
        msg = "Element text should be %s.  It is %s." % (self.obj_val[\
                                                        text_element], text_msg)
        self.assertError(msg)
    if text_msg in self.obj_val[text_element]:
      return True

  def isElementDisplayed(self, sec, element_displayed=""):
    """ Wait and check if a particular element is displayed.

    Args:
      sec: Number of seconds script should wait.
      element_displayed: A particular element which we want to check if it is 
      displayed. Return True if it is present else return false. If it is not 
      displayed just pass and continue the execution.
    """   
    self.wait(sec)
    try:
      if self.Browser.find_element_by_xpath\
                                (self.obj_id[element_displayed]).is_displayed():
        return True
    except:
      return False
      pass

  def fillRandomValue(self, element=""):
    """ It takes a value , add random string at the end and fill it in the form.

    Args:
      element: The element whose value will be changed by adding a random string 
               at the end.
    """
    N=5
    val = self.obj_val[element] + ''.join(random.choice(string.ascii_lowercase\
                                             + string.digits) for x in range(N))
    self.wait(1)
    self.clearField(id=None, xpath=True, clear_element=element)
    self.Browser.find_element_by_xpath(self.obj_id[element]).send_keys(val)

  def waitAndClick(self, sec,id=None, xpath=None, click_element=""):
    """ wait and click on a particular element.

    Args:
      sec: Number of seconds script should wait.
      id: id of element. If identification is done using element id.
      xapth: xpath of element. if identification is done using xpath.
      click_element: The element which we want to click.
    """    
    self.wait(sec)
    if id is not None:
      self.Browser.find_element_by_id(self.obj_id[click_element]).click()
    elif xpath is not None:
      self.Browser.find_element_by_xpath(self.obj_id[click_element]).click()
    else:
      raise KeyError

  def checkRegistrationSuccess(self, flash_message=""):
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
    
  def takeScreenshot(self, path=""):
    """Take screenshot.
    """
    self.Browser.save_screenshot(path)

  def setup(self):
    """Create a Browser Instance.
       Populate test configuration details.
    """
    self.Browser = webdriver.Firefox()

  def teardown(self):
    """Take a screenshot and close the browser.
    """
    self.wait(2)
    self.takeScreenshot("./tests/functional/Melange.png")
    self.Browser.close()

  def loginOnLocalhost(self):
    """ Logs in to the melange on localhost.
    """
    self.clearField(id=None, xpath=True, clear_element="Login_email_localhost")
    self.writeTextField(id=None, xpath=True, element="Login_email_localhost")
    self.clickOn(id=None, xpath=True, click_element="Sign_in_button_localhost")

  def loginByGoogleAccount(self):
    """ Logs in to the melange using Google Account.
    """
    self.wait(30)
    self.clearField(id=None, xpath=True, clear_element="Google_account")
    self.writeTextField(id=None, xpath=True, element="Google_account")
    self.wait(2)
    self.writeTextField(id=None, xpath=True, \
                                          element="Password_for_google_account")
    self.wait(2)    
    self.clickOn(id=None, xpath=True, click_element="Sign_in")
