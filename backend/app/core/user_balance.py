class UserBalance:
    def __init__(self):
        self.data = {

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
    


