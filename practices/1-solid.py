
import os
import sys


class PaymentMethod:
    pass


class CreditCard(PaymentMethod):
    pass


class DebitCard(PaymentMethod):
    pass


class PaymentManager:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    def load_payments(self):
        with open(os.path.join(sys.path[0], "payments.jsonl"), "r") as f:
            return f.read()

    def identify_payment(self):
        if self.raw_data["type"] == "credit_card":
            return CreditCard()
        elif self.raw_data["type"] == "debit_card":
            return DebitCard()

    def notify_payment(self):
        print("Notifying payment...", self.raw_data)


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

    print(p1.identify_payment().__class__.__name__)

    p2 = PaymentManager({
        "amount": "100",
        "reference": "iphone 13 pro",
        "payer_id": "808",
        "collector_id": "707",
        "card_issuer": "100",
        "card_number": "xxxxxxxxxxx",
        "country": "argentina",
        "type": "debit_card"
    })

    print(p2.identify_payment().__class__.__name__)
    