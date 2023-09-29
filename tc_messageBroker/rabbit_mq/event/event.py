from .events_microservice import (
    DiscordAnalyzerEvent,
    DiscordBotEvent,
    ServerEvent,
    TwitterAnalyzerEvent,
    TwitterBotEvent,
    HivemindEvent,
)


class Event:
    SERVER_API = ServerEvent
    DISCORD_BOT = DiscordBotEvent
    DISCORD_ANALYZER = DiscordAnalyzerEvent
    TWITTER_BOT = TwitterBotEvent
    TWITTER_ANALYZER = TwitterAnalyzerEvent
    HIVEMIND = HivemindEvent
