
from abc import ABC, abstractmethod, abstractstaticmethod
import os
import sys


class PaymentMethod(ABC):
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @abstractstaticmethod
    def meets_condition():
        pass
    
    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def show_card_info(self):
        pass

class CreditCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "credit_card"
    
    def pay(self):
        print("Paying with debit card...", self.raw_data["card_number"])

    def show_card_info(self):
        print("Card number:", self.raw_data["card_number"])
        print("Expiration date:", self.raw_data["expiration_date"])
        print("CVV:", self.raw_data["cvv"])

class DebitCard(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "debit_card"

    def pay(self):
        print("Paying with debit card...", self.raw_data["card_number"])

    def show_card_info(self):
        print("Card number:", self.raw_data["card_number"])
        print("Expiration date:", self.raw_data["expiration_date"])


class BankTransfer(PaymentMethod):
    @staticmethod
    def meets_condition(raw_data):
        return raw_data.get("type") == "bank_transfer"

    def pay(self):
        print("Paying with bank transfer...", self.raw_data["bank_account_number"])
    
    def show_card_info(self):
        raise Exception("Bank transfer does not have card info")

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
                return payment_method_cls(self.raw_data)

    def notify_payment(self):
        self.output.notify_payment(self.raw_data)


def process_payment(payment_method: PaymentMethod):
   payment_method.pay()


if __name__ == "__main__":
    p1 = PaymentManager({
        "amount": "100",
        "reference": "iphone 13 pro",
        "payer_id": "808",
        "collector_id": "707",
        "card_issuer": "100",
        "card_number": "xxxxxxxxxxx",
        "expiration_date": "12/20",
        "country": "argentina",
        "type": "credit_card",
        "cvv": "123"
    })

    pay_method = p1.identify_payment()

    pay_method.show_card_info()

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

    pay_method.show_card_info()
