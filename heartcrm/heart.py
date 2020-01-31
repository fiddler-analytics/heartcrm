"""Establishes a connection to HEART CRM via OAUTH2 or username/password/token
and uses that connection to make Salesforce API calls."""
import requests
from simple_salesforce import Salesforce


class HeartCRM(Salesforce):
    def __init__(self, **kwargs):
        self.salesforce = None
        self._try_oauth_connect(**kwargs)
        super().__init__(**kwargs)

    def _try_oauth_connect(self, **kwargs):
        """Attepts to connect to Salesforce using OAUTH2."""
        redirect_uri = kwargs.pop('redirect_uri', None)
        client_id = kwargs.pop('client_id', None)
        client_secret = kwargs.pop('client_secret', None)
        access_code = kwargs.pop('access_code', None)
        sandbox = kwargs.pop('sandbox', False)

        if any([redirect_uri, client_id, client_secret, access_code]):
            if not all([redirect_uri, client_id, client_secret, access_code]):
                raise ValueError('OAUTH2 authentication requires a '
                                 'redirect_uri, a client_id, a client_secret '
                                 'and an access_code.')

            access_token, instance_url = _get_access_token(redirect_uri,
                                                           client_id,
                                                           client_secret,
                                                           access_code,
                                                           sandbox)

            super().__init__(access_token=access_token,
                             instance_url=instance_url)


def _get_access_token(redirect_uri, client_id, client_secret,
                      access_code, sandbox=False):
    """Retrieves an access code from the Salesforce OAUTH2 enpoint.

    Parameters
    ----------
    redirect_uri : str
        the redirect URI that is registered in the Salesforce ConnectedApp
    client_id : str
        the consumer key for the Salesforce ConnectedApp
    client_secret : str
        the consumer secret for the Salesforce ConnectedApp
    access_code : str
        the access code generated in the query parameter of the redirect URI
        after authenticating
    sandbox : bool
        uses test.salesforce.com if True, otherwise uses login.salesforce.com

    Returns
    -------
    access_token : str
        the access token that can be used to make subsequent Salesforce
        API calls
    instance_url : str
        the instance URL for the Salesforce account
    """
    data = {'grant_type': 'authorization_code',
            'redirect_uri': redirect_uri,
            'code': access_code,
            'client_id': client_id,
            'client_secret': client_secret}
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    subdomain = 'test' if sandbox else 'login'
    access_token_url = 'https://{}.salesforce.com/services/oauth2/token'
    access_token_url = access_token_url.format(subdomain)
    req = requests.post(access_token_url, data=data, headers=headers)
    response = req.json()
    return response['access_token'], response['instance_url']
