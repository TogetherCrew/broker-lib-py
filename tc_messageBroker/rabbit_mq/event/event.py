from .events_microservice import (
    DiscordAnalyzerEvent,
    DiscordBotEvent,
    ServerEvent,
    TwitterAnalyzerEvent,
    TwitterBotEvent,
)


class Event:
    SERVER_API = ServerEvent
    DISCORD_BOT = DiscordBotEvent
    DISCORD_ANALYZER = DiscordAnalyzerEvent
    TWITTER_BOT = TwitterBotEvent
    TWITTER_ANALYZER = TwitterAnalyzerEvent
