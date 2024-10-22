import pika
import json
import os

# RabbitMQ connection details
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_QUEUE = os.environ.get('RABBITMQ_QUEUE')
RABBITMQ_USERNAME = os.environ.get('RABBITMQ_USERNAME')
RABBITMQ_PASSWORD = os.environ.get('RABBITMQ_PASSWORD')
USER_MAP = {}
EVENT_MAP = {}
STOCK_BALANCE_MAP = {}


class UserBalance:
    def __init__(self):
        self.data = {
            1: {
                "total_balance": 1500,
                "locked_balance": 0
            }
        }

    def setUserBalance(self, user_id: int, balance: float):
        self.data[user_id] = {
            "total_balance": balance,
            "locked_balance": 0
        }

    def getUserBalance(self, user_id: int):
        return self.data[user_id]

    def lockBalance(self, user_id: int, amount: float):
        self.data[user_id]["locked_balance"] += amount
        self.data[user_id]["total_balance"] -= amount

    def unlockBalance(self, user_id: int, amount: float):
        self.data[user_id]["locked_balance"] -= amount
        self.data[user_id]["total_balance"] += amount

    def checkSufficientBalance(self, user_id: int, amount: float):
        return self.data[user_id]["total_balance"] >= amount


class StockBalance:
    def __init__(self):
        self.data = {}

    def add(self, event_id, quantity):
        if not self.data.get(event_id):
            self.data[event_id] = {"quantity": quantity, "locked": 0}
        else:
            self.data[event_id]["quantity"] += quantity

    def remove(self, event_id, quantity):
        # TODO : complete this
        pass


class OrderBook:
    def __init__(self, event_id: int, buy_orders: list, sell_orders: list, buy_price: float, sell_price: float):
        self.event_id = event_id
        self.buy_orders = buy_orders
        self.sell_orders = sell_orders
        self.buy_price = buy_price
        self.sell_price = sell_price
        self.adjustment_factor = 0.5

    def match_order(self, offer_type, price, quantity, user_id, is_reverse):
        # TODO : I just've to creck the quantity
        match_order = False
        if offer_type == "buy":
            # check actually buy order
            if not is_reverse:
                # then match current price and lower will be matched
                seller_user_id = None
                seller_quantity = None
                for item in self.buy_orders:
                    if item["price"] <= price:
                        # match order
                        match_order = True
                        seller_user_id = item["user_id"]
                        seller_quantity = item["quantity"]
                        break
                if match_order:
                    STOCK_BALANCE_MAP.get(seller_user_id).remove(
                        self.event_id, seller_quantity
                    )
                    STOCK_BALANCE_MAP.get(user_id).add(
                        self.event_id, seller_quantity
                    )
                else:
                    self.add_order({
                        "offer_type": offer_type,
                        "price": price,
                        "quantity": quantity,
                        "user_id": user_id
                    })
            else:
                # then match current price and lower will be matched
                # TODO : check stock balance first of the current user
                seller_user_id = None
                seller_quantity = None
                for item in self.buy_orders:
                    if item["price"] >= price:
                        # match order
                        match_order = True
                        seller_user_id = item["user_id"]
                        seller_quantity = item["quantity"]
                        break
                if match_order:
                    STOCK_BALANCE_MAP.get(seller_user_id).add(
                        self.event_id, seller_quantity)
                    STOCK_BALANCE_MAP.get(user_id).remove(
                        self.event_id, seller_quantity)
                else:
                    self.add_order({
                        "offer_type": offer_type,
                        "price": price,
                        "quantity": quantity,
                        "user_id": user_id
                    })
            if match_order:
                self.adjust_prices()

    def initiate_order(self, offer_type, price, quantity, user_id, is_reverse):
        self.match_order(offer_type, price, quantity, user_id, is_reverse)

    def calculate_demand_supply(self):
        total_demand = sum(order['quantity'] for order in self.buy_orders)
        total_supply = sum(order['quantity'] for order in self.sell_orders)
        return total_demand, total_supply

    def adjust_prices(self):
        total_demand, total_supply = self.calculate_demand_supply()
        if total_demand > total_supply:
            self.buy_price += self.adjustment_factor
            self.sell_price -= self.adjustment_factor
        elif total_supply > total_demand:
            self.buy_price -= self.adjustment_factor
            self.sell_price += self.adjustment_factor

    def add_order(self, order: dict):
        # with user_id
        # total = offer_type, quantity, price, user_id
        if order["offer_type"] == "buy":
            self.buy_orders.append(order)
        else:
            self.sell_orders.append(order)
        self.adjust_prices()


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


def process_orderbook(orderbook_data):
    event_id = orderbook_data["event_id"]
    user_id = orderbook_data["user_id"]
    offer_type = orderbook_data["offer_type"]
    is_reverse = orderbook_data["is_reverse"]
    if not USER_MAP.get(orderbook_data["user_id"]):
        USER_MAP[orderbook_data["user_id"]] = UserBalance()

    if not EVENT_MAP.get(orderbook_data["event_id"]):
        EVENT_MAP[orderbook_data["event_id"]] = OrderBook(
            event_id=event_id,
            buy_orders=[],
            sell_orders=[],
            buy_price=5,
            sell_price=5
        )
    orderbook = EVENT_MAP[orderbook_data["event_id"]]
    l1_expected_price = orderbook_data.get("l1_expected_price")
    price = l1_expected_price*100
    orderbook.initiate_order(
        offer_type, price, orderbook_data["l1_order_quantity"], user_id, is_reverse
    )

    processed_data = {
        "processed": True,
        "buy_price": orderbook.buy_price,
        "sell_price": orderbook.sell_price,
        "buy_orders": orderbook.buy_orders,
        "sell_orders": orderbook.sell_orders
    }
    return processed_data


def publish_queue(channel, processed_data):
    # Convert the processed data to JSON
    message = json.dumps(processed_data)
    channel.basic_publish(exchange='',
                          routing_key="orderbook_queue_acknowledgment",
                          body=message)
    print("Acknowledgment sent:", processed_data)


def callback(ch, method, properties, body):
    # Callback function to process incoming messages
    orderbook_data = json.loads(body)
    print("Received orderbook:", orderbook_data)

    # Process the orderbook
    processed_data = process_orderbook(orderbook_data)

    # Send acknowledgment
    publish_queue(ch, processed_data)

    # Acknowledge the message consumption
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    # Set up RabbitMQ connection and start consuming messages
    channel = connect_to_rabbitmq()
    channel.basic_consume(queue=RABBITMQ_QUEUE, on_message_callback=callback)

    print("Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    main()
