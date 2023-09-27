from lib.takeaway import Takeaway
from lib.dish import Dish
from lib.delivery_time import Time
import pytest
from unittest.mock import Mock

def test_initializes_with_dish_list_param_and_return_menu():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    assert takeaway.menu == {'chicken' : 15, 'fish': 17, 'soup': 9, 'arancini': 8}

def test_adding_multiple_dishes_to_order_if_they_are_in_menu():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    assert takeaway.current_order == {'fish': 17, 'soup': 9}

def test_raises_error_if_ordered_item_not_in_menu():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    takeaway.add_to_order('fish')
    with pytest.raises(Exception) as e:
        takeaway.add_to_order('Steak')
    error_msg = str(e.value)
    assert error_msg == 'Sorry! Item not available'

def test_add_multiple_dishes_to_order_can_return_them_and_grand_total():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    assert takeaway.check_order() == {'fish': 17, 'soup': 9, 'total': 26}

def test_placing_an_order_sends_sms_with_arrive_by_time():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    assert takeaway.place_order() == 'Order Placed. Thank you!'

def test_placing_order_with_nothing_in_it_raises_error():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    with pytest.raises(Exception) as e:
        takeaway.place_order()
    error_msg = str(e.value)
    assert error_msg ==  "You haven't ordered anything"  

def test_send_msg_returns_confirmation_string():
    time = Time()
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    assert takeaway.send_sms() == f"Message sent: Thank you! Your order was placed and will be delivered before {time.delivery_eta()}."

def test_placing_an_order_empties_the_previous_order():
    dish_list = Dish()
    takeaway = Takeaway(dish_list)
    takeaway.add_to_order('fish')
    takeaway.add_to_order('soup')
    takeaway.place_order()
    assert takeaway.current_order == {}

