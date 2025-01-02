from .base import AlgoBase
import apache_beam as beam

high_low_strategy_boundary_percent = 0.001

class DayHighReversalStrategy(AlgoBase):

    def __init__(self):
        super().__init__()


    def condition(self, data):
        # print("DayHighReversalStrategy condition ---->")
        self.low_bound = self.d_high - (self.d_high * high_low_strategy_boundary_percent)
        self.high_bound = self.d_high + (self.d_high * high_low_strategy_boundary_percent)

        if self.low_bound <= self.c_price <= self.high_bound :
            print(f" ===========> condition met for {self.stock} at {self.c_price} LOW: {self.low_bound} HIGH: {self.high_bound}....")
            return True

    def on_condition_met(self):
        pass

    def on_condition_not_met(self):
        pass

    def track_placed_order(self, placed_orders):
        placed_orders.add(self.c_price)

    def is_order_already_placed_at_this_condition(self, placed_orders):
        placed_orders_list = list(placed_orders.read())
        if len(placed_orders_list) == 0 :
            print("Placing Order .... ", placed_orders_list)
            self.track_placed_order(placed_orders)
        elif self.c_price <= min(placed_orders_list) * 0.992:
            print("Placing Next Order ....")
            self.track_placed_order(placed_orders)

    # def process(self, element, *args, **kwargs):
    #     print("DayHighReversalStrategy ---> process:", element)