"""Cloud storage configuration."""
import os


class StorageConfig:
    AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    AWS_DEFAULT_REGION    = "us-east-1"
    S3_BUCKET: str = os.environ.get('S3_BUCKET', 'my-app-bucket')


def get_storage_config() -> StorageConfig:
    return StorageConfig()
