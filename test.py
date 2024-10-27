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
        self.assertEqual(user1_balance.locked_balance, 0)

        # User3 balance
        user3_balance = get_user_balance(3)
        self.assertEqual(user3_balance.total_balance, 9)
        self.assertEqual(user3_balance.locked_balance, 0)

        # user1 stockBalance
        stock_balance = get_stock_balance(1)
        self.assertEqual(stock_balance.get_stock_item(
            self.event_id).quantity, 1)
        self.assertEqual(stock_balance.get_stock_item(self.event_id).locked, 0)

        # user3 stockBalance
        stock_balance = get_stock_balance(3)
        self.assertEqual(stock_balance.get_stock_item(
            self.event_id).quantity, 1)
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
                "price": 6,
                "quantity": 1,
                "user_id": 2
            },
        ])
        self.assertListEqual(self.orderbook.buy_orders, [{
            "price": 6,
            "quantity": 1,
            "user_id": 3
        }])

        # User3 balance after selling
        user3_balance = get_user_balance(user_id_3)

        # Assuming starting balance
        self.assertEqual(user3_balance.total_balance, 5)

        # user1 want to sell holdings@5
        # this should be executed@6
        case5 = {
            "event_id": self.event_id,
            "user_id": 1,
            "offer_type": "SELL",
            "l1_expected_price": 5,
            "l1_order_quantity": 1,
            "is_reverse": True
        }
        consumer(case5)
        self.assertListEqual(self.orderbook.sell_orders, [])
        self.assertListEqual(self.orderbook.buy_orders, [{
            "price": 6,
            "quantity": 1,
            "user_id": 3
        }])
        user1_balance = get_user_balance(1)
        self.assertEqual(user1_balance.total_balance, 17)
        self.assertEqual(user1_balance.locked_balance, 0)

        # User2 balance after order
        user2_balance = get_user_balance(2)
        self.assertEqual(user2_balance.total_balance, 11)
        self.assertEqual(user2_balance.locked_balance, 0)


    # def test_consumer_adds_buy_order_with_quantity(self):
    #     # INIT PRICE IS 1500
    #     # case1 user1 buy-10@6
    #     user_id = 1
    #     case1 = {
    #         "event_id": self.event_id,
    #         "user_id": 1,
    #         "offer_type": "BUY",
    #         "l1_expected_price": 6,
    #         "l1_order_quantity": 10
    #     }
    #     user1_balance = get_user_balance(case1["user_id"])

    #     # Act
    #     consumer(case1)  # Process the order
    #     # unmatched
    #     self.orderbook = get_orderbook(self.event_id)
    #     # orderbook
    #     self.assertListEqual(self.orderbook.sell_orders, [
    #         {
    #             "price": 4,
    #             "quantity": 10,
    #             "user_id": 1
    #         }
    #     ], "sell order created for user1 @ price 10-n")
    #     self.assertEqual(self.orderbook.yes_price, 5.5)
    #     self.assertEqual(self.orderbook.no_price, 4.5)

    #     # userBalance
    #     user1_balance = get_user_balance(case1["user_id"])
    #     self.assertEqual(user1_balance.total_balance, 1440)
    #     self.assertEqual(user1_balance.locked_balance, 60)

    #     # stockBalance
    #     stock_balance = get_stock_balance(user_id)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id), None)

    #     # case2 user2 buy-15@7
    #     case2 = {
    #         "event_id": self.event_id,
    #         "user_id": 2,
    #         "offer_type": "BUY",
    #         "l1_expected_price": 7,
    #         "l1_order_quantity": 15
    #     }

    #     # Act
    #     consumer(case2)  # Process the order
    #     # unmatched
    #     self.orderbook = get_orderbook(self.event_id)
    #     # orderbook
    #     self.assertListEqual(self.orderbook.sell_orders, [
    #         {
    #             "price": 3,
    #             "quantity": 15,
    #             "user_id": 2
    #         },
    #         {
    #             "price": 4,
    #             "quantity": 10,
    #             "user_id": 1
    #         },
    #     ], "sell order created for user1 @ price 10-n")
    #     self.assertEqual(self.orderbook.yes_price, 6)
    #     self.assertEqual(self.orderbook.no_price, 4)

    #     # userBalance
    #     user2_balance = get_user_balance(2)
    #     self.assertEqual(user2_balance.total_balance, 1395)
    #     self.assertEqual(user2_balance.locked_balance, 105)

    #     # stockBalance
    #     stock_balance = get_stock_balance(2)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id), None)

    #     # case3 user3 buy-no-8@4
    #     case3 = {
    #         "event_id": self.event_id,
    #         "user_id": 3,
    #         "offer_type": "SELL",
    #         "l1_expected_price": 4,
    #         "l1_order_quantity": 8
    #     }

    #     # Act
    #     consumer(case3)  # Process the order
    #     # unmatched
    #     self.orderbook = get_orderbook(self.event_id)

    #     # orderbook
    #     self.assertListEqual(self.orderbook.sell_orders, [
    #         {
    #             "price": 3,
    #             "quantity": 7,
    #             "user_id": 2
    #         },
    #         {
    #             "price": 4,
    #             "quantity": 10,
    #             "user_id": 1
    #         },
    #     ], "sell order created for user1 @ price 10-n")

    #     # userBalance
    #     user3_balance = get_user_balance(3)
    #     self.assertEqual(user3_balance.total_balance, 1476)
    #     self.assertEqual(user3_balance.locked_balance, 0)

    #     # user2Balance
    #     user2_balance = get_user_balance(2)
    #     self.assertEqual(user2_balance.total_balance, 1395)
    #     self.assertEqual(user2_balance.locked_balance, 49)

    #     # stockBalance
    #     stock_balance = get_stock_balance(3)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 8)
    #     # stock2Balance
    #     stock_balance = get_stock_balance(2)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 8)

    #     # case4 user4 buy-no-15@3
    #     case4 = {
    #         "event_id": self.event_id,
    #         "user_id": 4,
    #         "offer_type": "SELL",
    #         "l1_expected_price": 3,
    #         "l1_order_quantity": 15
    #     }

    #     # Act
    #     consumer(case4)  # Process the order
    #     # unmatched
    #     self.orderbook = get_orderbook(self.event_id)
    #     # orderbook
    #     self.assertListEqual(self.orderbook.sell_orders, [
    #         {
    #             "price": 4,
    #             "quantity": 10,
    #             "user_id": 1
    #         },
    #     ], "sell order created for user1 @ price 10-n")
    #     self.assertListEqual(self.orderbook.buy_orders, [
    #         {
    #             "price": 7,
    #             "quantity": 8,
    #             "user_id": 4
    #         },
    #     ], "sell order created for user1 @ price 10-n")

    #     # userBalance
    #     user4_balance = get_user_balance(4)
    #     self.assertEqual(user4_balance.total_balance, 1455)
    #     self.assertEqual(user4_balance.locked_balance, 24)

    #     # user2Balance
    #     user2_balance = get_user_balance(2)
    #     self.assertEqual(user2_balance.total_balance, 1395)
    #     self.assertEqual(user2_balance.locked_balance, 0)

    #     # stockBalance
    #     stock_balance = get_stock_balance(4)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 7)

    #     # stock2Balance
    #     stock_balance = get_stock_balance(2)
    #     self.assertEqual(stock_balance.get_stock_item(self.event_id).quantity, 15)


if __name__ == "__main__":
    unittest.main()
