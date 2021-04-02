class Data:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.oxygen = 0
        self.is_fog = False
        self.precipitation = 0

    def print_display(self):
        s = 'Температура: {temp}°C\nВлажность: {humid}%\nДавление: {pres} мм.рт.ст\n' \
            'Процент кислорода: {oxyg}%\nКоличество осадков: {precip}%\nНаличие тумана: {fog}'. \
            format(temp=self.temperature, humid=self.humidity, pres=self.pressure, oxyg=self.oxygen,
                   precip=self.precipitation, fog=self.is_fog)
        return s
