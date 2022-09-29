#!/usr/bin/env python3

import os
import json

# Create an empty dictionary
env = {}

# Iterate through environment variables and add them to env
for env_key, env_value in os.environ.items():
    env[env_key] = env_value
    #print('{} -> {}'.format(env_key,env_value))

print("Content-Type: application/json")    # HTML is following
print()                             # blank line, end of headers
# Print env dictionary in json format
print(json.dumps(env))

#https://www.pythonstudio.us/introduction-2/environment-variables.html
#https://stackoverflow.com/questions/17665619/how-do-i-access-the-urls-query-string-in-a-python-cgi-script
for param in os.environ.keys():
    if (param=="QUERY_STRING"):
        #print(f"<em>{param}</em> = {os.environ[param]}</li>")
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))

for param in os.environ.keys():
    if (param == "HTTP_USER_AGENT"):
        print("<b>%20s</b>: %s<br>" % (param, os.environ[param]))