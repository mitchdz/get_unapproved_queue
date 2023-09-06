#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import argparse

def get_unapproved_queue():
    parser = argparse.ArgumentParser(description="Command-line argument example")
    parser.add_argument("--series", help="Specify the series argument", required=True)
    args = parser.parse_args()
    
    series=args.series
    
    # URL unapproved queue
    url = f"https://launchpad.net/ubuntu/{series}/+queue?queue_state=1&queue_text="

    # Send an HTTP GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")
    
        # Find all the td elements with the specified style
        td_elements = soup.find_all("td", style="padding-top: 5px")
    
        # Initialize an empty list to store the package names
        package_names = []
    
        # Iterate over the td elements to find the ones with a div with a specific id
        for td in td_elements:
            div_with_id = td.find("div", id=True)  # Find div with any id attribute
            if div_with_id:
                package_name = div_with_id.text.strip()
                package_names.append(package_name)
    
        # Print the list of package names that meet the criteria
        for index, package in enumerate(package_names, start=1):
            print(f"{index}. {package}")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")


if __name__ == "__main__":
    get_unapproved_queue()
