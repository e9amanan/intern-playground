"""
Module 4: Complete REST CRUD Operations & JSON Wire Serialization
"""
import json
import requests

API_ROOT = "https://jsonplaceholder.typicode.com"
headers = {"User-Agent": "REST-CRUD-Master/1.0", "Content-Type": "application/json"}


# HTTP GET

get_response = requests.get(f"{API_ROOT}/posts/1", headers=headers, timeout=5.0)

# DESERIALIZATION
post_data = get_response.json()
print(f"[READ - GET] Title: {post_data.get('title')[:30]}...")


# HTTP POST 

new_resource_dict = {
    "title": "HTTP & REST Architecture",
    "body": "Mastering status codes and JSON serialization.",
    "userId": 42,
}

# SERIALIZATION
json_wire_payload = json.dumps(new_resource_dict)

post_response = requests.post(
    f"{API_ROOT}/posts",
    headers=headers,
    data=json_wire_payload, 
    timeout=5.0,
)
created_resource = post_response.json()
print(f"[CREATE - POST] Status: {post_response.status_code} | Assigned ID: {created_resource.get('id')}")

# HTTP PUT

put_payload = {
    "id": 1,
    "title": "Completely Overwritten Resource",
    "body": "All previous body fields were replaced.",
    "userId": 42,
}
put_response = requests.put(
    f"{API_ROOT}/posts/1",
    headers=headers,
    json=put_payload, 
    timeout=5.0,
)
print(f"[REPLACE - PUT] Status: {put_response.status_code} | New Title: {put_response.json().get('title')}")


# HTTP PATCH 

patch_payload = {"title": "Only Title Was Updated Via Patch"}
patch_response = requests.patch(
    f"{API_ROOT}/posts/1",
    headers=headers,
    json=patch_payload,
    timeout=5.0,
)
print(f"[MODIFY - PATCH] Status: {patch_response.status_code} | Patched Title: {patch_response.json().get('title')}")


# HTTP DELETE

delete_response = requests.delete(f"{API_ROOT}/posts/1", headers=headers, timeout=5.0)
print(f"[DELETE - DELETE] Status: {delete_response.status_code} | Response Empty? {delete_response.text == '{}'}")