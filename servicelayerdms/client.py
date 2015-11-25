import requests
from .exceptions import DmsRequestError


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
        http_error_msg = ''
        if 400 <= response.status_code < 500:
            http_error_msg = '%s Client Error: %s' % (
                response.status_code, response.json()['Message'])
        elif 500 <= response.status_code < 600:
            http_error_msg = '%s Server Error: %s' % (
                response.status_code, response.json()['Message'])
        if http_error_msg:
            raise DmsRequestError(http_error_msg, response.status_code)
        else:
            return response.json()

    def post(self, uri, data, params=None):
        response = requests.post(self.api_url + uri,
                                 params=params,
                                 data=data,
                                 headers=self._get_default_headers(),
                                 verify=self.verify)
        http_error_msg = ''
        if 400 <= response.status_code < 500:
            http_error_msg = '%s Client Error: %s' % (
                response.status_code, response.json()['Message'])
        elif 500 <= response.status_code < 600:
            http_error_msg = '%s Server Error: %s' % (
                response.status_code, response.json()['Message'])
        if http_error_msg:
            raise DmsRequestError(http_error_msg, response.status_code)
        else:
            return response.json()

    def put(self, uri, data, params=None):
        response = requests.put(self.api_url + uri,
                                params=params,
                                data=data,
                                headers=self._get_default_headers(),
                                verify=self.verify)
        http_error_msg = ''
        if 400 <= response.status_code < 500:
            http_error_msg = '%s Client Error: %s' % (
                response.status_code, response.json()['Message'])
        elif 500 <= response.status_code < 600:
            http_error_msg = '%s Server Error: %s' % (
                response.status_code, response.json()['Message'])
        if http_error_msg:
            raise DmsRequestError(http_error_msg, response.status_code)
        else:
            return response.json()
