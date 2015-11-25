class Assets(object):
    def __init__(self, dms_client):
        self.dms_client = dms_client

    def get_assets(self, asset_type, options):
        params = {"assetType": asset_type}
        request = {"options": options}
        return self.dms_client.get(
            "v2/assets/query",
            params=params,
            data=request)['Results']['$values']

    def get_asset(self, id):
        return self.dms_client.get("v2/assets/%s" % id)

    def update_asset(self, id, asset_type, name, created_utc,
                     organization_id,
                     provisioned_service_id,
                     last_modified_utc, update_token,
                     provisioning_status, extra_properties=None):
        updated_asset = {
            "Name": name,
            "CreatedUtc": created_utc,
            "OrganizationId": organization_id,
            "ProvisionedServiceId": provisioned_service_id,
            "LastModifiedUtc": last_modified_utc,
            "UpdateToken": update_token,
            "ProvisioningStatus": provisioning_status
        }
        if extra_properties is not None:
            updated_asset["Properties"] = extra_properties

        return self.dms_client.put("v2/assets/%s" % id,
                                   updated_asset,
                                   params={"assetType": asset_type})

    def create_asset(self, name, asset_type, organization_id,
                     provisioned_service_id, extra_properties=None):
        new_asset = {
            "name": name,
            "assetType": asset_type,
            "organizationId": organization_id,
            "provisionedServiceId": provisioned_service_id
        }
        if extra_properties is not None:
            new_asset["properties"] = extra_properties
        return self.dms_client.post("v2/assets/provision",
                                    new_asset)

    def delete_asset(self, id, delete=True):
        params = {
            "delete": delete
        }
        return self.dms_client.post("v2/assets/%s/deprovision" % id,
                                    params=params)
