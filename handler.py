import json
import time
import logging

logger = logging.getLogger("handler_logger")
logger.setLevel(logging.DEBUG)


def ping(event, context):
    logger.info("Ping requested.")
    current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    response = {
        "statusCode": 200,
        "body": "Service status: Online. Timestamp: " + current_time
    }

    return response
