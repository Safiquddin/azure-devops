﻿# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from . import models


class ServiceHooksClient(Client):

    def __init__(self, base_url=None, creds=None):
        super(ServiceHooksClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = None

    def get_consumer_action(self, consumer_id, consumer_action_id, publisher_id=None):
        route_values = {}
        if consumer_id is not None:
            route_values['consumerId'] = self._serialize.url('consumer_id', consumer_id, 'str')
        if consumer_action_id is not None:
            route_values['consumerActionId'] = self._serialize.url('consumer_action_id', consumer_action_id, 'str')
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='c3428e90-7a69-4194-8ed8-0f153185ee0d',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('ConsumerAction', response)

    def list_consumer_actions(self, consumer_id, publisher_id=None):
        route_values = {}
        if consumer_id is not None:
            route_values['consumerId'] = self._serialize.url('consumer_id', consumer_id, 'str')
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='c3428e90-7a69-4194-8ed8-0f153185ee0d',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[ConsumerAction]', self._unwrap_collection(response))

    def get_consumer(self, consumer_id, publisher_id=None):
        route_values = {}
        if consumer_id is not None:
            route_values['consumerId'] = self._serialize.url('consumer_id', consumer_id, 'str')
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='4301c514-5f34-4f5d-a145-f0ea7b5b7d19',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('Consumer', response)

    def list_consumers(self, publisher_id=None):
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='4301c514-5f34-4f5d-a145-f0ea7b5b7d19',
                              version='5.0',
                              query_parameters=query_parameters)
        return self._deserialize('[Consumer]', self._unwrap_collection(response))

    def get_subscription_diagnostics(self, subscription_id):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        response = self._send(http_method='GET',
                              location_id='3b36bcb5-02ad-43c6-bbfa-6dfc6f8e9d68',
                              version='5.0-preview.1',
                              route_values=route_values)
        return self._deserialize('SubscriptionDiagnostics', response)

    def update_subscription_diagnostics(self, update_parameters, subscription_id):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        content = self._serialize.body(update_parameters, 'UpdateSubscripitonDiagnosticsParameters')
        response = self._send(http_method='PUT',
                              location_id='3b36bcb5-02ad-43c6-bbfa-6dfc6f8e9d68',
                              version='5.0-preview.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('SubscriptionDiagnostics', response)

    def get_event_type(self, publisher_id, event_type_id):
        route_values = {}
        if publisher_id is not None:
            route_values['publisherId'] = self._serialize.url('publisher_id', publisher_id, 'str')
        if event_type_id is not None:
            route_values['eventTypeId'] = self._serialize.url('event_type_id', event_type_id, 'str')
        response = self._send(http_method='GET',
                              location_id='db4777cd-8e08-4a84-8ba3-c974ea033718',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('EventTypeDescriptor', response)

    def list_event_types(self, publisher_id):
        route_values = {}
        if publisher_id is not None:
            route_values['publisherId'] = self._serialize.url('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='db4777cd-8e08-4a84-8ba3-c974ea033718',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('[EventTypeDescriptor]', self._unwrap_collection(response))

    def get_notification(self, subscription_id, notification_id):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        if notification_id is not None:
            route_values['notificationId'] = self._serialize.url('notification_id', notification_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0c62d343-21b0-4732-997b-017fde84dc28',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('Notification', response)

    def get_notifications(self, subscription_id, max_results=None, status=None, result=None):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        query_parameters = {}
        if max_results is not None:
            query_parameters['maxResults'] = self._serialize.query('max_results', max_results, 'int')
        if status is not None:
            query_parameters['status'] = self._serialize.query('status', status, 'str')
        if result is not None:
            query_parameters['result'] = self._serialize.query('result', result, 'str')
        response = self._send(http_method='GET',
                              location_id='0c62d343-21b0-4732-997b-017fde84dc28',
                              version='5.0',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[Notification]', self._unwrap_collection(response))

    def query_notifications(self, query):
        content = self._serialize.body(query, 'NotificationsQuery')
        response = self._send(http_method='POST',
                              location_id='1a57562f-160a-4b5c-9185-905e95b39d36',
                              version='5.0',
                              content=content)
        return self._deserialize('NotificationsQuery', response)

    def query_input_values(self, input_values_query, publisher_id):
        route_values = {}
        if publisher_id is not None:
            route_values['publisherId'] = self._serialize.url('publisher_id', publisher_id, 'str')
        content = self._serialize.body(input_values_query, 'InputValuesQuery')
        response = self._send(http_method='POST',
                              location_id='d815d352-a566-4dc1-a3e3-fd245acf688c',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('InputValuesQuery', response)

    def get_publisher(self, publisher_id):
        route_values = {}
        if publisher_id is not None:
            route_values['publisherId'] = self._serialize.url('publisher_id', publisher_id, 'str')
        response = self._send(http_method='GET',
                              location_id='1e83a210-5b53-43bc-90f0-d476a4e5d731',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('Publisher', response)

    def list_publishers(self):
        response = self._send(http_method='GET',
                              location_id='1e83a210-5b53-43bc-90f0-d476a4e5d731',
                              version='5.0')
        return self._deserialize('[Publisher]', self._unwrap_collection(response))

    def query_publishers(self, query):
        content = self._serialize.body(query, 'PublishersQuery')
        response = self._send(http_method='POST',
                              location_id='99b44a8a-65a8-4670-8f3e-e7f7842cce64',
                              version='5.0',
                              content=content)
        return self._deserialize('PublishersQuery', response)

    def create_subscription(self, subscription):
        content = self._serialize.body(subscription, 'Subscription')
        response = self._send(http_method='POST',
                              location_id='fc50d02a-849f-41fb-8af1-0a5216103269',
                              version='5.0',
                              content=content)
        return self._deserialize('Subscription', response)

    def delete_subscription(self, subscription_id):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        self._send(http_method='DELETE',
                   location_id='fc50d02a-849f-41fb-8af1-0a5216103269',
                   version='5.0',
                   route_values=route_values)

    def get_subscription(self, subscription_id):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        response = self._send(http_method='GET',
                              location_id='fc50d02a-849f-41fb-8af1-0a5216103269',
                              version='5.0',
                              route_values=route_values)
        return self._deserialize('Subscription', response)

    def list_subscriptions(self, publisher_id=None, event_type=None, consumer_id=None, consumer_action_id=None):
        query_parameters = {}
        if publisher_id is not None:
            query_parameters['publisherId'] = self._serialize.query('publisher_id', publisher_id, 'str')
        if event_type is not None:
            query_parameters['eventType'] = self._serialize.query('event_type', event_type, 'str')
        if consumer_id is not None:
            query_parameters['consumerId'] = self._serialize.query('consumer_id', consumer_id, 'str')
        if consumer_action_id is not None:
            query_parameters['consumerActionId'] = self._serialize.query('consumer_action_id', consumer_action_id, 'str')
        response = self._send(http_method='GET',
                              location_id='fc50d02a-849f-41fb-8af1-0a5216103269',
                              version='5.0',
                              query_parameters=query_parameters)
        return self._deserialize('[Subscription]', self._unwrap_collection(response))

    def replace_subscription(self, subscription, subscription_id=None):
        route_values = {}
        if subscription_id is not None:
            route_values['subscriptionId'] = self._serialize.url('subscription_id', subscription_id, 'str')
        content = self._serialize.body(subscription, 'Subscription')
        response = self._send(http_method='PUT',
                              location_id='fc50d02a-849f-41fb-8af1-0a5216103269',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('Subscription', response)

    def create_subscriptions_query(self, query):
        content = self._serialize.body(query, 'SubscriptionsQuery')
        response = self._send(http_method='POST',
                              location_id='c7c3c1cf-9e05-4c0d-a425-a0f922c2c6ed',
                              version='5.0',
                              content=content)
        return self._deserialize('SubscriptionsQuery', response)

    def create_test_notification(self, test_notification, use_real_data=None):
        query_parameters = {}
        if use_real_data is not None:
            query_parameters['useRealData'] = self._serialize.query('use_real_data', use_real_data, 'bool')
        content = self._serialize.body(test_notification, 'Notification')
        response = self._send(http_method='POST',
                              location_id='1139462c-7e27-4524-a997-31b9b73551fe',
                              version='5.0',
                              query_parameters=query_parameters,
                              content=content)
        return self._deserialize('Notification', response)

