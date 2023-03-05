#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;password=bobbycool;date_of_birth=03/04/1993;"]

for messages in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
