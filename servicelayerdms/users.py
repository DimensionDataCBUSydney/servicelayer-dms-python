class Users(object):
    def __init__(self, dms_client):
        self.dms_client = dms_client

    def get_users(self):
        return self.dms_client.get("v2/users")

    def get_user(self, id):
        return self.dms_client.get("v2/users/%s" % id)
