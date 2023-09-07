from typing import Any


message = (
    "Vestibulum aliquet, felis ac ultrices auctor, augue ex sodales "
    "lectus, at commodo erat quam sed purus."
)


class PaymentSystem:
    def __init__(self, provider) -> None:
        self.provider: str = provider

    def foo(self):
        return "I am foo from Payment system"

    def __getattribute__(self, name: str) -> Any:
        if name == "password":
            return "Access denied!"

        # if name not in self.__dict__.keys():
        #     raise AttributeError(
        #         f"Your class does not have this field: {name}"
        #     )

        return super().__getattribute__(name)

    def get_attr(self, name: str) -> Any:
        if name not in self.__dict__.keys():
            raise AttributeError(
                f"Your class does not have this field: {name}"
            )

        return self.__dict__[name]


paypal = PaymentSystem(provider="PayPal")
print(paypal.__dict__)


# paypal.provider
# data = paypal.get_attr("providerss")
print(paypal.provider)