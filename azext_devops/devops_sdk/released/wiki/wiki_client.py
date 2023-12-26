﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v5_1.wiki import models


class WikiClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WikiClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'bf7d82a0-8aa5-4613-94ef-6172a5ea01f3'

    def create_attachment(self, upload_stream, project, wiki_identifier, name, version_descriptor=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if name is not None:
            query_parameters['name'] = self._serialize.query('name', name, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='PUT',
                              location_id='c4382d8d-fefc-40e0-92c5-49852e9e17c0',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        response_object = models.WikiAttachmentResponse()
        response_object.attachment = self._deserialize('WikiAttachment', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def create_page_move(self, page_move_parameters, project, wiki_identifier, comment=None, version_descriptor=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        content = self._serialize.body(page_move_parameters, 'WikiPageMoveParameters')
        response = self._send(http_method='POST',
                              location_id='e37bbe71-cbae-49e5-9a4e-949143b9d910',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        response_object = models.WikiPageMoveResponse()
        response_object.page_move = self._deserialize('WikiPageMove', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def create_or_update_page(self, parameters, project, wiki_identifier, path, version, comment=None, version_descriptor=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        additional_headers = {}
        if version is not None:
            additional_headers['If-Match'] = version
        content = self._serialize.body(parameters, 'WikiPageCreateOrUpdateParameters')
        response = self._send(http_method='PUT',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              additional_headers=additional_headers,
                              content=content)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def delete_page(self, project, wiki_identifier, path, comment=None, version_descriptor=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if comment is not None:
            query_parameters['comment'] = self._serialize.query('comment', comment, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        response = self._send(http_method='DELETE',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        response_object = models.WikiPageResponse()
        response_object.page = self._deserialize('WikiPage', response)
        response_object.eTag = response.headers.get('ETag')
        return response_object

    def get_page_text(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_page_zip(self, project, wiki_identifier, path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
            if version_descriptor.version_options is not None:
                query_parameters['versionDescriptor.versionOptions'] = version_descriptor.version_options
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='25d3fbc7-fe3d-46cb-b5a5-0b6f79caf27b',
                              version='5.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def create_wiki(self, wiki_create_params, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(wiki_create_params, 'WikiCreateParametersV2')
        response = self._send(http_method='POST',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

    def delete_wiki(self, wiki_identifier, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='DELETE',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def get_all_wikis(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('[WikiV2]', self._unwrap_collection(response))

    def get_wiki(self, wiki_identifier, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        response = self._send(http_method='GET',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='5.1',
                              route_values=route_values)
        return self._deserialize('WikiV2', response)

    def update_wiki(self, update_parameters, wiki_identifier, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if wiki_identifier is not None:
            route_values['wikiIdentifier'] = self._serialize.url('wiki_identifier', wiki_identifier, 'str')
        content = self._serialize.body(update_parameters, 'WikiUpdateParameters')
        response = self._send(http_method='PATCH',
                              location_id='288d122c-dbd4-451d-aa5f-7dbbba070728',
                              version='5.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WikiV2', response)

