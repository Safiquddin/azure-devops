﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class SecurityClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(SecurityClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def remove_access_control_entries(self, security_namespace_id, token=None, descriptors=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        if descriptors is not None:
            query_parameters['descriptors'] = self._serialize.query('descriptors', descriptors, 'str')
        response = self._send(http_method='DELETE',
                              location_id='ac08c8ff-4323-4b08-af90-bcd018d380ce',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def set_access_control_entries(self, container, security_namespace_id):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        content = self._serialize.body(container, 'object')
        response = self._send(http_method='POST',
                              location_id='ac08c8ff-4323-4b08-af90-bcd018d380ce',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[AccessControlEntry]', self._unwrap_collection(response))

    def query_access_control_lists(self, security_namespace_id, token=None, descriptors=None, include_extended_info=None, recurse=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        if descriptors is not None:
            query_parameters['descriptors'] = self._serialize.query('descriptors', descriptors, 'str')
        if include_extended_info is not None:
            query_parameters['includeExtendedInfo'] = self._serialize.query('include_extended_info', include_extended_info, 'bool')
        if recurse is not None:
            query_parameters['recurse'] = self._serialize.query('recurse', recurse, 'bool')
        response = self._send(http_method='GET',
                              location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[AccessControlList]', self._unwrap_collection(response))

    def remove_access_control_lists(self, security_namespace_id, tokens=None, recurse=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if tokens is not None:
            query_parameters['tokens'] = self._serialize.query('tokens', tokens, 'str')
        if recurse is not None:
            query_parameters['recurse'] = self._serialize.query('recurse', recurse, 'bool')
        response = self._send(http_method='DELETE',
                              location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('bool', response)

    def set_access_control_lists(self, access_control_lists, security_namespace_id):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        content = self._serialize.body(access_control_lists, 'VssJsonCollectionWrapper')
        self._send(http_method='POST',
                   location_id='18a2ad18-7571-46ae-bec7-0c7da1495885',
                   version='5.0',
                   route_values=route_values,
                   content=content)

    def has_permissions_batch(self, eval_batch):
        content = self._serialize.body(eval_batch, 'PermissionEvaluationBatch')
        response = self._send(http_method='POST',
                              location_id='cf1faa59-1b63-4448-bf04-13d981a46f5d',
                              version='5.0',
                              content=content)
        return self._deserialize('PermissionEvaluationBatch', response)

    def has_permissions(self, security_namespace_id, permissions=None, tokens=None, always_allow_administrators=None, delimiter=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        if permissions is not None:
            route_values['permissions'] = self._serialize.url('permissions', permissions, 'int')
        query_parameters = {}
        if tokens is not None:
            query_parameters['tokens'] = self._serialize.query('tokens', tokens, 'str')
        if always_allow_administrators is not None:
            query_parameters['alwaysAllowAdministrators'] = self._serialize.query('always_allow_administrators', always_allow_administrators, 'bool')
        if delimiter is not None:
            query_parameters['delimiter'] = self._serialize.query('delimiter', delimiter, 'str')
        response = self._send(http_method='GET',
                              location_id='dd3b8bd6-c7fc-4cbd-929a-933d9c011c9d',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[bool]', self._unwrap_collection(response))

    def remove_permission(self, security_namespace_id, descriptor, permissions=None, token=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        if permissions is not None:
            route_values['permissions'] = self._serialize.url('permissions', permissions, 'int')
        query_parameters = {}
        if descriptor is not None:
            query_parameters['descriptor'] = self._serialize.query('descriptor', descriptor, 'str')
        if token is not None:
            query_parameters['token'] = self._serialize.query('token', token, 'str')
        response = self._send(http_method='DELETE',
                              location_id='dd3b8bd6-c7fc-4cbd-929a-933d9c011c9d',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('AccessControlEntry', response)

    def query_security_namespaces(self, security_namespace_id=None, local_only=None):
        route_values = {}
        if security_namespace_id is not None:
            route_values['securityNamespaceId'] = self._serialize.url('security_namespace_id', security_namespace_id, 'str')
        query_parameters = {}
        if local_only is not None:
            query_parameters['localOnly'] = self._serialize.query('local_only', local_only, 'bool')
        response = self._send(http_method='GET',
                              location_id='ce7b9f95-fde9-4be8-a86d-83b366f0b87a',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[SecurityNamespaceDescription]', self._unwrap_collection(response))

