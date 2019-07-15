from tests import *
from moto import mock_dynamodb
from handlers.answers import lambda_handler as h

def setup():
    pass

@mock_dynamodb
def test_answers_handler():
    setup()
    assert True