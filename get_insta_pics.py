#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import instagramy
from instagramy import InstagramUser
import os
import requests

directory="static/images/instagram_"
def get_pics():
    links = []
    session_id = "48842033096%3A9au9J0jH8XeNKT%3A5"
    user = InstagramUser('vividinit', from_cache=True)
    posts = user.posts
    for post in posts:
        links.append(f"{post[7]}media/?size=l")
    return links

def save_pics():
    j = 1
    while j <= len(get_pics()):
        for i in get_pics():
            pic_name = f"pict_{j}.jpg"
            response = requests.get(i)
            with open(directory + pic_name, 'wb') as f:
                f.write(response.content)
                j += 1

if __name__ == '__main__':
    save_pics()
