from decimal import Decimal
from calculator.calculation import Calculation
from calculator.operations import subtract

class SubtractCommand:
    def __init__(self, a: Decimal, b: Decimal):
        self.calculation = Calculation(a, b, subtract)

    def execute(self):
        return self.calculation.get_result()
