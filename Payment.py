import logging

# logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

class Payment:
    def __init__(self, amount: float):
        self.amount = amount

    def process_payment(self) -> bool:
        return False

class CreditCardPayment(Payment):
    def __init__(self, amount: float, card_number: str, expiry_date: str, cvv: str):
        super().__init__(amount)
        self.card_number = card_number
        self.expiry_date = expiry_date
        self.cvv = cvv

    def process_payment(self) -> bool:
        if len(self.card_number) != 16:
            return False
        # payment processing logic
        return True

class PayPalPayment(Payment):
    def __init__(self, amount: float, email: str):
        super().__init__(amount)
        self.email = email

    def process_payment(self) -> bool:
        if self.is_email_valid(self.email):
            return False
        # payment processing logic
        return True
    
    def is_email_valid(self, email):
        # todo: email validation
        return "@" in email

def main() -> list:
    # Create instances
    # valid payment
    credit_card_payment = CreditCardPayment(150.0, "1234567812345678", "12/24", "123")
    paypal_payment = PayPalPayment(75.0, "customer@example.com")
    # Invalid
    invalid_credit_card_payment = CreditCardPayment(200.0, "1234", "01/23", "999") 
    invalid_paypal_payment = PayPalPayment(50.0, "customerexample.com")         

    payments = [
        credit_card_payment,
        paypal_payment,
        invalid_credit_card_payment,
        invalid_paypal_payment
    ]

    results = []
    for payment in payments:
        results.append(payment.process_payment())

    return results


if __name__ == "__main__":
    final_results = main()
    logging.info("Final Payment Results: %s", final_results)
