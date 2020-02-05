from unittest.mock import patch

import pytest
import requests
from simple_salesforce import Salesforce

from heartcrm import HeartCRM


class MockResponse:
    @staticmethod
    def json():
        return {'access_token': 'sun', 'instance_url': 'conure'}


def test_connection_username_password_connects():
    with patch.object(Salesforce, '__init__', return_value=None):
        HeartCRM(username='jabber',
                 password='parrot',
                 security_token='squawk')


def test_connection_raises_without_password():
    with pytest.raises(ValueError):
        HeartCRM(username='jabber', security_token='squawk')


def test_connection_oauth_connects(monkeypatch):
    def mock_post(*args, **kwargs):
        return MockResponse()
    monkeypatch.setattr(requests, 'post', mock_post)

    with patch.object(Salesforce, '__init__', return_value=None):
        HeartCRM(redirect_uri='https://parrots.io',
                 client_id='jabber',
                 client_secret='parrot',
                 access_code='squawk')


def test_connection_raises_without_access_code():
    with pytest.raises(ValueError):
        HeartCRM(redirect_uri='https://parrots.io',
                 client_id='jabber',
                 client_secret='parrot')
