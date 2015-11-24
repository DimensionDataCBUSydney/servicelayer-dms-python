import requests


class DmsClient(object):
    def __init__(self, sts_client, api_url, verify=False):
        self.sts_client = sts_client
        self.api_url = api_url
        self.verify = verify
        self.token = self.sts_client.get_token()

    def _get_default_headers(self):
        return {"X-Auth-Token": self.token}

    def get(self, uri, params=None):
        response = requests.get(self.api_url + uri,
                                params=params,
                                headers=self._get_default_headers(),
                                verify=self.verify)
        return response.json()
