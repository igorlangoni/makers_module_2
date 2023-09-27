from lib.challenge_class_system.contact import *
import pytest

def test_after_initiating_can_access_properties():
    contact = Contact('Alline', '9834-3139')
    assert contact.name == 'Alline'
    assert contact.phone_number == '9834-3139'

def test_number_is_formatted_correctly():
    with pytest.raises(Exception) as e:
        contact = Contact('Alline', '000-0000')
    error = str(e.value)
    actual = error
    assert error == 'NUMERO INCORRETO'

