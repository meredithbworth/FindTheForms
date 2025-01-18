# %%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os

# Python program to demonstrate
# selenium
"""driver = webdriver.Firefox()
driver.get("https://www.irs.gov/prior-year-forms-and-instructions"
           )"""

# %%
desired_form = input("Which form are you looking for? \n")

# change spaces to + for url
sanitized_desired_form = desired_form.replace(" ", "+")

print("Looking for " + desired_form + " \n")

# %%
# Declare the url you want to scrape
URL = "https://www.irs.gov/prior-year-forms-and-instructions" + \
    sanitized_desired_form + "&isDescending=false"

# Request the raw HTML data from URL and store it in a variable
page = requests.get(URL)


# Use BeautifulSoup to parse the page content and store it in a variable
soup = BeautifulSoup(page.content, 'html.parser')
# print(soup)
# Find all useful table rows by searching for their even/odd class
results = soup.find_all(True, {'class': [0]})

print("HTML data retrieved \n")

# %%
# Declare an empty array of the future cleaned results
clean_results = []

# Declare empty strings for form number and title so they can be used later
found_form_number = ""
found_form_title = ""

# Iterate over the soup results
for row in results:
    # Find and assign desired data in the HTML
    found_form_number = row.find(
        'td',
        class_="views-field views-field-prior-year-products-picklist-title", headers_="view-prior-year-products-picklist-title-table-column")
    html_form_link = row.find('a', href=True)
    html_form_title = row.find(
        'td', class_='views-field-prior-year-products-picklist-title')
    html_form_year = row.find(
        'td', class_='views-field-prior-year-products-picklist-revision-date')
# Format the HTML data into useable text
row_form_number = html_form_number.text()
row_form_link = html_form_link['href']
row_form_title = html_form_title.get_text()
row_form_year = html_form_year.get_text(
)
# If the form number matches the found form
if row_form_number == desired_form:
    # Append each row as a dictionary to the cleaned results array
    clean_results.append({"form_number": row_form_number, "form_link": row_form_link,
                          "form_title": row_form_title, "form_year": int(row_form_year)})

    # Assign the title and form number to be used later
    found_form_number = row_form_number
    found_form_title = row_form_title

print("Results cleaned \n")

# Confirm if found form is being appended to the clean_results list/array

"""if len(clean_results) > 0:
    print(clean_results[0])
else:
    print("The list is empty.")"""

# %%
# If the URL has isDescending set to false than the first item will be the max year
#   and the last item will be the min year
if len(clean_results) > 0:
    print(clean_results[0])
else:
    print("The list is empty.")

try:
    max_form_year = clean_results[0]["form_year"]
except IndexError as ex:
    print("Index of form out of range.")
    # print(ex)
    # print(type(ex))

try:
    min_form_year = clean_results[len(clean_results)-1]["form_year"]
except IndexError as ex:
    print("Index of form out of range.")
    # print(ex)
    # print(type(ex))

# Initialize an empty array to hold the final output
desired_format = []
# Append desired data in desired order
desired_format.append({"form_number": found_form_number, "form_title": found_form_title,
                      "min_year": min_form_year, "max_year": max_form_year})

print("Forms found: \n", json.dumps(desired_format), '\n')
