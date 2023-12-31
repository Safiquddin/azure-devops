﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class SearchClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(SearchClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'ea48a0a1-269c-42d8-b8ad-ddc8fcdcf578'

    def fetch_code_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'CodeSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e7f29993-5b82-4fca-9386-f5cfe683d524',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('CodeSearchResponse', response)

    def fetch_wiki_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WikiSearchRequest')
        response = self._send(http_method='POST',
                              location_id='e90e7664-7049-4100-9a86-66b161d81080',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiSearchResponse', response)

    def fetch_work_item_search_results(self, request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(request, 'WorkItemSearchRequest')
        response = self._send(http_method='POST',
                              location_id='73b2c9e2-ff9e-4447-8cda-5f5b21ff7cae',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemSearchResponse', response)

