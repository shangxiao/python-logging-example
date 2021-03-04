from sample import config, info_only, show_all


def test_logging():
    info_only.log_something()
    show_all.log_something()
