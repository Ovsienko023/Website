import sys


def get_config():
    if sys.platform == "win32":
        config = {
            "db": {"host": "localhost", "port": 5432, "dbname": "website", "username": "postgres", "password": "",
                   "charset": "utf8"},
            "dirs": {"logsdir": "C:\\ProgramData\\website"},
            "webapi": {"port": 8888}
        }
    else:
        config = {
            "db": {"host": "localhost", "port": 5433, "dbname": "website", "username": "postgres", "password": "",
                   "charset": "utf8"},
            "dirs": {"logsdir": "/var/website"},
            "webapi": {"port": 8888}
        }

    return config
