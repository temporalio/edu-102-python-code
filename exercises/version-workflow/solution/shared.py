from dataclasses import dataclass

from shared import Address, Customer, Pizza, PizzaOrder

TASK_QUEUE_NAME = "loan-processing-workflow-taskqueue"
WORKFLOW_ID_PREFIX = "loan-processing-workflow-customer-"


@dataclass
class ChargeInput:
    customer_id: str
    amount: int
    period_number: int
    number_of_periods: int


@dataclass
class CustomerInfo:
    customer_id: str
    name: str
    email_address: str
    amount: int
    number_of_periods: int


def create_customer_info_db() -> dict[str, CustomerInfo]:
    customer1 = CustomerInfo(
        customer_id="a100",
        name="Ana Garcia",
        email_address="ana@example.com",
        amount=500,
        number_of_periods=10,
    )
    customer2 = CustomerInfo(
        customer_id="a101",
        name="Amit Singh",
        email_address="asingh@example.com",
        amount=250,
        number_of_periods=15,
    )
    customer3 = CustomerInfo(
        customer_id="a102",
        name="Mary O'Connor",
        email_address="marymo@example.com",
        amount=425,
        number_of_periods=12,
    )

    return {
        customer1.customer_id: customer1,
        customer2.customer_id: customer2,
        customer3.customer_id: customer3,
    }


def create_pizza_order() -> PizzaOrder:
    customer = Customer(
        customer_id=8675309,
        name="Lisa Anderson",
        email="lisa@example.com",
        phone="555-555-0000",
    )
    address = Address(
        line1="741 Evergreen Terrace",
        line2="Apartment 221B",
        city="Albuquerque",
        state="NM",
        postal_code="87101",
    )
    pizza1 = Pizza(description="Large, with mushrooms and onions", price=1500)
    pizza2 = Pizza(description="Small, with pepperoni", price=1200)
    pizza3 = Pizza(description="Medium, with extra cheese", price=1300)

    pizza_list = [pizza1, pizza2, pizza3]

    pizza_order = PizzaOrder(
        order_number="XD001",
        customer=customer,
        items=pizza_list,
        is_delivery=True,
        address=address,
    )
    return pizza_order
