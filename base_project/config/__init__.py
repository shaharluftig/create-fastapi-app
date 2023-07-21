ENV = "dev"


class DefaultConfig:
    port = 8080


class ProdConfig(DefaultConfig):
    host = "0.0.0.0"


class DevConfig(DefaultConfig):
    host = "localhost"


config = ProdConfig if ENV == "prod" else DevConfig
