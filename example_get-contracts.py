#!/usr/bin/env python
# coding: utf-8

import os
from apigw.client import ApiGWClient

access_token = os.environ.get("ACCESS_TOKEN")
service_name = os.environ.get("SERVICE_NAME")

client = ApiGWClient(config_path = "config.json", environment = "production")
business_process = client.business_process(access_token)
response = business_process.get("contracts", service_name)

print(">>>>> HTTP status: {0}".format(response.status_code))
if response.ok:
    print(">>>>> items count: {0}".format(len(response.json().get('items'))))
