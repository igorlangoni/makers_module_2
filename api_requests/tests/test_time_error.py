from unittest.mock import Mock
from lib.time_error import TimeError

def test_calling_error_returns():
    requester_mock = Mock()
    response_mock = Mock()
    timer_mock = Mock()
    timer_mock.time.return_value = 1695640928.5
    error_checker = TimeError(requester_mock, timer_mock)
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"unixtime": 1695640928 }
    assert  error_checker.error() == -0.5
