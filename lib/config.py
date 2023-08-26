import json


class Config:
    def load_config(self):
        with open(self.config_file_path, "r") as file:
            self.config = json.load(file)

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = {}
        self.load_config()

    def save_config(self):
        with open(self.config_file_path, "w") as file:
            json.dump(self.config, file, indent=4)

    def is_player_initialized(self):
        self.load_config()
        return self.config["player_init"] == "True"

    def is_conf_initialized(self):
        self.load_config()
        return self.config["conf_init"] == "true"

    def set_player_initialized(self, initialized):
        self.config["player_init"] = str(initialized)
        self.save_config()

    def set_conf_initialized(self, initialized):
        self.config["conf_init"] = str(initialized)
        self.save_config()

    def get_language(self):
        self.load_config()
        return self.config["settings"]["language"]

    def set_language(self, language):
        self.config["settings"]["language"] = language
        self.save_config()

    def get_allowed_ua(self):
        self.load_config()
        return self.config["server"]["Allowed UA"]

    def get_allowed_ip(self):
        self.load_config()
        return self.config["server"]["Allowed IP"]

    def get_game_path(self, game):
        self.load_config()
        return self.config["game"][game]["path"]

    def set_game_path(self, path, game):
        self.config["game"][game]["path"] = path
        self.save_config()

    def get_game_version(self, game):
        self.load_config()
        return self.config["game"][game]["bg_version"]

    def set_game_version(self, version, game):
        self.config["game"][game]["br_version"] = version
        self.save_config()

    def set_auth_key(self, key):
        self.config["auth"]["key"] = key
        self.save_config()
