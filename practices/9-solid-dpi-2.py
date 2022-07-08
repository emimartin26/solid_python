
from abc import ABC, abstractmethod, abstractstaticmethod
import os
import sys

class DataSourceReader(ABC):
    @abstractmethod
    def read_data(self):
        pass

class FileDataSourceReader(DataSourceReader):
    def read_data(self):
        with open(os.path.join(sys.path[0], "payments.jsonl"), "r") as f:
            return f.read()

class MemoryDataSourceReader(DataSourceReader):
    def read_data(self):
        return '{"amount":"100","reference":"iphone 13 pro","payer_id":"808","collector_id":"707","card_issuer":"100","card_number":"xxxxxxxxxxx","country":"argentina","type":"credit_card"}'


class PaymentReader:
    def __init__(self, reader: DataSourceReader):
        self.reader = reader 

    def read_payments(self):
        return self.reader.read_data()


class PaymentManager:
    def __init__(self, raw_data=None):
        self.raw_data = raw_data 
        self.payment_reader = PaymentReader(MemoryDataSourceReader())

    def load_payments(self):
        return self.payment_reader.read_payments()

    def identify_payment(self):
        pass

    def notify_payment(self):
        pass


if __name__ == "__main__":
    p1 = PaymentManager()

    print(p1.load_payments())
