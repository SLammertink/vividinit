#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import instagramy
from instagramy import InstagramUser
import os
import requests

directory="static/images/instagram_"


def get_profile_pic():
    session_id = "48842033096%3A9au9J0jH8XeNKT%3A5"
    user = InstagramUser('vividinit', sessionid=session_id)
    profile_pic = user.profile_picture_url
    pic_name = "profile_picture.jpg"
    response = requests.get(profile_pic)
    with open(directory + pic_name, 'wb') as f:
        f.write(response.content)

if __name__ == '__main__':
    get_profile_pic()
