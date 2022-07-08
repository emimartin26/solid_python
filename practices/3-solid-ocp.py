
from abc import ABC, abstractstaticmethod
import os
import sys


class PaymentMethod(ABC):
    @abstractstaticmethod
    def meets_condition(self):
        pass

class CreditCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "credit_card"


class DebitCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "debit_card"


class BankTransfer(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "bank_transfer"


class PaymentReader:
    def read_payments(self):
        with open(os.path.join(sys.path[0], "payments.jsonl"), "r") as f:
            return f.read()


class Output:
    def notify_payment(self, raw_data):
        print("Notifying payment...", raw_data)


class PaymentManager:
    def __init__(self, raw_data):
        self.raw_data = raw_data
        self.payment_reader = PaymentReader()
        self.output = Output()

    def load_payments(self):
        return self.payment_reader.read_payments()

    def identify_payment(self):
        for payment_method_cls in PaymentMethod.__subclasses__():
            if payment_method_cls.meets_condition(self.raw_data):
                return payment_method_cls()

    def notify_payment(self):
        self.output.notify_payment(self.raw_data)


if __name__ == "__main__":
    p1 = PaymentManager({
        "amount": "100",
        "reference": "iphone 13 pro",
        "payer_id": "808",
        "collector_id": "707",
        "card_issuer": "100",
        "card_number": "xxxxxxxxxxx",
        "country": "argentina",
        "type": "bank_transfer"
    })

    print(p1.identify_payment().__class__.__name__)
