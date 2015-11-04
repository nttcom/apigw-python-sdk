#!/usr/bin/env python
# coding: utf-8

import os
from datetime import date
from apigw.client import ApiGWClient

access_token = os.environ.get("ACCESS_TOKEN")
target_date = date.today().strftime("%Y%m%d")

client = ApiGWClient(config_path = "config.json", environment = "production")
api_log = client.api_log(access_token)
response = api_log.get(target_date)

print(">>>>> HTTP status: {0}".format(response.status_code))
if response.ok:
    print(">>>>> Records count: {0}".format(len(response.json().get('Records'))))
