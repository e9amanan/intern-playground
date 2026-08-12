import requests

#  Define HTTP Headers
request_headers = {
    "User-Agent": "IITR-CSE-RESTClient/1.0 (Linux; x86_64)",
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.sample_payload",
}

#  Execute the HTTP Request cycle over TCP/TLS
response = requests.get(
    url="https://httpbin.org/get",
    headers=request_headers,
    params={"module": "http_fundamentals", "week": "4"},
    timeout=5.0,
)

# Inspect the outgoing HTTP
wire_req = response.request
print("=== OUTGOING HTTP REQUEST ===")
print(f"HTTP Verb      : {wire_req.method}")
print(f"Target URI     : {wire_req.url}")
print("Headers Sent   :")
for header_name, header_val in wire_req.headers.items():
    print(f"  {header_name:<16}: {header_val}")

# Inspect the incoming HTTP
print("\n=== INCOMING HTTP RESPONSE ===")
print(f"Status Code    : {response.status_code} ({response.reason})")
print(f"Round-Trip Time: {response.elapsed.total_seconds():.3f} seconds")
print("Server Headers :")
for header_name, header_val in response.headers.items():
    print(f"  {header_name:<20}: {header_val}")
