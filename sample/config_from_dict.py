import logging
import logging.config
import sys

logging.config.dictConfig(
    {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "simple": {
                "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": logging.DEBUG,
                "formatter": "simple",
                "stream": sys.stdout,
            },
        },
        "loggers": {
            "sample.info_only": {
                "level": logging.INFO,
            },
        },
        "root": {
            "level": logging.DEBUG,
            "handlers": ["console"],
        },
    }
)
