﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class TfvcClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(TfvcClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '8aa40520-446d-40e6-89f6-9c9f9ce44c48'

    def get_branch(self, path, project=None, include_parent=None, include_children=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if include_parent is not None:
            query_parameters['includeParent'] = self._serialize.query('include_parent', include_parent, 'bool')
        if include_children is not None:
            query_parameters['includeChildren'] = self._serialize.query('include_children', include_children, 'bool')
        response = self._send(http_method='GET',
                              location_id='bc1f417e-239d-42e7-85e1-76e80cb2d6eb',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TfvcBranch', response)

    def get_branches(self, project=None, include_parent=None, include_children=None, include_deleted=None, include_links=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_parent is not None:
            query_parameters['includeParent'] = self._serialize.query('include_parent', include_parent, 'bool')
        if include_children is not None:
            query_parameters['includeChildren'] = self._serialize.query('include_children', include_children, 'bool')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='bc1f417e-239d-42e7-85e1-76e80cb2d6eb',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcBranch]', self._unwrap_collection(response))

    def get_branch_refs(self, scope_path, project=None, include_deleted=None, include_links=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        response = self._send(http_method='GET',
                              location_id='bc1f417e-239d-42e7-85e1-76e80cb2d6eb',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcBranchRef]', self._unwrap_collection(response))

    def get_changeset_changes(self, id=None, skip=None, top=None, continuation_token=None):
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='f32b86f2-15b9-4fe6-81b1-6f8938617ee5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcChange]', self._unwrap_collection(response))

    def create_changeset(self, changeset, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(changeset, 'TfvcChangeset')
        response = self._send(http_method='POST',
                              location_id='0bc8f0a4-6bfb-42a9-ba84-139da7b99c49',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TfvcChangesetRef', response)

    def get_changeset(self, id, project=None, max_change_count=None, include_details=None, include_work_items=None, max_comment_length=None, include_source_rename=None, skip=None, top=None, orderby=None, search_criteria=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if max_change_count is not None:
            query_parameters['maxChangeCount'] = self._serialize.query('max_change_count', max_change_count, 'int')
        if include_details is not None:
            query_parameters['includeDetails'] = self._serialize.query('include_details', include_details, 'bool')
        if include_work_items is not None:
            query_parameters['includeWorkItems'] = self._serialize.query('include_work_items', include_work_items, 'bool')
        if max_comment_length is not None:
            query_parameters['maxCommentLength'] = self._serialize.query('max_comment_length', max_comment_length, 'int')
        if include_source_rename is not None:
            query_parameters['includeSourceRename'] = self._serialize.query('include_source_rename', include_source_rename, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if search_criteria is not None:
            if search_criteria.item_path is not None:
                query_parameters['searchCriteria.itemPath'] = search_criteria.item_path
            if search_criteria.author is not None:
                query_parameters['searchCriteria.author'] = search_criteria.author
            if search_criteria.from_date is not None:
                query_parameters['searchCriteria.fromDate'] = search_criteria.from_date
            if search_criteria.to_date is not None:
                query_parameters['searchCriteria.toDate'] = search_criteria.to_date
            if search_criteria.from_id is not None:
                query_parameters['searchCriteria.fromId'] = search_criteria.from_id
            if search_criteria.to_id is not None:
                query_parameters['searchCriteria.toId'] = search_criteria.to_id
            if search_criteria.follow_renames is not None:
                query_parameters['searchCriteria.followRenames'] = search_criteria.follow_renames
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
            if search_criteria.mappings is not None:
                query_parameters['searchCriteria.mappings'] = search_criteria.mappings
        response = self._send(http_method='GET',
                              location_id='0bc8f0a4-6bfb-42a9-ba84-139da7b99c49',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TfvcChangeset', response)

    def get_changesets(self, project=None, max_comment_length=None, skip=None, top=None, orderby=None, search_criteria=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if max_comment_length is not None:
            query_parameters['maxCommentLength'] = self._serialize.query('max_comment_length', max_comment_length, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if orderby is not None:
            query_parameters['$orderby'] = self._serialize.query('orderby', orderby, 'str')
        if search_criteria is not None:
            if search_criteria.item_path is not None:
                query_parameters['searchCriteria.itemPath'] = search_criteria.item_path
            if search_criteria.author is not None:
                query_parameters['searchCriteria.author'] = search_criteria.author
            if search_criteria.from_date is not None:
                query_parameters['searchCriteria.fromDate'] = search_criteria.from_date
            if search_criteria.to_date is not None:
                query_parameters['searchCriteria.toDate'] = search_criteria.to_date
            if search_criteria.from_id is not None:
                query_parameters['searchCriteria.fromId'] = search_criteria.from_id
            if search_criteria.to_id is not None:
                query_parameters['searchCriteria.toId'] = search_criteria.to_id
            if search_criteria.follow_renames is not None:
                query_parameters['searchCriteria.followRenames'] = search_criteria.follow_renames
            if search_criteria.include_links is not None:
                query_parameters['searchCriteria.includeLinks'] = search_criteria.include_links
            if search_criteria.mappings is not None:
                query_parameters['searchCriteria.mappings'] = search_criteria.mappings
        response = self._send(http_method='GET',
                              location_id='0bc8f0a4-6bfb-42a9-ba84-139da7b99c49',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcChangesetRef]', self._unwrap_collection(response))

    def get_batched_changesets(self, changesets_request_data):
        content = self._serialize.body(changesets_request_data, 'TfvcChangesetsRequestData')
        response = self._send(http_method='POST',
                              location_id='b7e7c173-803c-4fea-9ec8-31ee35c5502a',
                              version='6.0-preview.1',
                              content=content)
        return self._deserialize('[TfvcChangesetRef]', self._unwrap_collection(response))

    def get_changeset_work_items(self, id=None):
        route_values = {}
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        response = self._send(http_method='GET',
                              location_id='64ae0bea-1d71-47c9-a9e5-fe73f5ea0ff4',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[AssociatedWorkItem]', self._unwrap_collection(response))

    def get_items_batch(self, item_request_data, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(item_request_data, 'TfvcItemRequestData')
        response = self._send(http_method='POST',
                              location_id='fe6f827b-5f64-480f-b8af-1eca3b80e833',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[[TfvcItem]]', self._unwrap_collection(response))

    def get_items_batch_zip(self, item_request_data, project=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(item_request_data, 'TfvcItemRequestData')
        response = self._send(http_method='POST',
                              location_id='fe6f827b-5f64-480f-b8af-1eca3b80e833',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_item(self, path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_option is not None:
                query_parameters['versionDescriptor.versionOption'] = version_descriptor.version_option
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ba9fc436-9a38-4578-89d6-e4f3241f5040',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TfvcItem', response)

    def get_item_content(self, path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_option is not None:
                query_parameters['versionDescriptor.versionOption'] = version_descriptor.version_option
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ba9fc436-9a38-4578-89d6-e4f3241f5040',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_items(self, project=None, scope_path=None, recursion_level=None, include_links=None, version_descriptor=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if include_links is not None:
            query_parameters['includeLinks'] = self._serialize.query('include_links', include_links, 'bool')
        if version_descriptor is not None:
            if version_descriptor.version_option is not None:
                query_parameters['versionDescriptor.versionOption'] = version_descriptor.version_option
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
        response = self._send(http_method='GET',
                              location_id='ba9fc436-9a38-4578-89d6-e4f3241f5040',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcItem]', self._unwrap_collection(response))

    def get_item_text(self, path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_option is not None:
                query_parameters['versionDescriptor.versionOption'] = version_descriptor.version_option
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ba9fc436-9a38-4578-89d6-e4f3241f5040',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='text/plain')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_item_zip(self, path, project=None, file_name=None, download=None, scope_path=None, recursion_level=None, version_descriptor=None, include_content=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if path is not None:
            query_parameters['path'] = self._serialize.query('path', path, 'str')
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        if scope_path is not None:
            query_parameters['scopePath'] = self._serialize.query('scope_path', scope_path, 'str')
        if recursion_level is not None:
            query_parameters['recursionLevel'] = self._serialize.query('recursion_level', recursion_level, 'str')
        if version_descriptor is not None:
            if version_descriptor.version_option is not None:
                query_parameters['versionDescriptor.versionOption'] = version_descriptor.version_option
            if version_descriptor.version_type is not None:
                query_parameters['versionDescriptor.versionType'] = version_descriptor.version_type
            if version_descriptor.version is not None:
                query_parameters['versionDescriptor.version'] = version_descriptor.version
        if include_content is not None:
            query_parameters['includeContent'] = self._serialize.query('include_content', include_content, 'bool')
        response = self._send(http_method='GET',
                              location_id='ba9fc436-9a38-4578-89d6-e4f3241f5040',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_label_items(self, label_id, top=None, skip=None):
        route_values = {}
        if label_id is not None:
            route_values['labelId'] = self._serialize.url('label_id', label_id, 'str')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='06166e34-de17-4b60-8cd1-23182a346fda',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcItem]', self._unwrap_collection(response))

    def get_label(self, label_id, request_data, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if label_id is not None:
            route_values['labelId'] = self._serialize.url('label_id', label_id, 'str')
        query_parameters = {}
        if request_data is not None:
            if request_data.label_scope is not None:
                query_parameters['requestData.labelScope'] = request_data.label_scope
            if request_data.name is not None:
                query_parameters['requestData.name'] = request_data.name
            if request_data.owner is not None:
                query_parameters['requestData.owner'] = request_data.owner
            if request_data.item_label_filter is not None:
                query_parameters['requestData.itemLabelFilter'] = request_data.item_label_filter
            if request_data.max_item_count is not None:
                query_parameters['requestData.maxItemCount'] = request_data.max_item_count
            if request_data.include_links is not None:
                query_parameters['requestData.includeLinks'] = request_data.include_links
        response = self._send(http_method='GET',
                              location_id='a5d9bd7f-b661-4d0e-b9be-d9c16affae54',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TfvcLabel', response)

    def get_labels(self, request_data, project=None, top=None, skip=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if request_data is not None:
            if request_data.label_scope is not None:
                query_parameters['requestData.labelScope'] = request_data.label_scope
            if request_data.name is not None:
                query_parameters['requestData.name'] = request_data.name
            if request_data.owner is not None:
                query_parameters['requestData.owner'] = request_data.owner
            if request_data.item_label_filter is not None:
                query_parameters['requestData.itemLabelFilter'] = request_data.item_label_filter
            if request_data.max_item_count is not None:
                query_parameters['requestData.maxItemCount'] = request_data.max_item_count
            if request_data.include_links is not None:
                query_parameters['requestData.includeLinks'] = request_data.include_links
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='a5d9bd7f-b661-4d0e-b9be-d9c16affae54',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcLabelRef]', self._unwrap_collection(response))

    def get_shelveset_changes(self, shelveset_id, top=None, skip=None):
        query_parameters = {}
        if shelveset_id is not None:
            query_parameters['shelvesetId'] = self._serialize.query('shelveset_id', shelveset_id, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='dbaf075b-0445-4c34-9e5b-82292f856522',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcChange]', self._unwrap_collection(response))

    def get_shelveset(self, shelveset_id, request_data=None):
        query_parameters = {}
        if shelveset_id is not None:
            query_parameters['shelvesetId'] = self._serialize.query('shelveset_id', shelveset_id, 'str')
        if request_data is not None:
            if request_data.name is not None:
                query_parameters['requestData.name'] = request_data.name
            if request_data.owner is not None:
                query_parameters['requestData.owner'] = request_data.owner
            if request_data.max_comment_length is not None:
                query_parameters['requestData.maxCommentLength'] = request_data.max_comment_length
            if request_data.max_change_count is not None:
                query_parameters['requestData.maxChangeCount'] = request_data.max_change_count
            if request_data.include_details is not None:
                query_parameters['requestData.includeDetails'] = request_data.include_details
            if request_data.include_work_items is not None:
                query_parameters['requestData.includeWorkItems'] = request_data.include_work_items
            if request_data.include_links is not None:
                query_parameters['requestData.includeLinks'] = request_data.include_links
        response = self._send(http_method='GET',
                              location_id='e36d44fb-e907-4b0a-b194-f83f1ed32ad3',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('TfvcShelveset', response)

    def get_shelvesets(self, request_data=None, top=None, skip=None):
        query_parameters = {}
        if request_data is not None:
            if request_data.name is not None:
                query_parameters['requestData.name'] = request_data.name
            if request_data.owner is not None:
                query_parameters['requestData.owner'] = request_data.owner
            if request_data.max_comment_length is not None:
                query_parameters['requestData.maxCommentLength'] = request_data.max_comment_length
            if request_data.max_change_count is not None:
                query_parameters['requestData.maxChangeCount'] = request_data.max_change_count
            if request_data.include_details is not None:
                query_parameters['requestData.includeDetails'] = request_data.include_details
            if request_data.include_work_items is not None:
                query_parameters['requestData.includeWorkItems'] = request_data.include_work_items
            if request_data.include_links is not None:
                query_parameters['requestData.includeLinks'] = request_data.include_links
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='e36d44fb-e907-4b0a-b194-f83f1ed32ad3',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TfvcShelvesetRef]', self._unwrap_collection(response))

    def get_shelveset_work_items(self, shelveset_id):
        query_parameters = {}
        if shelveset_id is not None:
            query_parameters['shelvesetId'] = self._serialize.query('shelveset_id', shelveset_id, 'str')
        response = self._send(http_method='GET',
                              location_id='a7a0c1c1-373e-425a-b031-a519474d743d',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[AssociatedWorkItem]', self._unwrap_collection(response))

