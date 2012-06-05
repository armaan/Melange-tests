#!/usr/bin/env python2.5
#
# Copyright 2010 the Melange authors.
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
import unittest2 as unittest

from selenium.common.exceptions import InvalidElementStateException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchAttributeException
from selenium.common.exceptions import NoSuchWindowException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

import xlrd

class FunctionalTests(object):  
  """ Base Class for all the Melange Functional Tests.
      Contains actions which will be used in writing Test scripts.
  """
    
  obj_id = {}
  obj_val = {}
  Browser = webdriver.Firefox()
  
  def getParameters(self, name_of_workbook, sheet_name):
    """ Read the test data from excel sheets.

    Args:
      name_of_workbook: workbook from which the test data will be imported.
      sheetname: particular sheet whose contents will be imported.
    """

    try:
      workbook = xlrd.open_workbook(name_of_workbook)
    except IOError as e:
      print "Workbook with name %s not found" %name_of_workbook
      functest.tearDown()
      raise e          
    #Get a sheet by name.
    sheet = workbook.sheet_by_name(sheet_name)                        
    #Pulling all the element values from spreadsheet.
    for x in range(1, sheet.nrows):
      for y in range(0,1):
        obj = sheet.cell_value(x,y)
        Id = sheet.cell_value(x,y+1)
        value = sheet.cell_value(x,y+2)
        functest.obj_id[obj] = Id
        functest.obj_val[obj] = value
    return

  def wait(self, sec):
    """ Delay the execution of script for specified number of seconds.

    Args:
      sec: Number of seconds for which the script should wait.
    """

    print "waiting for page to load for %s seconds " % sec
    time.sleep(sec)
    return

  def writeTextField(self, id_type="", element=""):
    """ Write text field in a form.

    Args:
      id_type: Type of identification used to uniquely identify an element.
      element: Particular text field which will be written.
    """
    if id_type == "id":
      functest.Browser.find_element_by_id(functest.obj_id[element]).send_keys(\
                                                      functest.obj_val[element])
    elif id_type == "xpath":
      functest.Browser.find_element_by_xpath(functest.\
                           obj_id[element]).send_keys(functest.obj_val[element])
    else:
      print "Error"
    return 

  def toggleCheckBox(self, chk_box=""):
    """ Toggle a check box.

    Args:
      chk_box: particular check box which will be selected/not selected.
    """
    functest.Browser.find_element_by_xpath(functest.obj_id[chk_box]).click()

  def setDropDownList(self, select_opt=""):
    """ Selects one option from the drop down list.

    Args:
      select_opt: The option which should be selected from the drop down list.       
    """
    selection = functest.Browser.find_element_by_xpath\
                                                  (functest.obj_id[select_opt])
    all_options = selection.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == functest.obj_val[select_opt]):
        option.click()
    return

  def waitAndCheckIfDisplayed(self, sec, elem_displayed=""):
    """ Wait and check if a particular element is displayed.

    Args:
      sec: Number of seconds script should wait.
      elem_displayed: The element which we want to check if it displayed or not.
    """
    while True:
      try:
        functest.wait(sec)
        functest.Browser.find_element_by_xpath\
                                (functest.obj_id[elem_displayed]).is_displayed()
        return True     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem_displayed
        break
    return
    

  def clearFieldAndEnterData(self, error_elem , elem=""):
    """Assert the error message , clear the input field and enter a new value.

    Args:
      erro_elem: It is the element which is showing error message.
      elem: The correct value for the input field.
                 
    """
    functest.assertTextIn(error_elem)
    functest.waitAndClearField(1, elem)
    functest.writeTextField("xpath", elem)
    return

  def waitAndClick(self, sec, elem_click=""):
    """ Wait and click on a particular element.

    Args:
      sec: Number of seconds script should wait.
      elem_click: The element which we want to click.
    """
    while True:
      try:
        functest.wait(sec)
        functest.Browser.find_element_by_xpath\
                                          (functest.obj_id[elem_click]).click()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem_click
        break
    return

  def waitAndEnterText(self, sec, elem=""):
    """ Wait and enter text in a particular field.

    Args:
      sec: Number of seconds script should wait.
      elem: The field in which we we want to enter some text.
    """
    while True:
      try:
        functest.wait(sec)
        functest.Browser.find_element_by_xpath(functest.obj_id[elem]).send_keys\
                                                        (functest.obj_val[elem])     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break
    return


  def waitAndClearField(self, sec, clear_elem=""):
    """ Wait and clear a particular field.

    Args:
      sec: Number of seconds script should wait.
      clear_elem: The field which we want to clear.
    """
    while True:
      try:
        functest.wait(sec)
        functest.Browser.find_element_by_xpath\
                                           (functest.obj_id[clear_elem]).clear()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %clear_elem
        break
    return  
 
  def clickOn(self, click_elem=""):
    """ Click on the specified element.

    Args:
      click_elem: The element which will be clicked.
    """
    functest.Browser.find_element_by_xpath(functest.obj_id[click_elem]).click()

  def assertError(self, msg):
    """Print the message and raise assertion error.

    Args:
      msg: The message which should be printed.  
    """
    print msg
    raise AssertionError(msg)
    return

  def assertLink(self, link_text=""):
    """Assert if a link is there.

    Args:
      link_text: The link which will be tested.  
    """
    try:
      link = functest.Browser.find_element_by_link_text(link_text)      
    except NoSuchElementException as e :
      msg = "The text %s is not part of a Link" %link_text
      functest.assertError(msg)
    return link

  def assertText(self, text_elem=""):
    """Assert a particular text.

    Args:
      text_elem: The text which will be checked. 
    """
    txt = functest.Browser.find_element_by_xpath(functest.obj_id[text_elem]).text
    if txt is None:
        msg = "Element %s has no text %s " % (text_elem, txt)
        functest.assertError(msg)
    if txt != functest.obj_val[text_elem]:
        msg = "Element text should be %s.  It is %s."\
                                            % (functest.obj_val[text_elem], txt)
        functest.assertError(msg)
    return

  def assertMessageAndEnterText(self, error_elem="", input_field=""):
    """Assert a message and enter value in the text field.

    Args:
      error_elem : the error message from the application which will be checked.
      input_field : input box in which a value will be entered.
    """
    functest.assertText(error_elem)
    functest.writeTextField("xpath", input_field)
    return

  def assertTextIn(self, text_elem):
    """check for the contents present in a text message.

    Args:
      text_elem : the message content which will be checked with the
                  message from the application.      
    """
    error_msg = functest.Browser.find_element_by_xpath(\
                                               functest.obj_id[text_elem]).text
    if error_msg is None:
        msg = "Element %s has no text %s " % (text_elem, error_msg)
        functest.assertError(msg)
    if error_msg not in functest.obj_val[text_elem]:
        msg = "Element text should be %s.  It is %s." % (functest.obj_val[\
                                                         text_elem], error_msg)
        functest.assertError(msg)
    return    

  def fillRandomValue(self, elem=""):
    """ It takes a value , add random string at the end and fill it in the form.

    Args:
      elem: The element whose value will be changed by adding a random string at
      the end.
    """
    N=5
    val = functest.obj_val[elem] + ''.join(random.choice(string.ascii_lowercase\
                                             + string.digits) for x in range(N))
    functest.waitAndClearField(1, elem)
    functest.Browser.find_element_by_xpath(functest.obj_id[elem]).send_keys(val)
    return

  def takeScreenshot(self):
    """Take screenshot.
    """
    functest.Browser.save_screenshot("Melange.png")
  
  def setUp(self):
    self.Browser = webdriver.Firefox()

  def tearDown(self):
    """Take a screenshot and close the browser.
    """
    functest.wait(2)
    functest.takeScreenshot()
    functest.Browser.close()

  def login(self):
    """ Logs in to the melange.
    """
    functest.waitAndClearField(5, "Login_email")
    functest.writeTextField("xpath", "Login_email")
    functest.clickOn("Sign_in_button")
    
functest = FunctionalTests()

