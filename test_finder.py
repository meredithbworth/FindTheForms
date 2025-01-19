from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.irs.gov/prior-year-forms-and-instructions"

driver = webdriver.Chrome()

driver.get(url)

rows = driver.find_elements("name", "tr")
print(rows)
for row in rows:
    product_number = row.find_element.get_text('td', 'class',
                                               'views-field views-field-natural-sort-field views-field-prior-year-products-picklist-number')
    title = row.find_element.get_text('td', 'class',
                                      'views-field views-field-prior-year-products-picklist-title')
    revision_year = row.find_element.get_text('td', 'class',
                                              'views-field views-field-prior-year-products-picklist-revision-date')

    print(product_number)
