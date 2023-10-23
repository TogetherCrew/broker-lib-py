class BotBaseEvent:
    FETCH = "FETCH"


class AnalyzerBaseEvent:
    RUN = "RUN"
    SAVE = "SAVE"
    RUN_ONCE = "RUN_ONCE"


class ServerEvent:
    UPDATE_GUILD = "UPDATE_GUILD"


class DiscordBotInteractionResponseEvent:
    CREATE = "INTERACTION_RESPONSE_CREATE"
    EDIT = "INTERACTION_RESPONSE_EDIT"
    DELETE = "INTERACTION_RESPONSE_DELETE"


class DiscordBotFollowUp:
    CREATE = "FOLLOWUP_CREATE"


class DiscordBotEvent:
    FETCH = BotBaseEvent.FETCH
    SEND_MESSAGE = "SEND_MESSAGE"
    FETCH_MEMBERS = "FETCH_MEMBERS"
    UPDATE_INTERACTION = "UPDATE_INTERACTION"
    INTERACTION_RESPONSE = DiscordBotInteractionResponseEvent
    FOLLOWUP_MESSAGE = DiscordBotFollowUp


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


class HivemindEvent:
    INTERACTION_CREATED = "INTERACTION_CREATED"
    GUILD_MESSAGES_UPDATED = "GUILD_MESSAGES_UPDATED"
