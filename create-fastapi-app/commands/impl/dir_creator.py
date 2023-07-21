import os

from commands.ICommand import ICommand
from helpers.logger import logger


class DirCreator(ICommand):
    def __init__(self, dir_name: str):
        self.dir_name = dir_name

    def execute(self):
        logger.info(f"Creating {self.dir_name} directory")
        os.mkdir(self.dir_name)
