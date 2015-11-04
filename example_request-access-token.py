#!/usr/bin/env python
# coding: utf-8

import os
from apigw.client import ApiGWClient

consumer_key = os.environ.get("CONSUMER_KEY")
secret_key = os.environ.get("SECRET_KEY")

client = ApiGWClient(config_path = "config.json", environment = "production")
oauth = client.oauth(consumer_key, secret_key)
response = oauth.request_access_token()

print(">>>>> HTTP status: {0}".format(response.status_code))
if response.ok:
    print(">>>>> accessToken: {0}".format(response.json().get('accessToken')))
