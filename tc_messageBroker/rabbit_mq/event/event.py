from .events_microservice import (DiscordAnalyzerEvent, DiscordBotEvent,
                                  ServerEvent)


class Event:
    SERVER_API = ServerEvent
    DISCORD_BOT = DiscordBotEvent
    DISCORD_ANALYZER = DiscordAnalyzerEvent
