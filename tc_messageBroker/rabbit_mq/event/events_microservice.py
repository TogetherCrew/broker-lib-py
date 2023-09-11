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
    FETCH_MEMBERS = "FETCH_MEMBERS"


class DiscordAnalyzerEvent:
    RUN = AnalyzerBaseEvent.RUN  # RECOMPUTE
    RUN_ONCE = AnalyzerBaseEvent.RUN_ONCE
    # SAVE = AnalyzerBaseEvent.SAVE


class EXTRACT:
    """
    breaking down twitter extraction process
    """

    TWEETS = "EXTRACT_TWEETS"
    LIKES = "EXTRACT_LIKES"
    PROFILES = "EXTRACT_PROFILES"


class TwitterBotEvent:
    EXTRACT = EXTRACT
    SEND_MESSAGE = "SEND_MESSAGE"


class TwitterAnalyzerEvent:
    RUN = AnalyzerBaseEvent.RUN  # RECOMPUTE
