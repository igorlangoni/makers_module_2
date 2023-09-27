import os
from twilio.rest import Client
from lib.delivery_time import Time
from datetime import datetime

class Takeaway:
    def __init__(self, dish_list):
        self.menu = dish_list.dish_list
        self.current_order = {}
    
    def see_menu(self):
        return self.menu
    
    def add_to_order(self, dish):
        if dish in self.menu:
            for k, v in self.menu.items():
                if k == dish:
                    self.current_order[k] = v
        else:
            raise Exception("Sorry! Item not available")    

    def check_order(self):
        self.current_order['total'] = 0
        for k, v in self.current_order.items():
            if k != 'total':
                self.current_order['total'] += v
        return self.current_order

    def place_order(self):
        if self.current_order != {}:
            self.send_sms()
            self.current_order.clear()
            return "Order Placed. Thank you!"
        else:
            raise Exception("You haven't ordered anything")
    
    def send_sms(self):
        time = Time()
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)

        message = client.messages \
                        .create(
                            body=f"Thank you! Your order was placed and will be delivered before {time.delivery_eta()}.",
                            from_='+14402204984',
                            to='+5534997384773'
                        )
        return(f"Message sent: Thank you! Your order was placed and will be delivered before {time.delivery_eta()}.")
