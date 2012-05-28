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

class funcTests:
  
  
  def get_parameters(self, name_of_workbook):
    workbook = xlrd.open_workbook(name_of_workbook)
    #Get a sheet by name        
    sheet2 = workbook.sheet_by_name('Objects')                
    #Pulling all the Xpath values from spreadsheet
    for x in range(1,sheet2.nrows):
      for y in range(0,1):
        obj = sheet2.cell_value(x,y)
        Id = sheet2.cell_value(x,y+1)
        value = sheet2.cell_value(x,y+2)
        global objId
        global objVal
        objId[obj] = Id
        objVal[obj] = value

  def wait(self, sec):
    print "waiting for page to load for %s seconds " % sec
    time.sleep(sec)

  def clear_field_and_enter_new_data(self, msg, path, fieldpath, value):
    Browser = self.Browser
    self.assertIn(msg, Browser.find_element_by_xpath(path).text)
    Browser.find_element_by_xpath(fieldpath).clear()
    Browser.find_element_by_xpath(fieldpath).send_keys(value) 

  def write_text_field(self, t = "", element = ""):
    if t == "id":
      Browser.find_element_by_id(objId[element]).send_keys(objVal[element])
    elif t == "xpath":
      Browser.find_element_by_xpath(objId[element]).send_keys(objVal[element])
    else:
      print "Error"


  def toggle_checkbox(self, element = ""):
    Browser.find_element_by_xpath(objId[element]).click()

  def set_dropdown_list(self, element = ""):
    selection = Browser.find_element_by_xpath(objId[element])
    all_options = selection.find_elements_by_tag_name("option")
    for option in all_options:
      if (option.get_attribute("value") == objVal[element]):
        option.click()

  def wait_and_check_if_displayed(self, sec, elem = ''):
    while True:
      try:
        funcTest.wait(sec)
        Browser.find_element_by_xpath(objId[elem]).is_displayed()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break

  def wait_and_click(self, sec, elem = ''):
    while True:
      try:
        funcTest.wait(sec)
        Browser.find_element_by_xpath(objId[elem]).click()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break

  def wait_and_enter_text(self, sec, elem = ''):
    while True:
      try:
        funcTest.wait(sec)
        Browser.find_element_by_xpath(objId[elem]).send_keys(objVal[elem])     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break

  def wait_and_clear_field(self, sec, elem = ''):
    while True:
      try:
        funcTest.wait(sec)
        Browser.find_element_by_xpath(objId[elem]).clear()     
        break
      except NoSuchElementException as e:
        print " The element with id %s cannot be located" %elem
        break  
 
  def click_on(self, element = ""):
    Browser.find_element_by_xpath(objId[element]).click()

  def assert_error(self, msg):
    print msg
    raise AssertionError(msg)

  def assert_link(self, element = ""):
    try:
      link = Browser.find_element_by_link_text(element)      
    except NoSuchElementException as e :
      msg = "The text %s is not part of a Link" % element
      funcTest.assert_error(msg)
    return link

  def assert_text(self, elem = ""):
    txt = Browser.find_element_by_xpath(objId[elem]).text
    if txt is None:
        msg = "Element %s has no text %s " % (elem, txt)
        funcTest.assert_error(msg)
    if txt != elem:
        msg = "Element text should be %s.  It is %s." % (elem, txt)
        funcTest.assert_error(msg)
    return

  def take_screenshot(self):
    Browser.save_screenshot("Melange.png")
  
  def setUp(self):
    self.Browser = webdriver.Firefox()
    #Browser = self.Browser

  def tearDown(self):
    funcTest.take_screenshot()
    Browser.close()

  def login(self):
    funcTest.wait_and_clear_field(5, "Login_email")
    funcTest.write_text_field("xpath", "Login_email")
    funcTest.click_on("Sign_in_button")
    
funcTest = funcTests()

