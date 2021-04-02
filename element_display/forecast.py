from base.display import Display
from base.observer import Observer
from weather_data.data import Data


class Forecast(Observer, Display):
    def __init__(self):
        self.data_forecast = Data()

    def update(self, data):
        self.data_forecast = self.get_forecast(data)

    def display(self):
        print(self.data_forecast.print_display())

    def get_forecast(self, data):
        # какие-то действия, которые расчитывают статистику по полученным данным
        return data
