# This should change my desktop background to today's top wallpaper post from imgur.
# Hopefully I'll also learn some coding stuff.


import urllib.request

kitty = 'http://placekitten.com/'

try:
    response = urllib.request.urlopen(kitty)
    kittens = response.read()
    body = kittens[559:1000]

    with open('temp.txt', 'w') as out_file:
        out_file.write(str(body))
            #out_file.write(line)

    with open('temp.txt', 'r') as in_file:
        text = in_file.read()

    print(body)

except urllib.request.URLError as e:
    print('no kitties, error: ', e)

