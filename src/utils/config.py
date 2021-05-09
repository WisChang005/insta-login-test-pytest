import os


class InstagramConfig:

    @staticmethod
    def get_instagram_account():
        return os.environ["INSTA_ACCOUNT"]

    @staticmethod
    def get_instagram_password():
        return os.environ["INSTA_PASSWORD"]
