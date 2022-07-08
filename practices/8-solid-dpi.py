
import os
import sys


class PaymentReader:
    def read_payments(self):
        with open(os.path.join(sys.path[0], "payments.jsonl"), "r") as f:
            return f.read()


class PaymentManager:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data 
        self.payment_reader = PaymentReader()

    def load_payments(self):
        return self.payment_reader.read_payments()

    def identify_payment(self):
        pass

    def notify_payment(self):
        pass


if __name__ == "__main__":
    p1 = PaymentManager()

    print(p1.load_payments())
