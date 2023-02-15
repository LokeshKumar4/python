# class currency :
#     amount=10

#     def changeCurrency(rupees):
#         return currency.amount+rupees

# print(currency.changeCurrency(100))

# ==================================================================================================================================

class currency :
    def __init__ (self,amount):
        self.amount=amount

    # @staticmethod
    @classmethod
    def changeCurrency(cls,amount,rupees):
        return cls(amount+rupees)

    def __repr__(self) -> str:
        return f"Currency - ${self.amount}"


class yen(currency):
    def __init__(self,amount):
        super().__init__(amount)
        self.symbol="¥"

    def __repr__(self) -> str:
        return f"the YEN currency symbol {self.symbol}={self.amount}"

y1=yen(50)
print(y1)
print(y1.changeCurrency(200,40))