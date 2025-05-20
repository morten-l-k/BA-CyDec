#File for extracting unique IP addresses occuring in json log file
from collections import Counter
import re
import json

log_file = "combined.json" #File to be read from

#Open log_file
with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

#Find occurences of IPv4 and IPv6 addresses using Regular Expression
pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b|\b(?:[A-Fa-f0-9]{1,4}:){2,7}[A-Fa-f0-9]{1,4}\b'
ips = re.findall(pattern, content)

#Counter returns an object with key value pairs - counts how many times each value occurs.
ip_count = Counter(ips)

#Save unique-ips.json containing all unique IP-addresses
with open('unique-ips.json','w',encoding='utf-8',errors='ignore') as ip_u:
    json.dump(list(set(ips)),ip_u)

#Save ips-occurences.json containing number of times each IP-address occurs in combined.json
with open('ips-occurences.json','w',encoding="utf-8", errors="ignore") as ip_f:
    json.dump(ip_count,ip_f)
