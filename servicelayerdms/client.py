class Client(object):
    def __init__(self, sts_client):
        self.sts_client = sts_client
        self.token = self.sts_client.get_token()
