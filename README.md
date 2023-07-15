# Monzo Python SDK

## Dependencies

- `Python >= 3.9`

## Quickstart

Make sure you have Python and pip on your machine

To install the package run

`pip install git+https://github.com/owenvoke/monzo-python-sdk`

### Example

Open up a Python terminal (or create a Python file) and enter the following:

```python
from monzo import Monzo # Import Monzo class

client = Monzo('access_token_goes_here') # Replace access token with a valid token found at: https://developers.monzo.com
account_id = client.get_first_account()['id'] # Get the ID of the first account linked to the access token
balance = client.get_balance(account_id) # Get your balance object
print(balance['balance']) # 100000000000
print(balance['currency']) # GBP
print(balance['spend_today']) # 2000
```

Yup. It's that easy. To see what more you can do with the `client` variable, take a look at the [tests](https://github.com/owenvoke/monzo-python/blob/main/tests/test_api_endpoints.py).

### OAuth

The library also supports OAuth. Read the [wiki entry](https://github.com/muyiwaolu/monzo-python/wiki/OAuth) for more information.
