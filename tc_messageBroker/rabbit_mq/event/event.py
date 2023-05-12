from .events_microservice import ServerEvent, DiscordBotEvent, DiscordAnalyzerEvent


class Event:
    SERVER_API = ServerEvent
    DISCORD_BOT = DiscordBotEvent
    DISCORD_ANALYZER = DiscordAnalyzerEvent
