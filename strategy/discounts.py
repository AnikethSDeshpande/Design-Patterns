'''
    In ecommerce, there are many offers and subsequent discounts 
    that could be applicable to a customer on his invoice.
    
    Lets apply offers using strategy pattern.
'''


from __future__ import annotations
from abc import ABC, abstractmethod


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate_discount(self, invoice_total):
        pass


class Invoice:
    def __init__(self, name: str, items: list, invoice_total: int):
        self.name = name
        self.items = items
        self.invoice_total = invoice_total
        self.invoice_discount = 0
    
    def apply_discount(self, discount_strategy = None) -> Invoice:
        if discount_strategy:
            self.invoice_discount += discount_strategy().calculate_discount(self.invoice_total)
        
        return self
        
    def total_after_discount(self):
        return self.invoice_total - self.invoice_discount


class DiwaliDiscount(DiscountStrategy):
    def calculate_discount(self, invoice_total):
        if invoice_total <= 1000:
            return invoice_total * 0.1
        
        if 1000 < invoice_total < 5000:
            return invoice_total * 0.2

        if 5001 < invoice_total < 10000:
            return invoice_total * 0.3
        
        if 10001 < invoice_total < 15000:
            return invoice_total * 0.35


class BBDayDiscount(DiscountStrategy):
    def calculate_discount(self, invoice_total):
        if invoice_total <= 1000:
            return invoice_total * 0.1
        
        if 1001 < invoice_total < 5000:
            return invoice_total * 0.3

        if 5001 < invoice_total < 10000:
            return invoice_total * 0.35
        
        if 10001 < invoice_total < 15000:
            return invoice_total * 0.40


class EngineersDayDiscount(DiscountStrategy):
    def calculate_discount(self, invoice_total):
        return invoice_total * 0.10


def print_invoice(context, invoice):
    print(f'''
        During {context},
        {invoice.name}'s invoice total is: {invoice.invoice_total} 
        {invoice.name}'s invoice total after discount is: {invoice.total_after_discount()}'
    ''')


def main():
    # During Diwali
    invoice = Invoice('Ram', ['Carrot', 'Ghee', 'Dry Fruits'], 1000)
    invoice.apply_discount(DiwaliDiscount)
    
    print_invoice('Diwali', invoice)

    # BBDay as well as EngineersDay discount applied together
    invoice = Invoice('Ram', ['Carrot', 'Ghee', 'Dry Fruits', 'Paneer'], 3000)
    invoice.apply_discount(BBDayDiscount)
    invoice.apply_discount(EngineersDayDiscount)

    print_invoice('BBD + EngDay', invoice)


if __name__ == '__main__':
    main()
