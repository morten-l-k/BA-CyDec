#Sort list of IP addresses into country origin
import requests
import sys
import json
import time
from collections import defaultdict

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print(f"Usage: python3 {sys.argv[0]} <ip_list_file>")
    sys.exit(1)

input_file = sys.argv[1] 

ips = []
try:
    with open(input_file) as f:
        ips = json.load(f)
except FileNotFoundError:
    print(f"File not found: {input_file}")
    sys.exit(1)

grouped = defaultdict(list)

def fill_countries(ips:list):
    number = 0
    for ip in ips:
        time.sleep(1.34)
        print(f"Trying IP: {ip}, number: {number}")
        number += 1
        try:
            response = requests.get(f"http://ip-api.com/json/{ip}", timeout=5)
            response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

            # Check if the response is empty
            if response.text:
                r = response.json()  # Parse the JSON response
                country = r.get("country", "Unknown")
                # Specify in json object what data to extract
                extract_data = {
                    'ip': ip,
                    'country': country,
                    'lat': r.get("lat", "Unknown"),
                    'lon': r.get("lon", "Unknown")
                }
                print(f"COUNTRY IS: {country}")
                grouped[country].append(extract_data)
            else:
                print(f"Received an empty response for IP: {ip}")
                grouped["Unknown"].append({'ip': ip, 'country': 'Unknown'})

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred for IP {ip}: {http_err}")  # e.g., 404 Not Found
            grouped["Unknown"].append({'ip': ip, 'country': 'Unknown'})
        except requests.exceptions.RequestException as req_err:
            print(f"Request error occurred for IP {ip}: {req_err}")  # Other request-related errors
            grouped["Unknown"].append({'ip': ip, 'country': 'Unknown'})
        except ValueError as json_err:
            print(f"JSON decode error for IP {ip}: {json_err}")  # JSON decoding errors
            grouped["Unknown"].append({'ip': ip, 'country': 'Unknown'})

fill_countries(ips)
   
#Intialize variables to be used for handling false data in "Unknown"
previous_length = 0
counter = 3

#Handling of data points mistakenly categorized as "Unknown". When the "Unknown" category is not decreased in size, there will be no more
#to find.
while(len(grouped["Unknown"]) > 0):
    if((previous_length == len(grouped["Unknown"])) and counter == 0):
        break
    if((previous_length == len(grouped["Unknown"]))):
        counter -= 1
        print("COUNTER IS: ", counter)
    previous_length = len(grouped["Unknown"])

    print("Length of unknown list is: ", len(grouped["Unknown"]))
    
    #Make list of ips as strings in unknown
    unknown_ip_list = [entry['ip'] for entry in grouped["Unknown"]]
    
    print("unknown_ip_list is:", unknown_ip_list)
    #Remove all ocurrences in "unknowns" category
    del grouped["Unknown"]

    #Call fill_countries on the unknown_ip_list to fill entries again
    fill_countries(unknown_ip_list)


#Print all data
print(grouped)

with open('ips-countries.json','w') as f_countries:
    json.dump(dict(grouped),f_countries,indent=4)
