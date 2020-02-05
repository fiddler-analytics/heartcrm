# Python Client for HEART CRM

## Installation

To install the package through PyPI, simply run

```
pip install heartcrm
```

If you want the latest and greatest, you can install the package by cloning the repo and running:
```
pip install -e .
```

## Configuration

To authenticate with Salesforce, you need the Client ID, Client Secret and Redirect URI for the ConnectedApp in Salesforce. This can be tedious to enter each time. The `.heartrc` file stores these configurations to make them easy to manage. To create a `.heartrc` file, run the following commands from an interactive Python session:

```python
from heartcrm import configure

configure()
```

This will create a `.heartrc` file in the root directory of the `heartcrm` project. When the file is created, the utility will change the permissions of the file so only the user who created it can read, write, and execute it. Please contact your HEART CRM administrator to determine the correct values to inclue in the configuration file.

## Connection

Once your configuration file is setup, you can connect to HEART CRM using the following steps. First, go to [this link](https://salesforce.shirconnect.com) and follow the steps to obtain and OAUTH2 access code. Next, run the following commands in an interaction Python session:

```python
from heartcrm import HeartCRM

heart = HeartCRM(access_code=access_code)
```

If that is successful, you should be able to run `heart.describe()` and get output. The `HeartCRM` object also supports authentication through username/passwork/security token. However, that option is only available to users who have direct access to the Salesforce backend. Most HeartCRM users need to authenticate with the OAUTH2 access code.
