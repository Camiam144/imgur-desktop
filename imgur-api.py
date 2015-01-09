# This should change my desktop background to today's top wallpaper post from imgur.
# Hopefully I'll also learn some coding stuff.


import urllib.request
import json
import random


paper_num = random.randrange(0, 10)

print(paper_num)


#wallpapers = 'http://www.reddit.com/r/wallpapers/top.json?t=day&limit=10'

'''
try:
    #response = urllib.request.urlopen(wallpapers)
    #bigjson = response.read()

except urllib.request.URLError as e:
    print('Everything sucks, error: ', e)
'''

with open('jsondata', 'r') as in_file:
        tempjson = json.load(in_file)

'''
with open('tempout.txt', 'w') as out_file:
        out_file.write(json.dumps(tempjson, indent=4))
'''

# define a function that navigates to the random wallpaper and check if it's from imgur.
# imput data must be a json

def paper_getter(data, number):

    trial_domain = data["data"]["children"][number]["data"]["domain"]

    Nsfw = data["data"]["children"][number]["data"]["over_18"]

    if trial_domain == 'i.imgur.com' and not Nsfw: