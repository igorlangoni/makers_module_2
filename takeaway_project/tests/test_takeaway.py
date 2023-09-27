from unittest.mock import Mock
from lib.takeaway import Takeaway
import pytest


def test_initializes_with_dish_list_param_and_return_menu():
    dish_list_mock = Mock()
    dish_list_mock.dish_list = {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}
    takeaway = Takeaway(dish_list_mock)
    assert takeaway.menu == {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}

def test_adding_multiple_dishes_to_order_if_they_are_in_menu():
    dish_list_mock = Mock()
    dish_list_mock.dish_list = {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}
    takeaway = Takeaway(dish_list_mock)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    assert takeaway.current_order == {'fish': 17, 'soup': 9}

def test_adding_multiple_dishes_to_order_if_they_are_in_menu():
    dish_list_mock = Mock()
    dish_list_mock.dish_list = {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}
    takeaway = Takeaway(dish_list_mock)
    takeaway.add_to_order('fish')
    with pytest.raises(Exception) as e:
        takeaway.add_to_order('Steak')
    error_msg = str(e.value)
    assert error_msg == 'Sorry! Item not available'

def test_add_multiple_dishes_to_order_returns_them_and_grand_total():
    dish_list_mock = Mock() 
    dish_list_mock.dish_list = {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}
    takeaway = Takeaway(dish_list_mock)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    assert takeaway.check_order() == {'fish': 17, 'soup': 9, 'total': 26}

# def test_send_msg_returns_confirmation_string():
#     time = Mock()
#     time.current_time = '10.30'
#     time.delivery_eta.return_value = '11.30'
#     dish_list_mock = Mock()
#     dish_list_mock.dish_list = {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}   
#     takeaway = Takeaway(dish_list_mock)
#     assert takeaway.send_sms() == f"Message sent: Thank you! Your order was placed and will be delivered before {time.delivery_eta()}."
