# Data analysis for BA-CyDec

Change ```log_file``` variable in ```get-ips.py``` to path of file to be analysed. **Notice**: only .json format allowed.

### 1) Get unique IP addresses and number of occurences
Run the following command:
  
    python3 get-ips.py

which produces two files: ```unique-ips.json``` and ```ips-occurences.json```

### 2) Map IP addresses to country origins
Run the following command:
  
    python3 map-ips.py unique-ips.json

which produces ```ips-countries.json``` that contains ```"Country":[{IP1},{IP2},...,{IPN}]'```, where the value for each country name is a list containing all IP addresses mapped to that specific country.
