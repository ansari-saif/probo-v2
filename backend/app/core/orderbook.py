class OrderBook:
    def __init__(self, event_id: int, buy_orders: list, sell_orders: list, buy_price: float, sell_price: float):
        self.event_id = event_id
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.adjustment_factor = 0.5

    def calculate_demand_supply(self):
        total_demand = sum(order['quantity'] for order in self.buy_orders)
        total_supply = sum(order['quantity'] for order in self.buy_orders)
        return total_demand, total_supply

    def adjust_prices(self):
        total_demand, total_supply = self.calculate_demand_supply()
        if total_demand > total_supply:
            self.buy_price += self.adjustment_factor
            self.sell_price -= self.adjustment_factor
        elif total_supply > total_demand:
            self.buy_price -= self.adjustment_factor
            self.sell_price += self.adjustment_factor



          
