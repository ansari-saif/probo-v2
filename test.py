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

        # Act
        consumer(case1)  # Process the order
        # unmatched
        self.orderbook = get_orderbook(self.event_id)
        # orderbook
        self.assertListEqual(self.orderbook.sell_orders, [
            {
                "price": 6,
                "quantity": 1,
                "user_id": 1
            }
        ], "sell order created for user1 @ price 10-n is 6")
        self.assertEqual(self.orderbook.yes_price, 5.5)
        self.assertEqual(self.orderbook.no_price, 4.5)

        # userBalance
        user1_balance = get_user_balance(case1["user_id"])
        self.assertEqual(user1_balance.total_balance, 11)
        self.assertEqual(user1_balance.locked_balance, 4)
        
        # stockBalance
        stock_balance = get_stock_balance(user_id)
        self.assertEqual(stock_balance.get_stock_item(self.event_id), None)

        # Test case 2: user2 buys at price 4
        user_id_2 = 2
        case2 = {
            "event_id": self.event_id,
            "user_id": user_id_2,
            "offer_type": "BUY",
            "l1_expected_price": 4,
            "l1_order_quantity": 1
        }
        

        consumer(case2)  # Process user2's order
        
        # Assert: orderbook updates
        self.assertListEqual(self.orderbook.sell_orders, [
            {
                "price": 6,
                "quantity": 1,
                "user_id": 1
            },
            {
                "price": 6,
                "quantity": 1,
                "user_id": 2
            }
        ], "Sell order created for user2 @ price 4")
        self.assertEqual(self.orderbook.yes_price, 6)
        self.assertEqual(self.orderbook.no_price, 4)

        # User balance after order
        user2_balance = get_user_balance(user_id_2)
        self.assertEqual(user2_balance.total_balance, 11)
        self.assertEqual(user2_balance.locked_balance, 4)

         # stockBalance
        stock_balance = get_stock_balance(user_id_2)
        self.assertEqual(stock_balance.get_stock_item(self.event_id), None)



        # Test case 3: user3 buy no at price 8
        case3 = {
            "event_id": self.event_id,
            "user_id": 3,
            "offer_type": "SELL",
            "l1_expected_price": 8,
            "l1_order_quantity": 1  # Assuming user is selling 1 stock
        }
        
        consumer(case3)  # Process user1's sell order
        
        # Assert: orderbook updates after user1 sells
        self.assertListEqual(self.orderbook.sell_orders, [
            {
                "price": 6,
                "quantity": 1,
                "user_id": 2
            },
        ], "Sell order created for user1 @ price 8")

        # matched with user1 

        # User1 balance
        user1_balance = get_user_balance(1)
        self.assertEqual(user1_balance.total_balance, 11)
        # TODO : WORKING HERE
        self.assertEqual(user1_balance.locked_balance, 0)

        # User3 balance
        user3_balance = get_user_balance(3)
        self.assertEqual(user3_balance.total_balance, 9)
        self.assertEqual(user3_balance.locked_balance, 0)

         # user1 stockBalance
        stock_balance = get_stock_balance(1)
        self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 1)
        self.assertEqual(stock_balance.get_stock_item(self.event_id).locked, 0)

         # user3 stockBalance
        stock_balance = get_stock_balance(3)
        self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 1)
        self.assertEqual(stock_balance.get_stock_item(self.event_id).locked, 0)

        # Test case 4: user3 sells at price 4
        user_id_3 = 3
        case4 = {
            "event_id": self.event_id,
            "user_id": user_id_3,
            "offer_type": "SELL",
            "l1_expected_price": 4,
            "l1_order_quantity": 1  # Assuming user3 is selling 1 stock
        }

        consumer(case4)  # Process user3's sell order

        # Assert: orderbook updates after user3 sells
        self.assertListEqual(self.orderbook.sell_orders, [
            {
                "price": 4,
                "quantity": 1,
                "user_id": 2
            },
        ])
        self.assertListEqual(self.orderbook.buy_orders, [
            {
                "price": 6,
                "quantity": 1,
                "user_id": 3
            },
        ])

        # User3 balance after selling
        user3_balance = get_user_balance(user_id_3)
        self.assertEqual(user3_balance.total_balance, 5)  # Assuming starting balance
        self.assertEqual(user3_balance.locked_balance, 4)  # Assuming no locked balance


if __name__ == "__main__":
    unittest.main()
