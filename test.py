import unittest
from engine import EVENT_MAP, consumer, get_orderbook, get_stock_balance, get_user_balance


class TestConsumerOrderBook(unittest.TestCase):
    def setUp(self):
        self.event_id = 1
        self.orderbook = get_orderbook(self.event_id)

    def test_consumer_adds_buy_order(self):
        # test1 user1 buy@4
        user_id = 1
        case1 = {
            "event_id": self.event_id,
            "user_id": 1,
            "offer_type": "BUY",
            "l1_expected_price": 4,
            "l1_order_quantity": user_id
        }
        user1_balance = get_user_balance(case1["user_id"])
        self.assertEqual(user1_balance.total_balance, 15)
        self.assertEqual(user1_balance.locked_balance, 0)

        # Act
        consumer(case1)  # Process the order
        # unmatched

        # orderbook
        self.assertDictEqual(self.orderbook.sell_orders, [
            {
                "price": 6,
                "quantity": 1,
                "user_id": 1
            }
        ], "sell order created for user1 @ price 10-n is 6")
        self.assertEqual(self.orderbook.buy_price, 5.5)

        # userBalance
        self.assertEqual(user1_balance.total_balance, 11)
        self.assertEqual(user1_balance.locked_balance, 4)
        
        # stockBalance
        stock_balance = get_stock_balance(user_id)
        self.assertEqual(stock_balance.get_stock_item(self.event_id), None)

        # TODO : ADD thse casses
        # case 2 user2 buy@4
        # case 3 user1 sell@8
        # case 4 user3 sell@4

if __name__ == "__main__":
    unittest.main()
