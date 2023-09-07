from abc import ABC, abstractmethod


class User:
    def __init__(self, name, card_name, cvv):
        self.name = name
        self.card_name = card_name
        self.cvv = cvv


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class PaymentSystem(ABC):
    @abstractmethod
    def checkout(self, product: Product, user: User):
        pass


class PayPal(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with PayPal for {user.name}\n"
            f"The product: {product.name} [{product.price}]"
        )


class Stripe(PaymentSystem):
    def checkout(self, product: Product, user: User):
        print(
            f"Checking out with Stripe for {user.name}\n"
            f"The product: {product.name} [{product.price}]"
        )


def make_purchace(
    payment_system: PaymentSystem,
    product: Product,
    user: User,
):
    print(
        f"{user.name} making a purchace - {product.name} for {product.price} UAH"
    )
    payment_system.checkout(product=product, user=user)


john = User(
    name="John",
    card_name="4444-1111-3333-5555",
    cvv="123",
)
paypal = PayPal()
stripe = Stripe()
shoes = Product(name="Adidas", price=5000)

make_purchace(
    user=john,
    payment_system=paypal,
    product=shoes,
)
make_purchace(
    user=john,
    payment_system=stripe,
    product=shoes,
)