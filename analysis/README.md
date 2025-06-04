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

### 3) Create geographic map visualizing IP address origin
Change the path in ```mapping.py```to the path containing ```ips-countries.json```

Run the following command:

    python3 mapping.py

which shows a geographic map for country origin of all IP addresses.

# Data analysis of commands

```divide-inputs.py``` can separate lines in a json file based on their length. Used for separating the commands run in the honeypot in longer and shorter commands. Change path for ```extracted-input.json``` in ```divide-inputs.py``` to path for the file. Requirement for ```extracted-input.py``` is that it needs to only include on each line the key-value pair for the {"input":"[COMMAND]"}:

    {"input": "echo Hi | cat -n"} 
