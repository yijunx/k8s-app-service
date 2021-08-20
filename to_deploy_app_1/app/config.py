import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    COLOR: str
    DOMAIN_NAME: str


class ProductionConfig(Settings):
    # it means that, every entry for Settings must
    # come from environment variables
    pass


class DevelopmentConfig(Settings):
    class Config:
        env_file = "./config/dev.env"


def _find_which_config():

    if os.getenv("DOMAIN_NAME"):  # there is DOMAIN name provided
        config = ProductionConfig()
    else:
        config = DevelopmentConfig()

    def func() -> Settings:
        return config

    return func()


configurations = _find_which_config()


if __name__ == "__main__":
    print(configurations)

