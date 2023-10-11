from dataclasses import dataclass

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
