from lib.activity_suggester import ActivitySuggester
from unittest.mock import Mock


def test_calls_api_to_provide_suggested_activity():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {
        "activity": 'swim with dolphins',
        "participants": 2
    }
    activity_suggester = ActivitySuggester(requester_mock)
    result = activity_suggester.suggest()
    assert result == 'Why not: swim with dolphins'