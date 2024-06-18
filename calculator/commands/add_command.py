from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import add

class AddCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, add)

    def execute(self):
        return self.calculation.get_result()
