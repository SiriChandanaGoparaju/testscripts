import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        driver = self.driver

        driver.get("http://sirichandanagoparaju.pythonanywhere.com/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul/li/a").click()
        time.sleep(1)
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        time.sleep(1)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        time.sleep(2)

        assert "logged in "
        data = open('product.csv')
        datareader = csv.reader(data)
        for row in datareader:
            if datareader.line_num == 1:
                continue
            else:
                cust_name = row[0]
                product= row[1]
                p_description = row[2]
                quantity = row[3]
                charge = row[4]


        # xpath, clicks on product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div[4]/div/div[2]/a").click()
        time.sleep(2)

        # xpath, clicks on add product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)

        #fillig out the service form
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys(cust_name)
        time.sleep(1)
        elem = driver.find_element_by_id("id_product")
        elem.send_keys(product)
        time.sleep(1)
        elem = driver.find_element_by_id("id_p_description")
        elem.send_keys(p_description)
        time.sleep(1)

        elem = driver.find_element_by_id("id_quantity")
        elem.send_keys(quantity)
        time.sleep(1)
        elem = driver.find_element_by_id("id_charge")
        elem.send_keys(charge)
        time.sleep(1)



        #xpath, clicks on save button for add service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(2)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()