from pathlib import Path

class ConfigurationService():
    def __init__(self):
        p = Path(Path.cwd(), "data")
        p.mkdir(parents=True, exist_ok=True)
        
        self.__db_path = p.joinpath("users.db")

    def get_connection_string(self):
        return self.__db_path