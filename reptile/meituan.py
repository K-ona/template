import requests

class MeiTuan:

    def __init__(self, headers):
        self.headers = headers
        
    def send_request(self, url):
        return requests.get(url, headers=self.headers,timeout=3).content
    

if __name__ == "__main__":
    MeiTuan A(headers = '')

    A.headers = ''