﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class PipelinesClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(PipelinesClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_log(self, project, pipeline_id, run_id, log_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if log_id is not None:
            route_values['logId'] = self._serialize.url('log_id', log_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='fb1b6d27-3957-43d5-a14b-a2d70403e545',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Log', response)

    def list_logs(self, project, pipeline_id, run_id, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='fb1b6d27-3957-43d5-a14b-a2d70403e545',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('LogCollection', response)

    def create_pipeline(self, input_parameters, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(input_parameters, 'CreatePipelineParameters')
        response = self._send(http_method='POST',
                              location_id='28e1305e-2afe-47bf-abaf-cbb0e6a91988',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Pipeline', response)

    def get_pipeline(self, project, pipeline_id, pipeline_version=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        query_parameters = {}
        if pipeline_version is not None:
            query_parameters['pipelineVersion'] = self._serialize.query('pipeline_version', pipeline_version, 'int')
        response = self._send(http_method='GET',
                              location_id='28e1305e-2afe-47bf-abaf-cbb0e6a91988',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Pipeline', response)

    def list_pipelines(self, project, order_by=None, top=None, continuation_token=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if order_by is not None:
            query_parameters['orderBy'] = self._serialize.query('order_by', order_by, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='28e1305e-2afe-47bf-abaf-cbb0e6a91988',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_value = self._deserialize('[Pipeline]', self._unwrap_collection(response))
        continuation_token = self._get_continuation_token(response)
        return self.ListPipelinesResponseValue(response_value, continuation_token)

    class ListPipelinesResponseValue(object):
        def __init__(self, value, continuation_token):
            self.value = value
            self.continuation_token = continuation_token

    def get_run(self, project, pipeline_id, run_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='7859261e-d2e9-4a68-b820-a5d84cc5bb3d',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('Run', response)

    def list_runs(self, project, pipeline_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        response = self._send(http_method='GET',
                              location_id='7859261e-d2e9-4a68-b820-a5d84cc5bb3d',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[Run]', self._unwrap_collection(response))

    def run_pipeline(self, run_parameters, project, pipeline_id, pipeline_version=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if pipeline_id is not None:
            route_values['pipelineId'] = self._serialize.url('pipeline_id', pipeline_id, 'int')
        query_parameters = {}
        if pipeline_version is not None:
            query_parameters['pipelineVersion'] = self._serialize.query('pipeline_version', pipeline_version, 'int')
        content = self._serialize.body(run_parameters, 'RunPipelineParameters')
        response = self._send(http_method='POST',
                              location_id='7859261e-d2e9-4a68-b820-a5d84cc5bb3d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Run', response)

