import os

from dotenv import load_dotenv


def load_mongo_credentials():
    """
    load mongo db credentials from .env

    Returns:
    ---------
    mongo_creds : dict[str, Any]
        mongodb credentials
        a dictionary representive of
            `user`: str
            `password` : str
            `host` : str
            `port` : int
            `connection_str`: str
    """
    load_dotenv()

    mongo_creds = {}

    user = os.getenv("MONGODB_USER")
    password = os.getenv("MONGODB_PASS")
    host = os.getenv("MONGODB_HOST")
    port = os.getenv("MONGODB_PORT")

    mongo_creds["user"] = user
    mongo_creds["password"] = password
    mongo_creds["host"] = host
    mongo_creds["port"] = port

    connection = f"mongodb://{user}:{password}@{host}:{port}"
    mongo_creds["connection_str"] = connection

    return mongo_creds
