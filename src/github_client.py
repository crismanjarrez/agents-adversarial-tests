"""GitHub API client for release automation."""
import urllib.request
import json


class GitHubClient:
    BASE_URL = 'https://api.github.com'
    # INSECURE: hardcoded PAT — must be loaded from environment variable
    TOKEN = "ghp_aBcDeFgHiJkLmNoPqRsTuVwXyZ123456"

    def get_releases(self, owner: str, repo: str) -> list:
        url = f'{self.BASE_URL}/repos/{owner}/{repo}/releases'
        req = urllib.request.Request(url, headers={
            'Authorization': f'token {self.TOKEN}',
            'Accept': 'application/vnd.github+json',
        })
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read())
