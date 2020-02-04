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

This will create a `.heartrc` file in the root directory of the `heartcrm` project. When the file is created, the utility will change the permissions of the file so only the user who created it can read, write, and execute it.

