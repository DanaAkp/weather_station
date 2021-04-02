from base.display import Display
from base.observer import Observer
from weather_data.data import Data


class Statistics(Observer, Display):
    def __init__(self):
        self.data_stat = Data()

    def update(self, data):
        self.data_stat = self.get_statistics(data)

    def display(self):
        print(self.data_stat.print_display())

    def get_statistics(self, data):
        #какие-то действия, которые расчитывают статистику по полученным данным
        return data
