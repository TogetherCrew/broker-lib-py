class BotBaseEvent:
    FETCH = "FETCH"


class AnalyzerBaseEvent:
    RUN = "RUN"
    SAVE = "SAVE"


class ServerEvent:
    UPDATE_GUILD = "UPDATE_GUILD"


class DiscordBotEvent:
    FETCH = BotBaseEvent.FETCH
    SEND_MESSAGE = "SEND_MESSAGE"


class DiscordAnalyzerEvent:
    RUN = AnalyzerBaseEvent.RUN
    SAVE = AnalyzerBaseEvent.SAVE
