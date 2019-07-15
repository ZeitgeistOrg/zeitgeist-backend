import boto3
import pytest
import json

def api_gateway_event(httpMethod, payload: dict) -> dict:
    return {
        'resource': '',
        'path': '',
        'httpMethod': httpMethod,
        'headers': {},
        'requestContext': {
            'resourcePath': '',
            'httpMethod': httpMethod
        },
        'body': json.dumps(payload)
    }