﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class WorkItemTrackingClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(WorkItemTrackingClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '5264459e-e5e0-4bd8-b118-0985e68a4ec5'

    def get_recent_activity_data(self):
        response = self._send(http_method='GET',
                              location_id='1bc988f4-c15f-4072-ad35-497c87e3a909',
                              version='6.0-preview.2')
        return self._deserialize('[AccountRecentActivityWorkItemModel2]', self._unwrap_collection(response))

    def get_work_artifact_link_types(self):
        response = self._send(http_method='GET',
                              location_id='1a31de40-e318-41cd-a6c6-881077df52e3',
                              version='6.0-preview.1')
        return self._deserialize('[WorkArtifactLink]', self._unwrap_collection(response))

    def query_work_items_for_artifact_uris(self, artifact_uri_query, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(artifact_uri_query, 'ArtifactUriQuery')
        response = self._send(http_method='POST',
                              location_id='a9a9aa7a-8c09-44d3-ad1b-46e855c1e3d3',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ArtifactUriQueryResult', response)

    def create_attachment(self, upload_stream, project=None, file_name=None, upload_type=None, area_path=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if upload_type is not None:
            query_parameters['uploadType'] = self._serialize.query('upload_type', upload_type, 'str')
        if area_path is not None:
            query_parameters['areaPath'] = self._serialize.query('area_path', area_path, 'str')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        content = self._client.stream_upload(upload_stream, callback=callback)
        response = self._send(http_method='POST',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/octet-stream')
        return self._deserialize('AttachmentReference', response)

    def get_attachment_content(self, id, project=None, file_name=None, download=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        response = self._send(http_method='GET',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/octet-stream')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_attachment_zip(self, id, project=None, file_name=None, download=None, **kwargs):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if file_name is not None:
            query_parameters['fileName'] = self._serialize.query('file_name', file_name, 'str')
        if download is not None:
            query_parameters['download'] = self._serialize.query('download', download, 'bool')
        response = self._send(http_method='GET',
                              location_id='e07b5fa4-1499-494d-a496-64b860fd64ff',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='application/zip')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_classification_nodes(self, project, ids, depth=None, error_policy=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if error_policy is not None:
            query_parameters['errorPolicy'] = self._serialize.query('error_policy', error_policy, 'str')
        response = self._send(http_method='GET',
                              location_id='a70579d1-f53a-48ee-a5be-7be8659023b9',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemClassificationNode]', self._unwrap_collection(response))

    def get_root_nodes(self, project, depth=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        response = self._send(http_method='GET',
                              location_id='a70579d1-f53a-48ee-a5be-7be8659023b9',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemClassificationNode]', self._unwrap_collection(response))

    def create_or_update_classification_node(self, posted_node, project, structure_group, path=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        content = self._serialize.body(posted_node, 'WorkItemClassificationNode')
        response = self._send(http_method='POST',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemClassificationNode', response)

    def delete_classification_node(self, project, structure_group, path=None, reclassify_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if reclassify_id is not None:
            query_parameters['$reclassifyId'] = self._serialize.query('reclassify_id', reclassify_id, 'int')
        self._send(http_method='DELETE',
                   location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                   version='6.0-preview.2',
                   route_values=route_values,
                   query_parameters=query_parameters)

    def get_classification_node(self, project, structure_group, path=None, depth=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        query_parameters = {}
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        response = self._send(http_method='GET',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemClassificationNode', response)

    def update_classification_node(self, posted_node, project, structure_group, path=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if structure_group is not None:
            route_values['structureGroup'] = self._serialize.url('structure_group', structure_group, 'TreeStructureGroup')
        if path is not None:
            route_values['path'] = self._serialize.url('path', path, 'str')
        content = self._serialize.body(posted_node, 'WorkItemClassificationNode')
        response = self._send(http_method='PATCH',
                              location_id='5a172953-1b41-49d3-840a-33f79c3ce89f',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemClassificationNode', response)

    def get_engaged_users(self, project, work_item_id, comment_id, reaction_type, top=None, skip=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if reaction_type is not None:
            route_values['reactionType'] = self._serialize.url('reaction_type', reaction_type, 'CommentReactionType')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='e33ca5e0-2349-4285-af3d-d72d86781c35',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[IdentityRef]', self._unwrap_collection(response))

    def add_comment(self, request, project, work_item_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        content = self._serialize.body(request, 'CommentCreate')
        response = self._send(http_method='POST',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def delete_comment(self, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        self._send(http_method='DELETE',
                   location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                   version='6.0-preview.3',
                   route_values=route_values)

    def get_comment(self, project, work_item_id, comment_id, include_deleted=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        query_parameters = {}
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Comment', response)

    def get_comments(self, project, work_item_id, top=None, continuation_token=None, include_deleted=None, expand=None, order=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if order is not None:
            query_parameters['order'] = self._serialize.query('order', order, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CommentList', response)

    def get_comments_batch(self, project, work_item_id, ids, include_deleted=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('CommentList', response)

    def update_comment(self, request, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        content = self._serialize.body(request, 'CommentUpdate')
        response = self._send(http_method='PATCH',
                              location_id='608aac0a-32e1-4493-a863-b9cf4566d257',
                              version='6.0-preview.3',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Comment', response)

    def create_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if reaction_type is not None:
            route_values['reactionType'] = self._serialize.url('reaction_type', reaction_type, 'CommentReactionType')
        response = self._send(http_method='PUT',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('CommentReaction', response)

    def delete_comment_reaction(self, project, work_item_id, comment_id, reaction_type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if reaction_type is not None:
            route_values['reactionType'] = self._serialize.url('reaction_type', reaction_type, 'CommentReactionType')
        response = self._send(http_method='DELETE',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('CommentReaction', response)

    def get_comment_reactions(self, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='f6cb3f27-1028-4851-af96-887e570dc21f',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[CommentReaction]', self._unwrap_collection(response))

    def get_comment_version(self, project, work_item_id, comment_id, version):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        if version is not None:
            route_values['version'] = self._serialize.url('version', version, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('CommentVersion', response)

    def get_comment_versions(self, project, work_item_id, comment_id):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if work_item_id is not None:
            route_values['workItemId'] = self._serialize.url('work_item_id', work_item_id, 'int')
        if comment_id is not None:
            route_values['commentId'] = self._serialize.url('comment_id', comment_id, 'int')
        response = self._send(http_method='GET',
                              location_id='49e03b34-3be0-42e3-8a5d-e8dfb88ac954',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[CommentVersion]', self._unwrap_collection(response))

    def create_field(self, work_item_field, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_field, 'WorkItemField')
        response = self._send(http_method='POST',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemField', response)

    def delete_field(self, field_name_or_ref_name, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if field_name_or_ref_name is not None:
            route_values['fieldNameOrRefName'] = self._serialize.url('field_name_or_ref_name', field_name_or_ref_name, 'str')
        self._send(http_method='DELETE',
                   location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                   version='6.0-preview.2',
                   route_values=route_values)

    def get_field(self, field_name_or_ref_name, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if field_name_or_ref_name is not None:
            route_values['fieldNameOrRefName'] = self._serialize.url('field_name_or_ref_name', field_name_or_ref_name, 'str')
        response = self._send(http_method='GET',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemField', response)

    def get_fields(self, project=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemField]', self._unwrap_collection(response))

    def update_field(self, payload, field_name_or_ref_name, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if field_name_or_ref_name is not None:
            route_values['fieldNameOrRefName'] = self._serialize.url('field_name_or_ref_name', field_name_or_ref_name, 'str')
        content = self._serialize.body(payload, 'UpdateWorkItemField')
        response = self._send(http_method='PATCH',
                              location_id='b51fd764-e5c2-4b9b-aaf7-3395cf4bdd94',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemField', response)

    def migrate_projects_process(self, new_process, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(new_process, 'ProcessIdModel')
        response = self._send(http_method='POST',
                              location_id='19801631-d4e5-47e9-8166-0330de0ff1e6',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ProcessMigrationResultModel', response)

    def create_query(self, posted_query, project, query, validate_wiql_only=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if validate_wiql_only is not None:
            query_parameters['validateWiqlOnly'] = self._serialize.query('validate_wiql_only', validate_wiql_only, 'bool')
        content = self._serialize.body(posted_query, 'QueryHierarchyItem')
        response = self._send(http_method='POST',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('QueryHierarchyItem', response)

    def delete_query(self, project, query):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        self._send(http_method='DELETE',
                   location_id='a67d190c-c41f-424b-814d-0e906f659301',
                   version='6.0-preview.2',
                   route_values=route_values)

    def get_queries(self, project, expand=None, depth=None, include_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[QueryHierarchyItem]', self._unwrap_collection(response))

    def get_query(self, project, query, expand=None, depth=None, include_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if depth is not None:
            query_parameters['$depth'] = self._serialize.query('depth', depth, 'int')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QueryHierarchyItem', response)

    def search_queries(self, project, filter, top=None, expand=None, include_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if filter is not None:
            query_parameters['$filter'] = self._serialize.query('filter', filter, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if include_deleted is not None:
            query_parameters['$includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('QueryHierarchyItemsResult', response)

    def update_query(self, query_update, project, query, undelete_descendants=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if query is not None:
            route_values['query'] = self._serialize.url('query', query, 'str')
        query_parameters = {}
        if undelete_descendants is not None:
            query_parameters['$undeleteDescendants'] = self._serialize.query('undelete_descendants', undelete_descendants, 'bool')
        content = self._serialize.body(query_update, 'QueryHierarchyItem')
        response = self._send(http_method='PATCH',
                              location_id='a67d190c-c41f-424b-814d-0e906f659301',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('QueryHierarchyItem', response)

    def get_queries_batch(self, query_get_request, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(query_get_request, 'QueryBatchGetRequest')
        response = self._send(http_method='POST',
                              location_id='549816f9-09b0-4e75-9e81-01fbfcd07426',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[QueryHierarchyItem]', self._unwrap_collection(response))

    def destroy_work_item(self, id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        self._send(http_method='DELETE',
                   location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                   version='6.0-preview.2',
                   route_values=route_values)

    def get_deleted_work_item(self, id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemDelete', response)

    def get_deleted_work_items(self, ids, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemDeleteReference]', self._unwrap_collection(response))

    def get_deleted_work_item_shallow_references(self, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemDeleteShallowReference]', self._unwrap_collection(response))

    def restore_work_item(self, payload, id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        content = self._serialize.body(payload, 'WorkItemDeleteUpdate')
        response = self._send(http_method='PATCH',
                              location_id='b70d8d39-926c-465e-b927-b1bf0e5ca0e0',
                              version='6.0-preview.2',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemDelete', response)

    def get_revision(self, id, revision_number, project=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        if revision_number is not None:
            route_values['revisionNumber'] = self._serialize.url('revision_number', revision_number, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='a00c85a5-80fa-4565-99c3-bcd2181434bb',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def get_revisions(self, id, project=None, top=None, skip=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='a00c85a5-80fa-4565-99c3-bcd2181434bb',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def delete_tag(self, project, tag_id_or_name):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if tag_id_or_name is not None:
            route_values['tagIdOrName'] = self._serialize.url('tag_id_or_name', tag_id_or_name, 'str')
        self._send(http_method='DELETE',
                   location_id='bc15bc60-e7a8-43cb-ab01-2106be3983a1',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_tag(self, project, tag_id_or_name):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if tag_id_or_name is not None:
            route_values['tagIdOrName'] = self._serialize.url('tag_id_or_name', tag_id_or_name, 'str')
        response = self._send(http_method='GET',
                              location_id='bc15bc60-e7a8-43cb-ab01-2106be3983a1',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemTagDefinition', response)

    def get_tags(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='bc15bc60-e7a8-43cb-ab01-2106be3983a1',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemTagDefinition]', self._unwrap_collection(response))

    def update_tag(self, tag_data, project, tag_id_or_name):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if tag_id_or_name is not None:
            route_values['tagIdOrName'] = self._serialize.url('tag_id_or_name', tag_id_or_name, 'str')
        content = self._serialize.body(tag_data, 'WorkItemTagDefinition')
        response = self._send(http_method='PATCH',
                              location_id='bc15bc60-e7a8-43cb-ab01-2106be3983a1',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTagDefinition', response)

    def create_template(self, template, team_context):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        content = self._serialize.body(template, 'WorkItemTemplate')
        response = self._send(http_method='POST',
                              location_id='6a90345f-a676-4969-afce-8e163e1d5642',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTemplate', response)

    def get_templates(self, team_context, workitemtypename=None):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if workitemtypename is not None:
            query_parameters['workitemtypename'] = self._serialize.query('workitemtypename', workitemtypename, 'str')
        response = self._send(http_method='GET',
                              location_id='6a90345f-a676-4969-afce-8e163e1d5642',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemTemplateReference]', self._unwrap_collection(response))

    def delete_template(self, team_context, template_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        self._send(http_method='DELETE',
                   location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                   version='6.0-preview.1',
                   route_values=route_values)

    def get_template(self, team_context, template_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        response = self._send(http_method='GET',
                              location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('WorkItemTemplate', response)

    def replace_template(self, template_content, team_context, template_id):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if template_id is not None:
            route_values['templateId'] = self._serialize.url('template_id', template_id, 'str')
        content = self._serialize.body(template_content, 'WorkItemTemplate')
        response = self._send(http_method='PUT',
                              location_id='fb10264a-8836-48a0-8033-1b0ccd2748d5',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('WorkItemTemplate', response)

    def get_update(self, id, update_number, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        if update_number is not None:
            route_values['updateNumber'] = self._serialize.url('update_number', update_number, 'int')
        response = self._send(http_method='GET',
                              location_id='6570bf97-d02c-4a91-8d93-3abe9895b1a9',
                              version='6.0-preview.3',
                              route_values=route_values)
        return self._deserialize('WorkItemUpdate', response)

    def get_updates(self, id, project=None, top=None, skip=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        response = self._send(http_method='GET',
                              location_id='6570bf97-d02c-4a91-8d93-3abe9895b1a9',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemUpdate]', self._unwrap_collection(response))

    def query_by_wiql(self, wiql, team_context=None, time_precision=None, top=None):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        content = self._serialize.body(wiql, 'Wiql')
        response = self._send(http_method='POST',
                              location_id='1a9c53f7-f243-4447-b110-35ef023636e4',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('WorkItemQueryResult', response)

    def get_query_result_count(self, id, team_context=None, time_precision=None, top=None):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='HEAD',
                              location_id='a02355f5-5f8a-4671-8e32-369d23aac83d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('int', response)

    def query_by_id(self, id, team_context=None, time_precision=None, top=None):
        project = None
        team = None
        if team_context is not None:
            if team_context.project_id:
                project = team_context.project_id
            else:
                project = team_context.project
            if team_context.team_id:
                team = team_context.team_id
            else:
                team = team_context.team

        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'string')
        if team is not None:
            route_values['team'] = self._serialize.url('team', team, 'string')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'str')
        query_parameters = {}
        if time_precision is not None:
            query_parameters['timePrecision'] = self._serialize.query('time_precision', time_precision, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='a02355f5-5f8a-4671-8e32-369d23aac83d',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemQueryResult', response)

    def get_work_item_icon_json(self, icon, color=None, v=None):
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemIcon', response)

    def get_work_item_icons(self):
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='6.0-preview.1')
        return self._deserialize('[WorkItemIcon]', self._unwrap_collection(response))

    def get_work_item_icon_svg(self, icon, color=None, v=None, **kwargs):
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='image/svg+xml')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_work_item_icon_xaml(self, icon, color=None, v=None, **kwargs):
        route_values = {}
        if icon is not None:
            route_values['icon'] = self._serialize.url('icon', icon, 'str')
        query_parameters = {}
        if color is not None:
            query_parameters['color'] = self._serialize.query('color', color, 'str')
        if v is not None:
            query_parameters['v'] = self._serialize.query('v', v, 'int')
        response = self._send(http_method='GET',
                              location_id='4e1eb4a5-1970-4228-a682-ec48eb2dca30',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              accept_media_type='image/xaml+xml')
        if "callback" in kwargs:
            callback = kwargs["callback"]
        else:
            callback = None
        return self._client.stream_download(response, callback=callback)

    def get_reporting_links_by_link_type(self, project=None, link_types=None, types=None, continuation_token=None, start_date_time=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if link_types is not None:
            link_types = ",".join(link_types)
            query_parameters['linkTypes'] = self._serialize.query('link_types', link_types, 'str')
        if types is not None:
            types = ",".join(types)
            query_parameters['types'] = self._serialize.query('types', types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        response = self._send(http_method='GET',
                              location_id='b5b5b6d0-0308-40a1-b3f4-b9bb3c66878f',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemLinksBatch', response)

    def get_relation_type(self, relation):
        route_values = {}
        if relation is not None:
            route_values['relation'] = self._serialize.url('relation', relation, 'str')
        response = self._send(http_method='GET',
                              location_id='f5d33bc9-5b49-4a3c-a9bd-f3cd46dd2165',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemRelationType', response)

    def get_relation_types(self):
        response = self._send(http_method='GET',
                              location_id='f5d33bc9-5b49-4a3c-a9bd-f3cd46dd2165',
                              version='6.0-preview.2')
        return self._deserialize('[WorkItemRelationType]', self._unwrap_collection(response))

    def read_reporting_revisions_get(self, project=None, fields=None, types=None, continuation_token=None, start_date_time=None, include_identity_ref=None, include_deleted=None, include_tag_ref=None, include_latest_only=None, expand=None, include_discussion_changes_only=None, max_page_size=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if types is not None:
            types = ",".join(types)
            query_parameters['types'] = self._serialize.query('types', types, 'str')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        if include_identity_ref is not None:
            query_parameters['includeIdentityRef'] = self._serialize.query('include_identity_ref', include_identity_ref, 'bool')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_tag_ref is not None:
            query_parameters['includeTagRef'] = self._serialize.query('include_tag_ref', include_tag_ref, 'bool')
        if include_latest_only is not None:
            query_parameters['includeLatestOnly'] = self._serialize.query('include_latest_only', include_latest_only, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if include_discussion_changes_only is not None:
            query_parameters['includeDiscussionChangesOnly'] = self._serialize.query('include_discussion_changes_only', include_discussion_changes_only, 'bool')
        if max_page_size is not None:
            query_parameters['$maxPageSize'] = self._serialize.query('max_page_size', max_page_size, 'int')
        response = self._send(http_method='GET',
                              location_id='f828fe59-dd87-495d-a17c-7a8d6211ca6c',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def read_reporting_revisions_post(self, filter, project=None, continuation_token=None, start_date_time=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if start_date_time is not None:
            query_parameters['startDateTime'] = self._serialize.query('start_date_time', start_date_time, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(filter, 'ReportingWorkItemRevisionsFilter')
        response = self._send(http_method='POST',
                              location_id='f828fe59-dd87-495d-a17c-7a8d6211ca6c',
                              version='6.0-preview.2',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def read_reporting_discussions(self, project=None, continuation_token=None, max_page_size=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        if max_page_size is not None:
            query_parameters['$maxPageSize'] = self._serialize.query('max_page_size', max_page_size, 'int')
        response = self._send(http_method='GET',
                              location_id='4a644469-90c5-4fcc-9a9f-be0827d369ec',
                              version='6.0-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ReportingWorkItemRevisionsBatch', response)

    def create_work_item(self, document, project, type, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if validate_only is not None:
            query_parameters['validateOnly'] = self._serialize.query('validate_only', validate_only, 'bool')
        if bypass_rules is not None:
            query_parameters['bypassRules'] = self._serialize.query('bypass_rules', bypass_rules, 'bool')
        if suppress_notifications is not None:
            query_parameters['suppressNotifications'] = self._serialize.query('suppress_notifications', suppress_notifications, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='POST',
                              location_id='62d3d110-0047-428c-ad3c-4fe872c91c74',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('WorkItem', response)

    def get_work_item_template(self, project, type, fields=None, as_of=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if fields is not None:
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='62d3d110-0047-428c-ad3c-4fe872c91c74',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def delete_work_item(self, id, project=None, destroy=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if destroy is not None:
            query_parameters['destroy'] = self._serialize.query('destroy', destroy, 'bool')
        response = self._send(http_method='DELETE',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemDelete', response)

    def get_work_item(self, id, project=None, fields=None, as_of=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItem', response)

    def get_work_items(self, ids, project=None, fields=None, as_of=None, expand=None, error_policy=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if fields is not None:
            fields = ",".join(fields)
            query_parameters['fields'] = self._serialize.query('fields', fields, 'str')
        if as_of is not None:
            query_parameters['asOf'] = self._serialize.query('as_of', as_of, 'iso-8601')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        if error_policy is not None:
            query_parameters['errorPolicy'] = self._serialize.query('error_policy', error_policy, 'str')
        response = self._send(http_method='GET',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def update_work_item(self, document, id, project=None, validate_only=None, bypass_rules=None, suppress_notifications=None, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if id is not None:
            route_values['id'] = self._serialize.url('id', id, 'int')
        query_parameters = {}
        if validate_only is not None:
            query_parameters['validateOnly'] = self._serialize.query('validate_only', validate_only, 'bool')
        if bypass_rules is not None:
            query_parameters['bypassRules'] = self._serialize.query('bypass_rules', bypass_rules, 'bool')
        if suppress_notifications is not None:
            query_parameters['suppressNotifications'] = self._serialize.query('suppress_notifications', suppress_notifications, 'bool')
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        content = self._serialize.body(document, '[JsonPatchOperation]')
        response = self._send(http_method='PATCH',
                              location_id='72c7ddf8-2cdc-4f60-90cd-ab71c14a399b',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters,
                              content=content,
                              media_type='application/json-patch+json')
        return self._deserialize('WorkItem', response)

    def get_work_items_batch(self, work_item_get_request, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(work_item_get_request, 'WorkItemBatchGetRequest')
        response = self._send(http_method='POST',
                              location_id='908509b6-4248-4475-a1cd-829139ba419f',
                              version='6.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[WorkItem]', self._unwrap_collection(response))

    def get_work_item_next_states_on_checkin_action(self, ids, action=None):
        query_parameters = {}
        if ids is not None:
            ids = ",".join(map(str, ids))
            query_parameters['ids'] = self._serialize.query('ids', ids, 'str')
        if action is not None:
            query_parameters['action'] = self._serialize.query('action', action, 'str')
        response = self._send(http_method='GET',
                              location_id='afae844b-e2f6-44c2-8053-17b3bb936a40',
                              version='6.0-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemNextStateOnTransition]', self._unwrap_collection(response))

    def get_work_item_type_categories(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='9b9f5734-36c8-415e-ba67-f83b45c31408',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemTypeCategory]', self._unwrap_collection(response))

    def get_work_item_type_category(self, project, category):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if category is not None:
            route_values['category'] = self._serialize.url('category', category, 'str')
        response = self._send(http_method='GET',
                              location_id='9b9f5734-36c8-415e-ba67-f83b45c31408',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemTypeCategory', response)

    def get_work_item_type(self, project, type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7c8d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('WorkItemType', response)

    def get_work_item_types(self, project):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        response = self._send(http_method='GET',
                              location_id='7c8d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='6.0-preview.2',
                              route_values=route_values)
        return self._deserialize('[WorkItemType]', self._unwrap_collection(response))

    def get_work_item_type_fields_with_references(self, project, type, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='bd293ce5-3d25-4192-8e67-e8092e879efb',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[WorkItemTypeFieldWithReferences]', self._unwrap_collection(response))

    def get_work_item_type_field_with_references(self, project, type, field, expand=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        if field is not None:
            route_values['field'] = self._serialize.url('field', field, 'str')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'str')
        response = self._send(http_method='GET',
                              location_id='bd293ce5-3d25-4192-8e67-e8092e879efb',
                              version='6.0-preview.3',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('WorkItemTypeFieldWithReferences', response)

    def get_work_item_type_states(self, project, type):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if type is not None:
            route_values['type'] = self._serialize.url('type', type, 'str')
        response = self._send(http_method='GET',
                              location_id='7c9d7a76-4a09-43e8-b5df-bd792f4ac6aa',
                              version='6.0-preview.1',
                              route_values=route_values)
        return self._deserialize('[WorkItemStateColor]', self._unwrap_collection(response))

