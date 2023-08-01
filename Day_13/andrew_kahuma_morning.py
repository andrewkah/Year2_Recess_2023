# Introdction to Web scraping with BeautifulSoup
""" 
- Extracting information from a website by using BeautifulSoup and parsing the HTML and XML code of the webpages.

# Installation of BeautifulSoup
- pip install beautifulsoup4

# Import Libraries
- from bs4 import BeautifulSoup
- import requests  ====== fetches the HTML content


"""

from bs4 import BeautifulSoup
import requests
import csv
import json
url = 'https://xeno-canto.org'
response = requests.get(url)

# Get Title of the website
soup = BeautifulSoup(response.content, 'html.parser')
title = soup.find('title')
print(title)

# Assignment
# Extract all bird species from this website url; https://xeno-canto.org and generate
# the csv file or the JSON file format for the bird species, family and more.

# Extract all bird songs from this website url; https://xeno-canto.org and use this API 
# to get data. the endpoint for the website is at https://xeno-canto.org/api/2/recordings

# Extract bird songs
def bird_species():
    url = 'https://xeno-canto.org/api/2/recordings'
    response = requests.get(url)
    # Bird Species with duplicates
    if response.status_code == 200:
        data = response.json()
        if "recordings" in data:
            species_list = [recording["sp"] for recording in data["recordings"]]
            print(species_list)
    else:
        print("Error: Unable to fetch data.")
        
    # Bird Species With no Duplicates. 
    if response.status_code == 200:
        data1 = response.json()
        if "recordings" in data1:
            species_list = list({recording["sp"] for recording in data1["recordings"]})
            print(species_list)
    else:
        print("Error: Unable to fetch data.")  

    # Bird species without duplicates into a CSV file
    if response.status_code == 200:
        data2 = response.json()
        if "recordings" in data2:
            species_list = list({recording["sp"] for recording in data2["recordings"]})

            # Specify the file path for the CSV file
            csv_file_path = "species.csv"

            # Write the species_list to the CSV file
            with open(csv_file_path, "w", newline="", encoding="utf-8") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(["Species"])  # Write header row
                writer.writerows([[species] for species in species_list])  # Write species names row by row

            print("Data saved to CSV file successfully.")
    else:
        print("Error: Unable to fetch data.")
        
bird_species()
    
def bird_songs():
    # Getting the audio list and species.
    audio_list = []

    species_list = []
    for i in range(10):
        request_result = requests.get(url.format(str(i)))
        soup = BeautifulSoup(request_result.text, "html.parser")
        links = soup.find_all("audio")
        for link in links:
            audio_list.append("https:" + link.attrs["src"])
        names = soup.find_all("span", class_="common-name")
        for name in names:
            speciesData = name.find("a")
            species_list.append(
                {"species": speciesData.text, "species_link": speciesData.attrs["href"]}
            )

    # Dumping them into a json file.
    with open("bird_songs.json", "+a") as file:
        json.dump({"bird_songs": audio_list, "bird_species": species_list}, file)
        
bird_songs()

# Using the api query parameters(0).
result1 = requests.get("https://xeno-canto.org/api/2/recordings?query=troglodytes+troglodytes")

# Prints values from the API in json format
print(result1.json())