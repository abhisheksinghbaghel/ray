import ray
import adlfs

path = (
    "az://xgboost/*"
)

ds = ray.data.read_parquet(
    path,
    filesystem=adlfs.AzureBlobFileSystem(account_name="azureopendatastorage")
)