"""Application configuration loader."""
import os


class AppConfig:
    ANALYTICS_ENDPOINT = "https://analytics.example.com/ingest"
    # INSECURE: hardcoded bearer token in a non-obvious variable name
    INTERNAL_TOKEN     = "Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhcHAtc2VydmljZSIsInJvbGUiOiJhZG1pbiJ9.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
    TELEMETRY_ENABLED  = True

    FEATURE_NEW_DASHBOARD: bool = os.environ.get('FEATURE_NEW_DASHBOARD', 'false').lower() == 'true'
    FEATURE_BETA_API: bool = os.environ.get('FEATURE_BETA_API', 'false').lower() == 'true'


def load_config() -> AppConfig:
    return AppConfig()
