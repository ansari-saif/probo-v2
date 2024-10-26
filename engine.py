import json
import os

import pika

# RabbitMQ connection details
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_QUEUE = os.environ.get('RABBITMQ_QUEUE')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
RABBITMQ_PORT = 5672
USER_MAP = {}
EVENT_MAP = {}
STOCK_BALANCE_MAP = {}
DEBUG = 0


class UserBalance:
    def __init__(self):
        self.total_balance = 15
        self.locked_balance = 0

    def addUserBalance(self, balance: float):
        self.total_balance += balance

    def deductUserBalance(self, balance: float):
        self.total_balance -= balance

    def lockBalance(self, amount: float):
        self.locked_balance += amount
        self.total_balance -= amount

    def unlockBalance(self, amount: float):
        self.locked_balance -= amount
        # self.total_balance += amount

    def checkSufficientBalance(self, amount: float):
        return self.total_balance >= amount


class StockItem:
    def __init__(self, quantity=0, locked=0):
        self.quantity = quantity
        self.locked = locked

    def __repr__(self):
        return f"StockItem(quantity={self.quantity}, locked={self.locked})"


class StockBalance:
    def __init__(self):
        self.data = {
            
        }

    def add(self, event_id, quantity):
        if event_id not in self.data:
            self.data[event_id] = StockItem(quantity=quantity)
        else:
            stock_item = self.get_stock_item(event_id)
            stock_item.quantity += quantity

    def remove(self, event_id, quantity):
        # Validate that quantity is non-negative
        if quantity < 0:
            print("Quantity to remove must be non-negative.")
            return

        # Get stock item
        stock_item = self.get_stock_item(event_id)
        if stock_item:
            # Check if there is enough quantity to remove
            if stock_item.quantity >= quantity:
                stock_item.quantity -= quantity
                # Remove the event if quantity is zero
                if stock_item.quantity == 0:
                    del self.data[event_id]
            else:
                print(
                    f"Insufficient quantity to remove for event_id {event_id}")
        else:
            print(f"Event ID {event_id} not found in stock")

    def get_stock_item(self, event_id) -> StockItem:
        return self.data.get(event_id, None)

    def __repr__(self):
        return f"StockBalance(data={self.data})"


class OrderBook:
    def __init__(self, event_id: int, buy_orders: list, sell_orders: list, yes_price: float, no_price: float):
        self.event_id = event_id
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders
        self.yes_price = yes_price
        self.no_price = no_price
        self.adjustment_factor = 0.5

    def match_order(self, offer_type, price, quantity, user_id, is_reverse):
        # TODO : I just've to check the quantity
        match_order = False
        stock_balance = get_stock_balance(user_id)
        user_balance = get_user_balance(user_id)
        if offer_type == "BUY":
            # check actually buy order
            if not is_reverse:
                # then match current price and lower will be matched
                seller_user_id = None
                seller_quantity = None
                for item in self.buy_orders:
                    if item["price"] <= price:
                        # match order
                        match_order = True
                        seller_order = item
                        seller_user_id = item["user_id"]
                        seller_quantity = item["quantity"]
                        seller_price = item["price"]
                        break

                if match_order:
                    # adding stock balance both
                    stock_balance.add(
                        self.event_id, seller_quantity
                    )
                    seller_stock_balance = get_stock_balance(seller_user_id)
                    seller_stock_balance.add(self.event_id, seller_quantity)

                    
                    # unlock seller balance
                    seller_user_balance = get_user_balance(seller_user_id)
                    seller_user_balance.unlockBalance(seller_price)

                    # reduce buyer user balance
                    user_balance.deductUserBalance(seller_price)


                    self.remove_order(seller_order, offer_type)

                else:
                    self.add_order({
                        "offer_type": offer_type,
                        "price": price,
                        "quantity": quantity,
                        "user_id": user_id
                    })
                    # lock balance
                    user_balance.lockBalance(price)
            else:
                # will do later
                pass
                # # then match current price and lower will be matched
                # # TODO : check stock balance first of the current user
                # seller_user_id = None
                # seller_quantity = None
                # for item in self.buy_orders:
                #     if item["price"] >= price:
                #         # match order
                #         match_order = True
                #         seller_user_id = item["user_id"]
                #         seller_quantity = item["quantity"]
                #         break
                # if match_order:
                #     STOCK_BALANCE_MAP.get(seller_user_id).add(
                #         self.event_id, seller_quantity)
                #     STOCK_BALANCE_MAP.get(user_id).remove(
                #         self.event_id, seller_quantity)
                # else:
                #     self.add_order({
                #         "offer_type": offer_type,
                #         "price": price,
                #         "quantity": quantity,
                #         "user_id": user_id
                #     })
        elif offer_type == "SELL":
            if not is_reverse:
                # then match current price and lower will be matched
                seller_quantity = None
                seller_user_id = None
                for item in self.sell_orders:
                    if item["price"] <= price:
                        # match order
                        match_order = True
                        seller_order = item
                        seller_user_id = item["user_id"]
                        seller_quantity = item["quantity"]
                        seller_price = item["price"]
                        break
                if match_order:
                    # adding stock balance for both
                    stock_balance.add(
                        self.event_id, seller_quantity
                    )
                    seller_stock_balance = get_stock_balance(seller_user_id)
                    seller_stock_balance.add(self.event_id, seller_quantity)


                    # unlock seller balance
                    seller_user_balance = get_user_balance(seller_user_id)
                    seller_user_balance.unlockBalance(10-seller_price)

                    # reduce buyer user balance
                    user_balance.deductUserBalance(seller_price)
                    self.remove_order(seller_order, offer_type)

                else:
                    self.add_order({
                        "offer_type": offer_type,
                        "price": price,
                        "quantity": quantity,
                        "user_id": user_id
                    })
                    # lock balance
                    user_balance.lockBalance(price)
            else:
                pass
            # reverse order
            # implement here sell logic
        else:
            raise Exception("Invalid offer type")
        self.adjust_prices()

    def initiate_order(self, offer_type, price, quantity, user_id, is_reverse):
        self.match_order(offer_type, price, quantity, user_id, is_reverse)

    def calculate_demand_supply(self):
        total_demand = sum(order['quantity'] * order['price']
                           for order in self.buy_orders)
        total_supply = sum(order['quantity'] * order['price']
                           for order in self.sell_orders)
        return total_demand, total_supply

    def adjust_prices(self):
        total_demand, total_supply = self.calculate_demand_supply()
        if total_demand > total_supply:
            self.no_price += self.adjustment_factor
            self.yes_price -= self.adjustment_factor
        elif total_supply > total_demand:
            self.no_price -= self.adjustment_factor
            self.yes_price += self.adjustment_factor

    def add_order(self, order: dict):
        # with user_id
        # total = offer_type, quantity, price, user_id
        if order["offer_type"] == "BUY":
            self.sell_orders.append({
                "price": 10-order["price"],
                "quantity": order["quantity"],
                "user_id": order["user_id"]
            })
        elif order["offer_type"] == "SELL":
            self.buy_orders.append({
                "price": 10-order["price"],
                "quantity": order["quantity"],
                "user_id": order["user_id"]
            })
        else:
            raise Exception("INVALID offer type")
        
    def remove_order(self, order: dict, offer_type):
        target_orders = self.buy_orders if offer_type == "BUY" else self.sell_orders
        for o in target_orders:
            # TODO : implement price and quantity logic
            if o["user_id"] == order["user_id"]:
                target_orders.remove(o)
                break



def connect_to_rabbitmq():
    credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(RABBITMQ_HOST,
                                           5672,  # Default RabbitMQ port
                                           RABBITMQ_USERNAME,
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)
    return channel


def get_orderbook(event_id) -> OrderBook:
    return EVENT_MAP.get(event_id)  # Returns None if event_id is not found


def get_user_balance(user_id) -> UserBalance:
    return USER_MAP.get(user_id)  # Returns None if user_id is not found


def get_stock_balance(user_id) -> StockBalance:
    # Returns None if user_id is not found
    return STOCK_BALANCE_MAP.get(user_id)


def process_orderbook(orderbook_data):
    event_id = orderbook_data["event_id"]
    user_id = orderbook_data["user_id"]
    offer_type = orderbook_data["offer_type"]
    is_reverse = orderbook_data.get("is_reverse", False)
    if not USER_MAP.get(orderbook_data["user_id"]):
        USER_MAP[orderbook_data["user_id"]] = UserBalance()

    if not EVENT_MAP.get(orderbook_data["event_id"]):
        EVENT_MAP[orderbook_data["event_id"]] = OrderBook(
            event_id=event_id,
            buy_orders=[],
            sell_orders=[],
            yes_price=5,
            no_price=5
        )
    if not STOCK_BALANCE_MAP.get(orderbook_data["user_id"]):
        STOCK_BALANCE_MAP[orderbook_data["user_id"]] = StockBalance()

    orderbook = get_orderbook(orderbook_data["event_id"])
    l1_expected_price = orderbook_data.get("l1_expected_price")
    price = l1_expected_price
    orderbook.initiate_order(
        offer_type, price, orderbook_data["l1_order_quantity"], user_id, is_reverse
    )

    processed_data = {
        "processed": True,
        "yes_price": orderbook.yes_price,
        "no_price": orderbook.no_price,
        "buy_orders": orderbook.buy_orders,
        "sell_orders": orderbook.sell_orders
    }
    return processed_data


def publish_queue(data, queue_name):
    RABBITMQ_CONNECTION = pika.BlockingConnection(
        pika.ConnectionParameters(RABBITMQ_HOST, int(RABBITMQ_PORT),
                                  RABBITMQ_USERNAME,
                                  pika.PlainCredentials(RABBITMQ_USERNAME,
                                                        RABBITMQ_PASSWORD)))
    RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()
    RABBITMQ_CHANNEL.basic_publish(exchange='', routing_key=queue_name,
                                   body=json.dumps(data, default=str).encode('utf-8'))
    RABBITMQ_CONNECTION.close()


def consumer(body):
    processed_data = process_orderbook(body)
    publish_queue(processed_data, "orderbook_queue_acknowledgment")


input_data = {}


def main():
    if DEBUG:
        consumer(input_data)
    else:
        RABBITMQ_CONNECTION = pika.BlockingConnection(
            pika.ConnectionParameters(RABBITMQ_HOST, int(RABBITMQ_PORT),
                                      RABBITMQ_USERNAME,
                                      pika.PlainCredentials(RABBITMQ_USERNAME,
                                                            RABBITMQ_PASSWORD)))
        RABBITMQ_CHANNEL = RABBITMQ_CONNECTION.channel()

        def callback(ch, method, properties, body):
            try:
                requested_data = json.loads(body.decode("utf-8"))
                consumer(requested_data)
                ch.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as E:
                ch.basic_ack(delivery_tag=method.delivery_tag)
                error_text = str(E)
                print(error_text)

        RABBITMQ_CHANNEL.basic_consume(
            queue=RABBITMQ_QUEUE, on_message_callback=callback)
        print(' [*] Waiting for messages. To exit press CTRL+C')
        RABBITMQ_CHANNEL.start_consuming()


if __name__ == '__main__':
    main()
