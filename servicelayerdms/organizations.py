class Organizations(object):
    def __init__(self, dms_client):
        self.dms_client = dms_client

    def get_organizations(self):
        return self.dms_client.get("v2/organizations")

    def get_organization(self, id):
        return self.dms_client.get("v2/organizations/%s" % id)
