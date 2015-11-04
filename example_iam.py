#!/usr/bin/env python
# coding: utf-8
import uuid
import os
import json
from apigw.client import ApiGWClient

access_token = os.environ.get('ACCESS_TOKEN')

uuid = uuid.uuid4()
mail_address = "pyagent_" + '{}'.format(uuid) + "@dummy.com"
input_data = [{ 
        "distributorFlag": 0,
        "mail": mail_address,
        "password": "YOUR_PASSWORD",
        "portalUse": 1
        }] 

client = ApiGWClient(config_path = "config.json", environment = "production")
iam = client.iam(access_token)

print '[1. iam user crete...]'
response = iam.post('users', input_data)

print(">>>>> HTTP status: {0}".format(response.status_code))
data = response.json()

user_uuid = data['users'][0]['uuid']
user_consumer_key = data['users'][0]['consumerKey']
user_secret_key = data['users'][0]['consumerSecret']

search_user_uuid = "users/" + user_uuid
iam.get(search_user_uuid)

print '[2. iam group create...]'
group_name = "pydev_" + '{}'.format(uuid)
group_data = {"groupName": group_name}

print group_data
random_data = group_data

response = iam.post('groups', random_data)
data = response.json()
group_uuid = data["groups"][0]["uuid"]

search_group_uuid = "groups/" + group_uuid
iam.get(search_group_uuid)

print '[3. iam role create...]'
role_data = {"resources": [
    {
     "basePath": "/v1/business-process",
     "ipAddress": "*",
     "path": "*",
     "verb": "*"
    },
    {
     "basePath": "/v1/apilog",
     "ipAddress": "153.142.2.18/32",
     "path": "*",
     "verb": "*"
    },
    {
     "basePath": "/v1/cloudn",
     "ipAddress": "*",
     "path": "*",
     "verb": "*"
     }
   ],
   "roleName": "pyagent-role1"
}

response = iam.post('roles', role_data)
data = response.json()
role_uuid = data["roles"][0]["uuid"]
search_role_uuid = "roles/" + role_uuid
iam.get(search_role_uuid)

print '[4. iam attach group to role...]'
attach_group_to_role_path = "groups/" + group_uuid + "/roles/" + role_uuid
print attach_group_to_role_path
response = iam.put(attach_group_to_role_path)
iam.get(search_group_uuid)

print '[5. iam attach group to user...]'
attach_group_to_user_path = "groups/" + group_uuid + "/users/" + user_uuid
print attach_group_to_user_path
response = iam.put(attach_group_to_user_path)
search_group_users = "groups/" + group_uuid + "/users"
iam.get(search_group_users)

print '[6. test iam user request APIs]'
client = ApiGWClient(config_path = "config.json", environment = "production")
iam_oauth = client.oauth(user_consumer_key, user_secret_key)
response = iam_oauth.request_access_token()
data = response.json()
iam_access_token = data["accessToken"]

print '[6-1. get IAM API...]'
iam_user_iam = client.iam(iam_access_token)
iam_user_iam.get("users")

print '[6-2. get business-process API...]'
service_name = 'bocn'
business_process = client.business_process(iam_access_token)
business_process.get("contracts", service_name)

print '[7. delete role from group...]'
delete_role_from_group_path = "groups/" + group_uuid  + "/roles/" + role_uuid
print delete_role_from_group_path
response = iam.delete(delete_role_from_group_path)
iam.get(search_group_uuid)

print '[8. get business-process API...]'
service_name = 'mss'
business_process.get("contracts", service_name)
