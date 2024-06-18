from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import divide

class DivideCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, divide)

    def execute(self):
        return self.calculation.get_result()
