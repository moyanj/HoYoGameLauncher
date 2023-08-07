import json


class Config:
    def load_config(self):
        with open(self.config_file_path, 'r') as file:
            self.config = json.load(file)

    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config = None
        self.load_config()

    def save_config(self):
        with open(self.config_file_path, 'w') as file:
            json.dump(self.config, file, indent=4)

    def get_player_uid(self):
        return self.config['player']['uid']

    def set_player_uid(self, uid):
        self.config['player']['uid'] = uid
        self.save_config()

    def get_player_username(self):
        return self.config['player']['username']

    def set_player_username(self, username):
        self.config['player']['username'] = username
        self.save_config()

    def is_player_initialized(self):
        return self.config['player']['init'] == 'true'

    def set_player_initialized(self, initialized):
        self.config['player']['init'] = 'true' if initialized else 'false'
        self.save_config()

    def is_debug_enabled(self):
        return self.config['settings']['debug'] == 'true'

    def get_server_port(self):
        return int(self.config['server']['port'])

    def get_allowed_ua(self):
        return self.config['server']['Allowed UA']

    def get_allowed_ip(self):
        return self.config['server']['Allowed IP']

    def get_game_path(self, game):
        return self.config['game'][game]['path']

    def set_game_path(self, path, game):
        self.config['game'][game]['path'] = path
        self.save_config()
