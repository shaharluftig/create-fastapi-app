ENV = "prod"


class DefaultConfig:
    base_git_project = "https://github.com/shaharluftig/base-fastapi-project.git"
    pip_packages = ["fastapi", "pytest", "ruff", "cachetools"]


class ProdConfig(DefaultConfig):
    git_branch = "main"


class DevConfig(DefaultConfig):
    git_branch = "develop"


config = ProdConfig if ENV == "prod" else DevConfig
