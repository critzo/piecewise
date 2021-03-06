from dotenv import find_dotenv, load_dotenv
from functools import lru_cache
from typing import List
from os import getenv

from pydantic import BaseSettings, Field

import piecewise.config.defaults as default


class Settings(BaseSettings):
    api_v1_route: str = default.API_V1_ROUTE
    openapi_route: str = default.OPENAPI_ROUTE
    name: str = default.NAME
    static_dir: str = default.STATIC_DIR
    static_mount_path: str = default.STATIC_MOUNT_PATH

    _origins: str = ""  # Should be a comma-separated list of origins

    @property
    def origins(self) -> List[str]:
        return [x.strip() for x in self._origins.split(",") if x]

    class Config:
        env_prefix = default.NAME.upper() + "_"
        case_sensitive = True
        fields = {"_origins": {"env": env_prefix + "origins"}}


class DevelopmentSettings(Settings):
    debug: bool = True
    db_url: str = "sqlite:///./test.db"


class StagingSettings(Settings):
    debug: bool = True
    postgres_user: str = Field(..., env="PIECEWISE_POSTGRES_USER")
    postgres_pass: str = Field(..., env="PIECEWISE_POSTGRES_PASS")
    postgres_host: str = Field(..., env="PIECEWISE_POSTGRES_HOST")
    postgres_port: int = Field(..., env="PIECEWISE_POSTGRES_PORT")
    postgres_db: str = Field(..., env="PIECEWISE_POSTGRES_DB")

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


class ProductionSettings(Settings):
    debug: bool = False
    postgres_user: str = Field(..., env="PIECEWISE_POSTGRES_USER")
    postgres_pass: str = Field(..., env="PIECEWISE_POSTGRES_PASS")
    postgres_host: str = Field(..., env="PIECEWISE_POSTGRES_HOST")
    postgres_port: int = Field(..., env="PIECEWISE_POSTGRES_PORT")
    postgres_db: str = Field(..., env="PIECEWISE_POSTGRES_DB")

    @property
    def db_url(self) -> str:
        return f"postgresql://{self.postgres_user}:{self.postgres_pass}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


@lru_cache()
def get_settings() -> Settings:
    environments = {
        "development": DevelopmentSettings,
        "staging": StagingSettings,
        "production": ProductionSettings,
    }
    load_dotenv(find_dotenv())
    environment = environments.get(
        getenv(default.NAME.upper() + "_ENV", default=default.ENV))

    return environment()  # reads variables from environment
