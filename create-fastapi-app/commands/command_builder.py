from typing import List

from commands.ICommand import ICommand
from commands.impl.dir_creator import DirCreator


class CommandBuilder:
    def __init__(self):
        self.commands: List[ICommand] = []

    def create_dir(self, dir_name: str):
        self.commands.append(DirCreator(dir_name))
        return self

    def run(self):
        for command in self.commands:
            command.execute()
