from abc import ABC, abstractmethod
from apache_beam.transforms.userstate import BagStateSpec
import apache_beam as beam

class AlgoBase(ABC, beam.DoFn):

    def __init__(self):
        print("AlgoBase INIT ---->")


    @abstractmethod
    def condition(self, data):
        pass

    @abstractmethod
    def on_condition_met(self):
        pass

    @abstractmethod
    def on_condition_not_met(self):
        pass

    @abstractmethod
    def track_placed_order(self, data):
        pass

    @abstractmethod
    def is_order_already_placed_at_this_condition(self):
        pass

    def process(self, element):
        print(f"AlgoBase ---->PROCESS element: {element}")
        stock, data = element
        self.stock = stock
        self.c_price = data["price"]
        self.d_low = data["dayLow"]
        self.d_high = data["dayHigh"]


        is_condition_met = self.condition(data=element)

        if is_condition_met:
            if self.is_order_already_placed_at_this_condition():
                self.on_condition_met()
                self.track_placed_order(data)
        else:
            self.on_condition_not_met()
