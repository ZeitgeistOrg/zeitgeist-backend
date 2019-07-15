from tests import *
from moto import mock_dynamodb2
from handlers.questions import lambda_handler as h, TABLE_NAME

@mock_dynamodb2
def setup():
    # TODO do some setup here using moto
    pass

setup()

@mock_dynamodb2
def test_questions_handler():
    # TODO response = h(api_gateway_event('POST', {}), None)
    assert True