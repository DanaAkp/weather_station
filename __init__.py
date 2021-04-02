from base.subject import Subject
from weather_data.weather_data import WeatherData
from element_display.current_condition import CurrentCondition
from weather_data.data import Data


if __name__ == '__main__':
    data = Data()
    wd = WeatherData()
    x = CurrentCondition()

    wd.register_observer(x)

    x.display()
    wd.measurements_changed()
    x.display()