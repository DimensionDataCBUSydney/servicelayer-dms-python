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

    def get_user_properties(self, id, property_group):
        return self.dms_client.get(
            "v2/users/%s/properties" % id,
            params={"propertyGroup": property_group})

    def get_users_by_ids(self, user_ids):
        return self.dms_client.post(
            "v2/users/query/byids",
            {user_ids})['Results']['$values']

    def update_user(self, id, first_name, last_name, display_name, upn,
                    created_utc, last_modified_utc, update_token,
                    provisioning_status, extra_properties=None):
        updated_user = {
            "FirstName": first_name,
            "LastName": last_name,
            "DisplayName": display_name,
            "Upn": upn,
            "CreatedUtc": created_utc,
            "LastModifiedUtc": last_modified_utc,
            "UpdateToken": update_token,
            "ProvisioningStatus": provisioning_status
        }
        if extra_properties is not None:
            updated_user["Properties"] = extra_properties

        return self.dms_client.put("v2/users/%s" % id, updated_user)

    def create_user(self, first_name, last_name, display_name, upn,
                    organization_id, extra_properties=None):
        params = {
            "firstName": first_name,
            "lastName": last_name,
            "displayName": display_name,
            "upn": upn,
            "organizationId": organization_id
        }
        if extra_properties is not None:
            params["properties"] = extra_properties

        return self.dms_client.post("v2/users/provision", params=params)

    def delete_user(self, id, delete=True):
        params = {
            "delete": delete
        }
        return self.dms_client.post("v2/users/%s/deprovision" % id,
                                    params=params)
