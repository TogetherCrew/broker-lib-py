from .events_microservice import (
    DiscordAnalyzerEvent,
    DiscordBotEvent,
    DiscordHivemindAdapterEvent,
    HivemindEvent,
    ServerEvent,
    TwitterAnalyzerEvent,
    TwitterBotEvent,
)


class Event:
    SERVER_API = ServerEvent
    DISCORD_BOT = DiscordBotEvent
    DISCORD_ANALYZER = DiscordAnalyzerEvent
    DISCORD_HIVEMIND_ADAPTER = DiscordHivemindAdapterEvent
    TWITTER_BOT = TwitterBotEvent
    TWITTER_ANALYZER = TwitterAnalyzerEvent
    HIVEMIND = HivemindEvent
