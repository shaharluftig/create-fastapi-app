from git import Repo

from cfa.commands.ICommand import ICommand
from cfa.helpers.logger import logger


class GitClone(ICommand):
    def __init__(self, repo_url: str, branch: str, dir_path: str):
        self.branch = branch
        self.dir_path = dir_path
        self.repo_url = repo_url

    def execute(self, *args, **kwargs):
        logger.info(f"Cloning {self.repo_url} to {self.dir_path}")
        Repo.clone_from(
            self.repo_url,
            to_path=f"./{self.dir_path}/",
            branch=self.branch
        )
