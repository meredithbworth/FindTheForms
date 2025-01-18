import requests
from bs4 import BeautifulSoup
import json
import os

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
