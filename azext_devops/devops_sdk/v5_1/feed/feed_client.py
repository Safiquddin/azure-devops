﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class FeedClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(FeedClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = '7ab4e64e-c4d8-4f50-ae73-5ef2e21642a5'

    def get_badge(self, feed_id, package_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        response = self._send(http_method='GET',
                              location_id='61d885fd-10f3-4a55-82b6-476d866b673f',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('str', response)

    def get_feed_change(self, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='29ba2dad-389a-4661-b5d3-de76397ca05b',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedChange', response)

    def get_feed_changes(self, project=None, include_deleted=None, continuation_token=None, batch_size=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'long')
        if batch_size is not None:
            query_parameters['batchSize'] = self._serialize.query('batch_size', batch_size, 'int')
        response = self._send(http_method='GET',
                              location_id='29ba2dad-389a-4661-b5d3-de76397ca05b',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('FeedChangesResponse', response)

    def create_feed(self, feed, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(feed, 'Feed')
        response = self._send(http_method='POST',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Feed', response)

    def delete_feed(self, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        self._send(http_method='DELETE',
                   location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed(self, feed_id, project=None, include_deleted_upstreams=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if include_deleted_upstreams is not None:
            query_parameters['includeDeletedUpstreams'] = self._serialize.query('include_deleted_upstreams', include_deleted_upstreams, 'bool')
        response = self._send(http_method='GET',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Feed', response)

    def get_feeds(self, project=None, feed_role=None, include_deleted_upstreams=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if feed_role is not None:
            query_parameters['feedRole'] = self._serialize.query('feed_role', feed_role, 'str')
        if include_deleted_upstreams is not None:
            query_parameters['includeDeletedUpstreams'] = self._serialize.query('include_deleted_upstreams', include_deleted_upstreams, 'bool')
        response = self._send(http_method='GET',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Feed]', self._unwrap_collection(response))

    def update_feed(self, feed, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(feed, 'FeedUpdate')
        response = self._send(http_method='PATCH',
                              location_id='c65009a7-474a-4ad1-8b42-7d852107ef8c',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Feed', response)

    def get_global_permissions(self, include_ids=None):
        query_parameters = {}
        if include_ids is not None:
            query_parameters['includeIds'] = self._serialize.query('include_ids', include_ids, 'bool')
        response = self._send(http_method='GET',
                              location_id='a74419ef-b477-43df-8758-3cd1cd5f56c6',
                              version='5.1-preview.1',
                              query_parameters=query_parameters)
        return self._deserialize('[GlobalPermission]', self._unwrap_collection(response))

    def set_global_permissions(self, global_permissions):
        content = self._serialize.body(global_permissions, '[GlobalPermission]')
        response = self._send(http_method='PATCH',
                              location_id='a74419ef-b477-43df-8758-3cd1cd5f56c6',
                              version='5.1-preview.1',
                              content=content)
        return self._deserialize('[GlobalPermission]', self._unwrap_collection(response))

    def get_package_changes(self, feed_id, project=None, continuation_token=None, batch_size=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'long')
        if batch_size is not None:
            query_parameters['batchSize'] = self._serialize.query('batch_size', batch_size, 'int')
        response = self._send(http_method='GET',
                              location_id='323a0631-d083-4005-85ae-035114dfb681',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PackageChangesResponse', response)

    def query_package_metrics(self, package_id_query, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(package_id_query, 'PackageMetricsQuery')
        response = self._send(http_method='POST',
                              location_id='bddc9b3c-8a59-4a9f-9b40-ee1dcaa2cc0d',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[PackageMetrics]', self._unwrap_collection(response))

    def get_package(self, feed_id, package_id, project=None, include_all_versions=None, include_urls=None, is_listed=None, is_release=None, include_deleted=None, include_description=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_release is not None:
            query_parameters['isRelease'] = self._serialize.query('is_release', is_release, 'bool')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if include_description is not None:
            query_parameters['includeDescription'] = self._serialize.query('include_description', include_description, 'bool')
        response = self._send(http_method='GET',
                              location_id='7a20d846-c929-4acc-9ea2-0d5a7df1b197',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def get_packages(self, feed_id, project=None, protocol_type=None, package_name_query=None, normalized_package_name=None, include_urls=None, include_all_versions=None, is_listed=None, get_top_package_versions=None, is_release=None, include_description=None, top=None, skip=None, include_deleted=None, is_cached=None, direct_upstream_id=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if protocol_type is not None:
            query_parameters['protocolType'] = self._serialize.query('protocol_type', protocol_type, 'str')
        if package_name_query is not None:
            query_parameters['packageNameQuery'] = self._serialize.query('package_name_query', package_name_query, 'str')
        if normalized_package_name is not None:
            query_parameters['normalizedPackageName'] = self._serialize.query('normalized_package_name', normalized_package_name, 'str')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if get_top_package_versions is not None:
            query_parameters['getTopPackageVersions'] = self._serialize.query('get_top_package_versions', get_top_package_versions, 'bool')
        if is_release is not None:
            query_parameters['isRelease'] = self._serialize.query('is_release', is_release, 'bool')
        if include_description is not None:
            query_parameters['includeDescription'] = self._serialize.query('include_description', include_description, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if include_deleted is not None:
            query_parameters['includeDeleted'] = self._serialize.query('include_deleted', include_deleted, 'bool')
        if is_cached is not None:
            query_parameters['isCached'] = self._serialize.query('is_cached', is_cached, 'bool')
        if direct_upstream_id is not None:
            query_parameters['directUpstreamId'] = self._serialize.query('direct_upstream_id', direct_upstream_id, 'str')
        response = self._send(http_method='GET',
                              location_id='7a20d846-c929-4acc-9ea2-0d5a7df1b197',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Package]', self._unwrap_collection(response))

    def get_feed_permissions(self, feed_id, project=None, include_ids=None, exclude_inherited_permissions=None, identity_descriptor=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if include_ids is not None:
            query_parameters['includeIds'] = self._serialize.query('include_ids', include_ids, 'bool')
        if exclude_inherited_permissions is not None:
            query_parameters['excludeInheritedPermissions'] = self._serialize.query('exclude_inherited_permissions', exclude_inherited_permissions, 'bool')
        if identity_descriptor is not None:
            query_parameters['identityDescriptor'] = self._serialize.query('identity_descriptor', identity_descriptor, 'str')
        response = self._send(http_method='GET',
                              location_id='be8c1476-86a7-44ed-b19d-aec0e9275cd8',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[FeedPermission]', self._unwrap_collection(response))

    def set_feed_permissions(self, feed_permission, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(feed_permission, '[FeedPermission]')
        response = self._send(http_method='PATCH',
                              location_id='be8c1476-86a7-44ed-b19d-aec0e9275cd8',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[FeedPermission]', self._unwrap_collection(response))

    def get_package_version_provenance(self, feed_id, package_id, package_version_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        response = self._send(http_method='GET',
                              location_id='0aaeabd4-85cd-4686-8a77-8d31c15690b8',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('PackageVersionProvenance', response)

    def get_recycle_bin_package(self, feed_id, package_id, project=None, include_urls=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='2704e72c-f541-4141-99be-2004b50b05fa',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Package', response)

    def get_recycle_bin_packages(self, feed_id, project=None, protocol_type=None, package_name_query=None, include_urls=None, top=None, skip=None, include_all_versions=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        query_parameters = {}
        if protocol_type is not None:
            query_parameters['protocolType'] = self._serialize.query('protocol_type', protocol_type, 'str')
        if package_name_query is not None:
            query_parameters['packageNameQuery'] = self._serialize.query('package_name_query', package_name_query, 'str')
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if include_all_versions is not None:
            query_parameters['includeAllVersions'] = self._serialize.query('include_all_versions', include_all_versions, 'bool')
        response = self._send(http_method='GET',
                              location_id='2704e72c-f541-4141-99be-2004b50b05fa',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Package]', self._unwrap_collection(response))

    def get_recycle_bin_package_version(self, feed_id, package_id, package_version_id, project=None, include_urls=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='aceb4be7-8737-4820-834c-4c549e10fdc7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('RecycleBinPackageVersion', response)

    def get_recycle_bin_package_versions(self, feed_id, package_id, project=None, include_urls=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        response = self._send(http_method='GET',
                              location_id='aceb4be7-8737-4820-834c-4c549e10fdc7',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[RecycleBinPackageVersion]', self._unwrap_collection(response))

    def delete_feed_retention_policies(self, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        self._send(http_method='DELETE',
                   location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed_retention_policies(self, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedRetentionPolicy', response)

    def set_feed_retention_policies(self, policy, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(policy, 'FeedRetentionPolicy')
        response = self._send(http_method='PUT',
                              location_id='ed52a011-0112-45b5-9f9e-e14efffb3193',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedRetentionPolicy', response)

    def query_package_version_metrics(self, package_version_id_query, feed_id, package_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        content = self._serialize.body(package_version_id_query, 'PackageVersionMetricsQuery')
        response = self._send(http_method='POST',
                              location_id='e6ae8caa-b6a8-4809-b840-91b2a42c19ad',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[PackageVersionMetrics]', self._unwrap_collection(response))

    def get_package_version(self, feed_id, package_id, package_version_id, project=None, include_urls=None, is_listed=None, is_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        if package_version_id is not None:
            route_values['packageVersionId'] = self._serialize.url('package_version_id', package_version_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='3b331909-6a86-44cc-b9ec-c1834c35498f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('PackageVersion', response)

    def get_package_versions(self, feed_id, package_id, project=None, include_urls=None, is_listed=None, is_deleted=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if package_id is not None:
            route_values['packageId'] = self._serialize.url('package_id', package_id, 'str')
        query_parameters = {}
        if include_urls is not None:
            query_parameters['includeUrls'] = self._serialize.query('include_urls', include_urls, 'bool')
        if is_listed is not None:
            query_parameters['isListed'] = self._serialize.query('is_listed', is_listed, 'bool')
        if is_deleted is not None:
            query_parameters['isDeleted'] = self._serialize.query('is_deleted', is_deleted, 'bool')
        response = self._send(http_method='GET',
                              location_id='3b331909-6a86-44cc-b9ec-c1834c35498f',
                              version='5.1-preview.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[PackageVersion]', self._unwrap_collection(response))

    def create_feed_view(self, view, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        content = self._serialize.body(view, 'FeedView')
        response = self._send(http_method='POST',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedView', response)

    def delete_feed_view(self, feed_id, view_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        self._send(http_method='DELETE',
                   location_id='42a8502a-6785-41bc-8c16-89477d930877',
                   version='5.1-preview.1',
                   route_values=route_values)

    def get_feed_view(self, feed_id, view_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        response = self._send(http_method='GET',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('FeedView', response)

    def get_feed_views(self, feed_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        response = self._send(http_method='GET',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values)
        return self._deserialize('[FeedView]', self._unwrap_collection(response))

    def update_feed_view(self, view, feed_id, view_id, project=None):
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if feed_id is not None:
            route_values['feedId'] = self._serialize.url('feed_id', feed_id, 'str')
        if view_id is not None:
            route_values['viewId'] = self._serialize.url('view_id', view_id, 'str')
        content = self._serialize.body(view, 'FeedView')
        response = self._send(http_method='PATCH',
                              location_id='42a8502a-6785-41bc-8c16-89477d930877',
                              version='5.1-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('FeedView', response)

