import sys
import os

from dotenv import load_dotenv
from github import Github

load_dotenv()


def create_project(project_name):
    access_token = os.getenv("ACCESSTOKEN")
    g = Github(access_token)
    g_user = g.get_user()
    print("Logged in as {}".format(g_user.name))
    g_repo = g_user.create_repo(project_name)
    print("Created repository: {}".format(project_name))


if __name__ == "__main__":
    try:
        project_name = sys.args[1]
        create_project(project_name)
    except:
        print("A problem occured while creating new project...")
