from unittest import TestCase

from tc_messageBroker.utils.credentials import load_mongo_credentials


class TestCredentialsLoading(TestCase):
    def test_non_none_values(self):
        creds = load_mongo_credentials()
        self.assertIsNotNone(creds["user"])
        self.assertIsNotNone(creds["password"])
        self.assertIsNotNone(creds["host"])
        self.assertIsNotNone(creds["port"])
        self.assertNotEqual(creds["connection_str"], "mongodb://None:None@None:None")
