import xlrd

import unittest2 as unittest
from unittest2 import SkipTest
import random
import string
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (
    NoSuchElementException, NoSuchAttributeException,
    InvalidElementStateException, WebDriverException,
    NoSuchWindowException, NoSuchFrameException, TimeoutException)

objId = {}
objVal = {}
Browser = webdriver.Firefox()

class FunctionalTests(object):  
  """Contains actions which will be used in writing Test scripts
  """

  def getParameters(self, name_of_workbook, sheetname):
    """Read Test data from excel sheets

    Args:
      name_of_workbook: workbook from which the test data will be imported.
      sheetname: particular sheet whose contents will be imported.
    """
    workbook = xlrd.open_workbook(name_of_workbook)
    #Get a sheet by name        
    sheet = workbook.sheet_by_name(sheetname)                
    #Pulling all the Xpath values from spreadsheet
    for x in range(1,sheet.nrows):
      for y in range(0,1):
        obj = sheet.cell_value(x,y)
        Id = sheet.cell_value(x,y+1)
        value = sheet.cell_value(x,y+2)
        global objId
        global objVal
        objId[obj] = Id
        objVal[obj] = value

  def wait(self, sec):
    """ delay the execution of script for specified number of seconds.

    Args:
      sec: Number of seconds for which the script should wait.
    """
    print "waiting for page to load for %s seconds " % sec
    time.sleep(sec)

  def clearFieldAndEnterNewData(self, msg, path, fieldpath, value):

    Browser = self.Browser
    self.assertIn(msg, Browser.find_element_by_xpath(path).text)
    Browser.find_element_by_xpath(fieldpath).clear()
    Browser.find_element_by_xpath(fieldpath).send_keys(value) 

  def writeTextField(self, id_type = "", element = ""):
    """Write text field in a form.

    Args:
      id_type: Type of identification used to uniquely identify an element.
      element: Particular text field which will be written.
    """
    if id_type == "id":
      Browser.find_element_by_id(objId[element]).send_keys(objVal[element])
    elif id_type == "xpath":
      Browser.find_element_by_xpath(objId[element]).send_keys(objVal[element])
    else:
      print "Error"

  def toggleCheckBox(self, chk_box = ""):
    """ Toggle a check box

    Args:
      chk_box: particular check box which will be selected/not selected.
    """
    Browser.find_element_by_xpath(objId[chk_box]).click()

  def setDropDownList(self, select_opt = ""):
    """ Selects one option from the drop down list.

    Args:
      select_opt: The option which should be selected from the drop down list.       
    """
    selection = Browser.find_element_by_xpath(objId[select_opt])
    all_options = selection.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == objVal[select_opt]):
        option.click()

  def waitAndCheckIfDisplayed(self, sec, elem_displayed = ""):
    """ wait and check if a particular element is displayed.

    Args:
      sec: Number of seconds script should wait.
      elem_displayed: The element which we want to check if it displayed or not.
    """
    while True:
      try:
        functest.wait(sec)
        Browser.find_element_by_xpath(objId[elem_displayed]).is_displayed()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem_displayed
        break

  def waitAndClick(self, sec, elem_click = ""):
    """ wait and click on a particular element.

    Args:
      sec: Number of seconds script should wait.
      elem_click: The element which we want to click.
    """
    while True:
      try:
        functest.wait(sec)
        Browser.find_element_by_xpath(objId[elem_click]).click()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem_click
        break

  def waitAndEnterText(self, sec, elem = ""):
    """ wait and enter text in a particular field.

    Args:
      sec: Number of seconds script should wait.
      elem: The field in which we we want to enter some text.
    """
    while True:
      try:
        functest.wait(sec)
        Browser.find_element_by_xpath(objId[elem]).send_keys(objVal[elem])     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break

  def waitAndClearField(self, sec, clear_elem = ""):
    """ wait and clear a particular field.

    Args:
      sec: Number of seconds script should wait.
      clear_elem: The field which we want to clear.
    """
    while True:
      try:
        functest.wait(sec)
        Browser.find_element_by_xpath(objId[clear_elem]).clear()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %clear_elem
        break  
 
  def clickOn(self, click_elem = ""):
    """ Click on the specified element.

    Args:
      click_elem: The element which will be clicked.
    """
    Browser.find_element_by_xpath(objId[click_elem]).click()

  def assertError(self, msg):
    """Print the message and raise assertion error."""
    print msg
    raise AssertionError(msg)

  def assertLink(self, link_text = ""):
    """Assert if a link is there.

    Args:
      link_text: The link which will be tested.  
    """
    try:
      link = Browser.find_element_by_link_text(link_text)      
    except NoSuchElementException as e :
      msg = "The text %s is not part of a Link" %link_text
      functest.assertError(msg)
    return link

  def assertText(self, text_elem = ""):
    """Assert a particular text.

    Args:
      text_elem: The text which will be checked. 
    """
    txt = Browser.find_element_by_xpath(objId[text_elem]).text
    if txt is None:
        msg = "Element %s has no text %s " % (text_elem, txt)
        functest.assertError(msg)
    if txt != text_elem:
        msg = "Element text should be %s.  It is %s." % (text_elem, txt)
        functest.assertError(msg)
    return

  def takeScreenshot(self):
    """Take screenshot"""
    Browser.save_screenshot("Melange.png")
  
  def setUp(self):
    self.Browser = webdriver.Firefox()

  def tearDown(self):
    functest.takeScreenshot()
    Browser.close()

  def login(self):
    """ Login to the melange """
    functest.waitAndClearField(5, "Login_email")
    functest.writeTextField("xpath", "Login_email")
    functest.clickOn("Sign_in_button")
    
functest = FunctionalTests()

