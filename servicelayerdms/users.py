class Users(object):
    def __init__(self, dms_client):
        self.dms_client = dms_client

    def get_users(self, organization):
        return self.dms_client.post(
            "v2/users/query",
            {"OrganizationId": organization,
             "WithProperties": []})['Results']['$values']

    def get_user(self, id):
        return self.dms_client.get("v2/users/%s" % id)
