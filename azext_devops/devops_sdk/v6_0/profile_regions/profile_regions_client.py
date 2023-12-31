﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ProfileRegionsClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ProfileRegionsClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8ccfef3d-2b87-4e99-8ccb-66e343d2daa8'

    def get_geo_region(self, ip):
        query_parameters = {}
        if ip is not None:
            query_parameters['ip'] = self._serialize.query('ip', ip, 'str')
        response = self._send(http_method='GET',
                              location_id='35b3ff1d-ab4c-4d1c-98bb-f6ea21d86bd9',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('GeoRegion', response)

    def get_regions(self):
        response = self._send(http_method='GET',
                              location_id='b129ca90-999d-47bb-ab37-0dcf784ee633',
                              version='6.0-preview.1')
        return self._deserialize('ProfileRegions', response)

