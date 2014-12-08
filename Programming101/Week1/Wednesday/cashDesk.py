class CashDesk():

    money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, cash):
        self.cash = cash
        for item in self.cash:
            self.money[item] += self.cash[item]

    def total(self):
        sum = 0
        for item in self.money:
            sum += self.money[item] * item
        return sum

    def can_withdraw_money(self, money):
        cash = []
        for item in self.money:
            count = self.money[item]
            while count > 0:
                cash.append(item)
                count -= 1
        cash = sorted(cash, reverse=True)

        for item in cash:
            if money - item >= 0:
                money -= item
        if money == 0:
            return True
        return False
