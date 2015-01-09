# This should change my desktop background to today's top wallpaper post from imgur.
# Hopefully I'll also learn some coding stuff.


import urllib.request
import json
import random
from pprint import pprint

paper_num = random.randrange(0, 10)

print(paper_num)


#wallpapers = 'http://www.reddit.com/r/wallpapers/top.json?t=day&limit=10'


try:
    #response = urllib.request.urlopen(wallpapers)
    #bigjson = response.read()

    with open('jsondata', 'r') as in_file:
        tempjson = json.load(in_file)

    '''
    with open('tempout.txt', 'w') as out_file:
        out_file.write(json.dumps(tempjson, indent=4))
    '''








except urllib.request.URLError as e:
    print('Everything sucks, error: ', e)

