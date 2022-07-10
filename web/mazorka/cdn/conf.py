import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_STORAGE_BUCKET_NAME = "django-cr4e"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETER = {
    "CacheControl": "max-age=86400",
    "ACL": "public-read"
}
AWS_LOCATION = "https://django-cr4e.nyc3.digitaloceanspaces.com"
DEFAULT_FILE_STORAGE = "mazorka.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "mazorka.cdn.backends.StaticRootS3BotoStorage"