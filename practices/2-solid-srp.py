
import os
import sys


class PaymentMethod:
    pass


class CreditCard(PaymentMethod):
    pass


class DebitCard(PaymentMethod):
    pass


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
        if self.raw_data["type"] == "credit_card":
            return CreditCard()
        elif self.raw_data["type"] == "debit_card":
            return DebitCard()

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
        "type": "credit_card"
    })

    print(p1.load_payments())
    
    p1.notify_payment()