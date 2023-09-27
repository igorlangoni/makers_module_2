from unittest.mock import Mock
from lib.cat_facts import CatFacts

def test_providing_a_cat_fact():
    requester_mock = Mock()
    response_mock = Mock()
    requester_mock.get.return_value = response_mock
    response_mock.json.return_value = {"fact": 'cats are the worse', "lenght": 18}
    cat_facts = CatFacts(requester_mock)
    assert cat_facts.provide() == "Cat fact: cats are the worse"
