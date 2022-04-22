from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
import time

class SBClass:
    def method(self):
              #driver = webdriver.Chrome(executable_path="C:\\Users\\PAVAN\\Downloads\\chromedriver_win32\\chromedriver.exe")
              driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
              driver.get("https://www.google.com")
              driver.maximize_window()
              time.sleep(4)

# home page
              driver.get("http://127.0.0.1:5000")
              time.sleep(4)




# login page
              driver.get("http://127.0.0.1:5000/loginForm")
              time.sleep(4)
              element = driver.find_element(By.NAME, "email")
              element.send_keys("rakeshc@gmail.com")
              time.sleep(4)
              element = driver.find_element(By.NAME, "password")
              element.send_keys("abc")
              element = driver.find_element(By.NAME, "password").submit()
              time.sleep(4)


# shop by categories
              driver.get("http://127.0.0.1:5000/displayCategory?categoryId=2")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[2]/table[1]/tbody/tr[2]/td[2]/a/img").click()
              time.sleep(4)



# selecting items
              driver.get("http://127.0.0.1:5000/")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[2]/div/ul/li[2]/a").click()
              time.sleep(4)

# remove cart
              driver.get("http://127.0.0.1:5000/cart")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/a").click()
              time.sleep(4)

# proceed to checkout
              driver.get("http://127.0.0.1:5000/cart")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/a").click()
              time.sleep(4)



# home page
              driver.get("http://127.0.0.1:5000")
              time.sleep(4)

# add to cart
              driver.get("http://127.0.0.1:5000/productDescription?productId=22")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[2]/div[4]/a/button").click()
              time.sleep(4)

# view cart
              driver.get("http://127.0.0.1:5000")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/a").click()
              time.sleep(4)
              
              '''# add to cart error
              driver.get("http://127.0.0.1:5000/cart")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/a").click()
              time.sleep(4)'''



#Registration
              driver.get("http://127.0.0.1:5000/registerationForm")
              time.sleep(4)
              element = driver.find_element(By.NAME, "email")
              element.send_keys("rakesh@gmail.com")
              time.sleep(4)
              element = driver.find_element(By.NAME, "password")
              element.send_keys("abc")
              time.sleep(4)
              element = driver.find_element(By.NAME, "cpassword")
              element.send_keys("abc")
              time.sleep(4)
              element = driver.find_element(By.NAME, "firstName")
              element.send_keys("Rakesh")
              time.sleep(4)
              element = driver.find_element(By.NAME, "lastName")
              element.send_keys("C")
              time.sleep(4)
              element = driver.find_element(By.NAME, "address1")
              element.send_keys("Indra nagar")
              time.sleep(4)
              element = driver.find_element(By.NAME, "address2")
              element.send_keys("Bengaluru")
              time.sleep(4)
              element = driver.find_element(By.NAME, "zipcode")
              element.send_keys("560038")
              time.sleep(4)
              element = driver.find_element(By.NAME, "city")
              element.send_keys("Bengaluru")
              time.sleep(4)
              element = driver.find_element(By.NAME, "state")
              element.send_keys("Karnataka")
              time.sleep(4)
              element = driver.find_element(By.NAME, "country")
              element.send_keys("India")
              time.sleep(4)
              element = driver.find_element(By.NAME, "phone")
              element.send_keys("9945743882")
              time.sleep(4)
              element = driver.find_element(By.NAME, "phone").submit()
              time.sleep(4)



                         #Admin Page Testing


# home page to admi login page
              driver.get("http://127.0.0.1:5000")
              time.sleep(4)
              driver.find_element(By.ID, "admin").click()
              time.sleep(4)



#admin login page
              driver.get("http://127.0.0.1:5000/Alogin?")
              time.sleep(4)
              element = driver.find_element(By.NAME, "aid")
              element.send_keys("admin")
              element = driver.find_element(By.NAME, "pass")
              element.send_keys("adminrock123")
              element = driver.find_element(By.NAME, "pass").submit()
              time.sleep(4)
              

#admin logout
              driver.get("http://127.0.0.1:5000/cart")
              time.sleep(4)
              driver.find_element(By.XPATH, "/html/body/a[4]").click()
              time.sleep(4)


                  #Seller page testing



#home page to seller page
              driver.get("http://127.0.0.1:5000/")
              time.sleep(4)
              driver.find_element(By.ID, "seller12").click()
              time.sleep(4)


dm=SBClass()
dm.method()