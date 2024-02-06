#!/usr/bin/python3
""" Contains script to load and save json"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


FILE = "add_item.json"

try:
    arr = load_from_json_file(FILE)
except Exception:
    arr = []

for _arg in sys.argv[1:]:
    arr.append(_arg)

save_to_json_file(arr, FILE)
