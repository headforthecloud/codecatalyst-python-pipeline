#! /usr/bin/env python
""" An example lambda function """

import os
import json
import logging


# define a logger using logging library. If LOG_LEVEL is not set, default to INFO.
# otherwise use value of LOG_LEVEL
logger = logging.getLogger()
logger.setLevel(os.getenv('LOG_LEVEL', 'INFO'))


def lambda_handler(event, context):
    """ define a lambda_handler function that takes in an event and a context """
    logger.info("Hello from Lambda!")

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }


def add_x_y(x, y):
    """ This is a simple function that adds two numbers together and returns the result. """
    return x + y


def multiply_x_y(x, y):
    """ This is a simple function that multiplies two numbers together and returns the result. """
    return x * y


# if this file is run directly, run the lambda_handler function with dummy event and context
if __name__ == '__main__':
    lambda_handler(None, None)
