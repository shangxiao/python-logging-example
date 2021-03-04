import logging
import sys

# configure the root logger to print to stdout and show everything
# logging.basicConfig(handler=logging.StreamHandler(sys.stdout), level=logging.DEBUG)
logger = logging.getLogger()
stdout_handler = logging.StreamHandler(sys.stdout)
stdout_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(stdout_handler)
logger.setLevel(logging.DEBUG)

# make sure that only info messages are shown from sample.sample
info_only_logger = logging.getLogger("sample.info_only")
info_only_logger.setLevel(logging.INFO)
