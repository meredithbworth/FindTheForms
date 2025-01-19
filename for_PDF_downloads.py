# %%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import os
from find_the_form.py import *

# %%
# Get input for desired form year or years
desired_years = input(
    "If you want to download, please enter a 4 digit year xxxx or range of years xxxx-xxxx \n")
# Save the desired year or range of years to reference later
desired_year = 0
max_year = 0
min_year = 0
# Save the form url for downloading
form_url = " "

# If the input was only 4 digits then 1 year is desired
if len(desired_years) == 4:
    # Set the input as the desired year
    desired_year = desired_years
    print("Downloading " + desired_year + " " + found_form_number + "\n")

    # Iterate through the clean results
    for form in clean_results:

        # Check to see if the form year is the same as desired year
        if form['form_year'] == int(desired_year):

            # Set the form url from the cleaned data
            form_url = form['form_link']

            # Check if subdirectory with file name exists
            if not os.path.exists(desired_form):
                print("Creating subdirectory... \n")

                # Make a new directory with read write access
                os.mkdir(desired_form, mode=0o666)

                # Get the data from the url
                requested_download = requests.get(form_url, stream=True)

                # Change into the directory we want to save the data in
                os.chdir(f'{desired_form}')

                # Steam the data to be saved
                with open(f"{desired_form} - {desired_year}.pdf", 'wb') as f:
                    for chunk in requested_download.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                    f.close()

                print("Enjoy your download! \n")
                # Go up a level, useful if cell is ran multiple times
                os.chdir('..')

            # Else if the directory does exist
            elif os.path.exists(desired_form):

                # Change to the desired directory
                os.chdir(f'{desired_form}')

                # Get the data from the url
                requested_download = requests.get(form_url, stream=True)

                # Stream the data to be saved
                with open(f"{desired_form} - {desired_year}.pdf", 'wb') as f:
                    for chunk in requested_download.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

                    f.close()

                print("Enjoy your download! \n")

                # Go up a level, useful if cell is ran multiple times
                os.chdir('..')

# If the input was length 9, then a range of years is desired
elif len(desired_years) == 9:

    # Slice the input string for the max and min year
    max_year = desired_years[5:]
    min_year = desired_years[:4]
    print("Downloading " + found_form_number +
          " forms from " + min_year + " to " + max_year)

    # Create an empty array to store the download urls
    url_list = []

    # Iterate over the cleaned results
    for form in clean_results:

        # If the form year fall within the range of desired years
        if int(min_year) <= form['form_year'] <= int(max_year):

            # Append the url and form year to the url list
            url_list.append(
                {"form_link": form['form_link'], "form_year": form['form_year']})

    # Iterate over the urls
    for url in url_list:
        # If the directory does not exist
        if not os.path.exists(desired_form):
            print("Creating subdirectory... \n")

            # Create the subdirectory
            os.mkdir(desired_form, mode=0o666)

            # Get the data from the url
            requested_download = requests.get(url['form_link'], stream=True)

            # Navigate to the desired directory
            os.chdir(f'{desired_form}')

            # Stream and save the data
            with open(f"{desired_form} - {url['form_year']}.pdf", 'wb') as f:
                for chunk in requested_download.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                f.close()

            print(f"Downloading {url['form_year']} \n")

            # Go up a level
            os.chdir('..')

            print("Enjoy your downloads!")

        # If the directory does exist
        elif os.path.exists(desired_form):

            # Navigate to the directory
            os.chdir(f'{desired_form}')

            # Download the data
            requested_download = requests.get(url['form_link'], stream=True)

            # Steam and save the data
            with open(f"{desired_form} - {url['form_year']}.pdf", 'wb') as f:
                for chunk in requested_download.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)

                f.close()

            print(f"Downloading {url['form_year']} \n")

            # Go up a level
            os.chdir('..')

            print("Enjoy your downloads!")
# %%
