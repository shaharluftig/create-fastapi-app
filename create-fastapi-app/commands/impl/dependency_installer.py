import os
from typing import List

import virtualenv

from commands.ICommand import ICommand
from helpers.logger import logger


class DependencyInstaller(ICommand):
    def __init__(self, virtualenv_path: str, packages: List[str]):
        self.packages = packages
        self.virtualenv_path = virtualenv_path

    def execute(self):
        logger.info("Creating virtualenv")
        virtualenv.run.cli_run([f"{self.virtualenv_path}/venv"])
        logger.info("Installing dependencies")
        self.install_deps()

    def install_deps(self):
        path = os.path.abspath(self.virtualenv_path)
        if os.name == "nt":
            os.system(f"{path}\\venv\\Scripts\\python -m pip install --upgrade pip")
            os.system(f"{path}\\venv\\Scripts\\python -m pip install {','.join(map(str, self.packages))}")

        if os.name == "posix":
            os.system(f"{path}\\venv\\bin\\python -m pip install --upgrade pip")
            os.system(f"{path}\\venv\\bin\\python -m pip install {','.join(map(str, self.packages))}")
