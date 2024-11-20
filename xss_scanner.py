import requests

def check_xss(url):
    payload = '<script>alert("XSS")</script>'
    response = requests.get(url, params={'q': payload})
    if payload in response.text:
        print(f"Possible XSS vulnerability found at: {url}")
    else:
        print(f"No XSS found at: {url}")

check_xss('http://example.com/search')
