class BotBaseEvent:
    FETCH = "FETCH"


class AnalyzerBaseEvent:
    RUN = "RUN"
    SAVE = "SAVE"
    RUN_ONCE = "RUN_ONCE"


class ServerEvent:
    UPDATE_GUILD = "UPDATE_GUILD"


class DiscordBotEvent:
    FETCH = BotBaseEvent.FETCH
    SEND_MESSAGE = "SEND_MESSAGE"


class DiscordAnalyzerEvent:
    RUN = AnalyzerBaseEvent.RUN  ## RECOMPUTE
    RUN_ONCE = AnalyzerBaseEvent.RUN_ONCE
    # SAVE = AnalyzerBaseEvent.SAVE
