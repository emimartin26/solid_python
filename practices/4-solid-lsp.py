
from abc import ABC, abstractmethod, abstractstaticmethod
import os
import sys


class PaymentMethod(ABC):

    @abstractstaticmethod
    def meets_condition():
        pass
    
    @abstractmethod
    def pay(self):
        pass

class CreditCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "credit_card"
    
    def pay(self, credit_card_number):
        print("Paying with credit card...")

class DebitCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "debit_card"

    def pay(self, debit_card_number):
        print("Paying with debit card...")

class BankTransfer(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "bank_transfer"

    def pay(self, bank_account_number):
        print("Paying with bank transfer...")

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


def process_payment(payment_method: PaymentMethod, raw_data):
    if isinstance(payment_method, CreditCard):
        payment_method.pay(raw_data.get("credit_card_number"))
    elif isinstance(payment_method, DebitCard):
        payment_method.pay(raw_data.get("debit_card_number"))
    elif isinstance(payment_method, BankTransfer):
        payment_method.pay(raw_data.get("bank_account_number"))

if __name__ == "__main__":
    p1 = PaymentManager({
        "amount": "100",
        "reference": "iphone 13 pro",
        "payer_id": "808",
        "collector_id": "707",
        "card_issuer": "100",
        "card_number": "xxxxxxxxxxx",
        "country": "argentina",
        "type": "credit_card"
    })

    pay_method = p1.identify_payment()

    process_payment(pay_method, p1.raw_data)

    p2 = PaymentManager({
        "amount": "100",
        "reference": "iphone 13 pro",
        "payer_id": "808",
        "collector_id": "707",
        "country": "argentina",
        "bank_account_number": "123456789",
        "type": "bank_transfer"
    })

    pay_method = p2.identify_payment()

    process_payment(pay_method, p1.raw_data)
