#! /usr/bin/env python
""" Test lambda_handler """

import json
from lambda_function import lambda_handler


def test_lambda_handler():
    """ Test the main function returns 200 """
    event = {
        "test": "test"
    }
    context = {
        "test": "test"
    }
    response = lambda_handler(event, context)
    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == event
