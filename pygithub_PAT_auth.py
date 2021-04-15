import requests, jwt, cryptography, time
import config
from github import Github
import os
import base64
from github import BadCredentialsException
from github import GithubIntegration


g = Github(base_url=config.GITHUB_BASE_URL, login_or_token=config.PAT)

while True:
    git_repo = g.get_repo('chrislee18a/pygithub_githubapp')
    print(list(git_repo.get_branches()))
    time.sleep(3 * 60) # 3 mins