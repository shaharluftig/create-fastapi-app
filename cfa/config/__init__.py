ENV = "dev"


class DefaultConfig:
    base_git_project = "https://github.com/shaharluftig/base-fastapi-project.git"
    pip_packages = ["fastapi"]


class ProdConfig(DefaultConfig):
    git_branch = "master"


class DevConfig(DefaultConfig):
    git_branch = "develop"


config = ProdConfig if ENV == "prod" else DevConfig
