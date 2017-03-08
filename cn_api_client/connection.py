import requests

class Connection():

    def perform_request(self, url):

        req = requests.get(url)

        if req.status_code == 200:

            return req.text

        else:
            req.raise_for_status()

