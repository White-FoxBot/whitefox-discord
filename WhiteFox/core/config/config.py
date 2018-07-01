import json


class DiscordConfig(object):

    def __init__(self, client_config):
        self.raw = client_config
        for config in self.raw:
            self.__setattr__(config, self.raw[config])


class FoxConfig(object):

    def __init__(self, fox_config):
        self.raw = fox_config
        for config in self.raw:
            self.__setattr__(config, self.raw[config])


class Config(object):

    def __init__(self):
        self.discord = None
        self.fox = None
        self._get_discord_config()
        self._get_fox_config()

    def _get_discord_config(self):
        try:
            with open("cfg/discord.json") as config_file:
                discord_config = json.load(config_file)
                self.discord = DiscordConfig(discord_config)
        except IOError:
            print("Unable to find 'cfg/discord.json'")

    def _get_fox_config(self):
        try:
            with open("cfg/fox.json") as config_file:
                fox_config = json.load(config_file)
                self.fox = FoxConfig(fox_config)
        except IOError:
            print("Unable to find 'cfg/fox.json'")
