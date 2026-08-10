"""
Module 2: HTTP Methods & Programmatic Status Code Class Handlers
"""
from typing import Any, Dict, Optional
import requests


def execute_and_categorize(
    method: str, url: str, payload: Optional[Dict[str, Any]] = None
) -> None:
    """Executes any HTTP verb and categorizes the returned status code class."""
    try:
        response = requests.request(
            method=method,
            url=url,
            json=payload,
            timeout=5.0,
            allow_redirects=False,
        )
        code = response.status_code

        # SUCCESS
        if 200 <= code < 300:
            print(f"[2xx SUCCESS - {code}] {method:<6} {url}")
            if code == 201:
                print("  -> Resource successfully created in backend storage.")
            elif code == 204:
                print("  -> Operation succeeded; server returned empty payload.")

        #  REDIRECTION
        elif 300 <= code < 400:
            destination = response.headers.get("Location", "Unknown Target")
            print(f"[3xx REDIRECT - {code}] {method:<6} {url}")
            print(f"  -> Server instructed redirect to: {destination}")

        # CLIENT ERROR 
        elif 400 <= code < 500:
            print(f"[4xx CLIENT ERROR - {code}] {method:<6} {url}")
            if code == 400:
                print("  -> 400 Bad Request: Malformed syntax or invalid payload.")
            elif code == 401:
                print("  -> 401 Unauthorized: Identity unverified (missing auth).")
            elif code == 403:
                print("  -> 403 Forbidden: Identity known, but lacking ACL permissions.")
            elif code == 404:
                print("  -> 404 Not Found: Target resource URI does not exist.")
            elif code == 429:
                retry_after = response.headers.get("Retry-After", "Unknown")
                print(f"  -> 429 Too Many Requests: Rate-limited! Wait {retry_after}s.")

        #  SERVER ERROR
        elif 500 <= code < 600:
            print(f"[5xx SERVER ERROR - {code}] {method:<6} {url}")
            print("  -> Upstream crash or overload. Candidate for Exponential Backoff!")

    except requests.exceptions.RequestException as err:
        print(f"[NETWORK FAILURE] Socket/DNS error connecting to {url}: {err}")



execute_and_categorize("GET", "https://httpbin.org/status/200")
execute_and_categorize("POST", "https://httpbin.org/status/201", {"name": "test"})
execute_and_categorize("DELETE", "https://httpbin.org/status/204")
execute_and_categorize("GET", "https://httpbin.org/status/302")
execute_and_categorize("GET", "https://httpbin.org/status/401")
execute_and_categorize("GET", "https://httpbin.org/status/403")
execute_and_categorize("GET", "https://httpbin.org/status/404")
execute_and_categorize("GET", "https://httpbin.org/status/429")
execute_and_categorize("GET", "https://httpbin.org/status/500")