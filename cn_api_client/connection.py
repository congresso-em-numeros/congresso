import requests

class Connection():

    def perform_request(self, url):

        try:
            req = requests.get(url)

            return req.text

        except Exception as e:

            raise ConnectionError(e)