from git import Repo

from commands.ICommand import ICommand
from helpers.logger import logger


class GitClone(ICommand):
    def __init__(self, git_repo: str, dir_path: str):
        self.dir_path = dir_path
        self.git_repo = git_repo

    def execute(self, *args, **kwargs):
        logger.info(f"Cloning {self.git_repo} to {self.dir_path}")
        Repo.clone_from(self.git_repo, self.dir_path)
