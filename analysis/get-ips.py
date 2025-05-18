#File for extracting unique IP addresses occuring in json log file
from collections import Counter
import re
import json

log_file = "combined.json" #File to be read from

with open(log_file, "r", encoding="utf-8", errors="ignore") as f:
    content = f.read()

#.findall() returns ALL occurences. Duplicates are included multiple times. Returns: list of strings 
ips = re.findall(r'(\d{1,3}(?:\.\d{1,3}){3})', content)

#Counter returns an object with key value pairs. Counts how many times each value occurs.
ip_count = Counter(ips)

with open('unique-ips.json','w',encoding='utf-8',errors='ignore') as ip_u:
    json.dump(list(set(ips)),ip_u)

with open('ips-occurences.json','w',encoding="utf-8", errors="ignore") as ip_f:
    json.dump(ip_count,ip_f)
