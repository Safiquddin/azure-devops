﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.profile import models


class ProfileClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ProfileClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8ccfef3d-2b87-4e99-8ccb-66e343d2daa8'

    def get_profile(self, id, details=None, with_attributes=None, partition=None, core_attributes=None, force_refresh=None):
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if details is not None:
            query_parameters['details'] = self._serialize.query('details', details, 'bool')
        if with_attributes is not None:
            query_parameters['withAttributes'] = self._serialize.query('with_attributes', with_attributes, 'bool')
        if partition is not None:
            query_parameters['partition'] = self._serialize.query('partition', partition, 'str')
        if core_attributes is not None:
            query_parameters['coreAttributes'] = self._serialize.query('core_attributes', core_attributes, 'str')
        if force_refresh is not None:
            query_parameters['forceRefresh'] = self._serialize.query('force_refresh', force_refresh, 'bool')
        response = self._send(http_method='GET',
                              location_id='f83735dc-483f-4238-a291-d45f6080a9af',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Profile', response)

