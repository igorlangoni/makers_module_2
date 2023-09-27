import time
import requests

class TimeError():
    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def __init__(self, requester, timer):
        self.requester = requester
        self.timer = timer

    def error(self):
        return self._get_server_time() - self.timer.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self.requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]

# timeerror = TimeError()
# print(timeerror.error())