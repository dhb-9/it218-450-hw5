from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import multiply

class MultiplyCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, multiply)

    def execute(self):
        return self.calculation.get_result()
