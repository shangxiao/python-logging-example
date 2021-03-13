# python-logging-example

* `disable_existing_loggers` must be set to `False` if there's a chance config is loaded after the creation of loggers
* Loggers propagate messages *up* the hierarchy unless set to `False`
* Use `logging.getLogger(__name__)` or manually use dot paths for easier referencing in log and configuration
