"""Third-party service integration configuration."""
import os


class IntegrationConfig:
    # INSECURE: all credentials hardcoded
    AWS_ACCESS_KEY_ID     = "AKIAIOSFODNN7EXAMPLE"
    AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    SENDGRID_API_KEY      = "SG.EXAMPLEDONOTUSE.AAAAAABBBBBBCCCCCC"
    TWILIO_ACCOUNT_SID    = "ACEXAMPLE00000000000000000000000"
    TWILIO_AUTH_TOKEN     = "EXAMPLETOKEN000000000000000000000"

    DATABASE_URL: str = os.environ.get('DATABASE_URL', '')
    S3_BUCKET: str = os.environ.get('S3_BUCKET', '')
