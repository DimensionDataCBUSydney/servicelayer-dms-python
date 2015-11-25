class Organizations(object):
    def __init__(self, dms_client):
        self.dms_client = dms_client

    def get_organizations(self, parent_organization_id='Organizations/ROOT'):
        data = {
            "ParentOrganizationId": parent_organization_id
        }
        return self.dms_client.post(
            "v2/organizations/query", data)['Results']['$values']

    def get_organization(self, id):
        return self.dms_client.get("v2/organizations/%s" % id)

    def get_organization_properties(self, id, property_group):
        return self.dms_client.get(
            "v2/organizations/%s/properties" % id,
            params={"propertyGroup": property_group})

    def get_organizations_by_ids(self, organization_ids):
        list_str = '\',\''.join(organization_ids)
        return self.dms_client.post(
            "v2/organizations/query/byids",
            "['%s']" % list_str)

    def update_organization(self, id, name, created_utc,
                            last_modified_utc, update_token,
                            provisioning_status, extra_properties=None):
        updated_organization = {
            "Name": name,
            "CreatedUtc": created_utc,
            "LastModifiedUtc": last_modified_utc,
            "UpdateToken": update_token,
            "ProvisioningStatus": provisioning_status
        }
        if extra_properties is not None:
            updated_organization["Properties"] = extra_properties

        return self.dms_client.put("v2/organizations/%s" % id,
                                   updated_organization)

    def create_organization(self, name, parent_organization_id,
                            extra_properties=None):
        new_organization = {
            "Name": name,
            "ParentOrganizationId": parent_organization_id
        }
        if extra_properties is not None:
            new_organization["Properties"] = extra_properties
        return self.dms_client.post("v2/organizations/provision",
                                    new_organization)

    def delete_organization(self, id, delete=True):
        params = {
            "delete": delete
        }
        return self.dms_client.post("v2/organizations/%s/deprovision" % id,
                                    {}, params=params)
