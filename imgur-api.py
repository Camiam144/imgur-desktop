# This should change my desktop background to today's top wallpaper post from imgur.
# Hopefully I'll also learn some coding stuff.


import urllib.request
import json
import random

'''

wallpapers = 'http://www.reddit.com/r/wallpapers/top.json?t=week&limit=25'


try:
    response = urllib.request.urlopen(wallpapers)
    content = response.read()
    json_data = json.loads(content.decode('utf-8'))


except urllib.request.URLError as e:
    print('Everything sucks, error: ', e)

with open('tempout.txt', 'w') as out_file:
    out_file.write(json.dumps(json_data, indent=4))

'''

with open('tempout.txt', 'r') as in_file:
        json_data = json.load(in_file)


# define a function that navigates to the random wallpaper and check if it's from imgur.
# input data must be a json

def reddit_paper(data):

    number = random.randrange(0, 25)

    trial_domain = data["data"]["children"][number]["data"]["domain"]

    if trial_domain == 'i.imgur.com':
        wallpaper_url = data["data"]["children"][number]["data"]["url"]
        return wallpaper_url

imgur_url = reddit_paper(json_data)



