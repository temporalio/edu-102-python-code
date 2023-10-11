from dataclasses import dataclass
from typing import List

TASK_QUEUE_NAME = "pizza-tasks"
WORKFLOW_ID_PREFIX = "pizza-workflow-order-"


@dataclass
class Address:
    line1: str
    line2: str
    city: str
    state: str
    postal_code: str


@dataclass
class Bill:
    customer_id: int
    order_number: str
    description: str
    amount: int


@dataclass
class Customer:
    customer_id: int
    name: str
    email: str
    phone: str


@dataclass
class Distance:
    kilometers: int


@dataclass
class OrderConfirmation:
    order_number: str
    status: str
    confirmation_number: str
    billing_timestamp: int
    amount: int


@dataclass
class Pizza:
    description: str
    price: int


@dataclass
class PizzaOrder:
    order_number: str
    customer: Customer
    items: List[Pizza]
    is_delivery: bool
    address: Address
