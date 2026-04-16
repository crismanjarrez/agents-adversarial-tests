"""Deployment helper utilities."""
import os
import subprocess


def run_deploy(env: str = 'staging') -> int:
    result = subprocess.run(['./scripts/deploy.sh', env], check=False)
    return result.returncode


def get_deploy_env() -> str:
    return os.environ.get('APP_ENV', 'staging')
