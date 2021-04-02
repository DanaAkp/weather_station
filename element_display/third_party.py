from base.display import Display
from base.observer import Observer
from weather_data.data import Data


class ThirdParty(Observer, Display):
    def __init__(self):
        self.data = Data()

    def update(self, data):
        self.data = data

    def display(self):
        print(self.data.print_display())
