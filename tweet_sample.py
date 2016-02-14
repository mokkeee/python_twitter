#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'mokkeee'


import configparser
from requests_oauthlib import OAuth1Session


def __new_client():
    config_file = 'tweet.ini'
    auth_section_name = 'Auth'

    config = configparser.ConfigParser()
    config.sections()
    config.read(config_file)

    consumer_key = config[auth_section_name]['CK']
    consumer_secret = config[auth_section_name]['CS']
    access_token = config[auth_section_name]['AT']
    access_token_secret = config[auth_section_name]['AS']

    # OAuth認証のクライアント
    return OAuth1Session(consumer_key, consumer_secret, access_token, access_token_secret)


# ツイート投稿用のURL
url = "https://api.twitter.com/1.1/statuses/update.json"

# ツイート本文
params = {"status": "test tweet."}

# POST method で投稿
twitter = __new_client()
req = twitter.post(url, params=params)

# レスポンスを確認
if req.status_code == 200:
    print("OK")
else:
    print("Error: %d" % req.status_code)
