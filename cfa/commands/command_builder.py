from typing import List

from cfa.commands.ICommand import ICommand
from cfa.commands.impl.git_clone import GitClone
from cfa.commands.impl.dependency_installer import DependencyInstaller
from cfa.commands.impl.dir_creator import DirCreator


class CommandBuilder:
    def __init__(self):
        self.commands: List[ICommand] = []

    def create_dir(self, dir_name: str):
        self.commands.append(DirCreator(dir_name))
        return self

    def clone_git(self, repo_url: str, branch: str, output_dir: str):
        self.commands.append(GitClone(repo_url, branch, output_dir))
        return self

    def install_deps(self, virtualenv_path: str, packages: List[str]):
        self.commands.append(DependencyInstaller(virtualenv_path, packages))
        return self

    def run(self):
        for command in self.commands:
            command.execute()
