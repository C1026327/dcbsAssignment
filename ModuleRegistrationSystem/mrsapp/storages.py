from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = "c1026327storaccount"
    account_key = "/0UyyqUeK3JKTZKASW/bp2HjnA9INX1nnYTqZnF4XLOVpCNRJErIeOKjpQF6zu+eqQxi2KfelvwM+AStXE966Q=="
    azure_container = "media"
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = "c1026327storaccount"
    account_key = "/0UyyqUeK3JKTZKASW/bp2HjnA9INX1nnYTqZnF4XLOVpCNRJErIeOKjpQF6zu+eqQxi2KfelvwM+AStXE966Q=="
    azure_container = "static"
    expiration_secs = None
