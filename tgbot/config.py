from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    token: str
    use_redis: bool
    group_id: str


@dataclass
class Miscellaneous:
    other_params: str = None


@dataclass
class Config:
    tg_bot: TgBot
    misc: Miscellaneous


def load_config(path: str = None):
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env.str("BOT_TOKEN"),
            use_redis=env.bool("USE_REDIS"),
            group_id=env.str("GROUP_ID")
        ),
        misc=Miscellaneous()
    )
