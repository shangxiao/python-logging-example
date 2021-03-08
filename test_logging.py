from sample import info_only, show_all


def test_logging():
    from sample import config

    info_only.log_something()
    show_all.log_something()


def test_logging_dict_config():
    from sample import config_from_dict

    info_only.log_something()
    show_all.log_something()
