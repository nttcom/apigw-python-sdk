#!/usr/bin/env python
# coding: utf-8

import os
import json
from apigw.client import ApiGWClient

access_token = os.environ.get('ACCESS_TOKEN')
service_name = 'unol2' # 固定
data = json.load(open('example_new-service-order-data.json', 'r'))

client = ApiGWClient(config_path = "config.json", environment = "production")
business_process = client.business_process(access_token)
response = business_process.post('service-orders', service_name, data, querys={ 'pattern': 'new' })

print(">>>>> HTTP status: {0}".format(response.status_code))
if response.ok:
    response_key = response.json().get('key')
    print(">>>>> circuitEntryId: {0}, circuitEntrySubid: {1}".format(response_key.get('circuitEntryId'), response_key.get('circuitEntrySubid')))
