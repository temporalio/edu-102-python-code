import pytest
from activities import PizzaOrderActivities
from shared import Address, Bill, Distance
from temporalio.testing import ActivityEnvironment


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "input, output",
    [
        (
            Address(
                line1="701 Mission Street",
                line2="Apartment 9C",
                city="San Francisco",
                state="CA",
                postal_code="94104",
            ),
            Distance(20),
        ),
        (
            Address(
                line1="917 Delores Street",
                line2="",
                city="San Francisco",
                state="CA",
                postal_code="94104",
            ),
            Distance(8),
        ),
    ],
)
async def test_get_distance(input, output):
    activity_environment = ActivityEnvironment()
    activities = PizzaOrderActivities()
    assert output == await activity_environment.run(activities.get_distance, input)


@pytest.mark.asyncio
async def test_send_bill_typical_order():
    bill = Bill(
        customer_id=12983,
        order_number="XD001",
        description="2 large cheese pizzas",
        amount=2600,
    )
    activity_environment = ActivityEnvironment()
    activities = PizzaOrderActivities()
    confirmation = await activity_environment.run(activities.send_bill, bill)

    assert "XD001" == confirmation.order_number
    assert 2600 == confirmation.amount


@pytest.mark.asyncio
async def test_send_bill_typical_order():
    bill = Bill(
        customer_id=12983,
        order_number="XD001",
        description="2 large cheese pizzas",
        amount=2600,
    )
    activity_environment = ActivityEnvironment()
    activities = PizzaOrderActivities()
    confirmation = await activity_environment.run(activities.send_bill, bill)

    assert "XD001" == confirmation.order_number
    assert 2600 == confirmation.amount


# TODO implement test_send_bill_applies_discount


@pytest.mark.asyncio
async def test_send_bill_fails_negative_amount():
    bill = Bill(
        customer_id=21974,
        order_number="QU812",
        description="1 large supreme pizza",
        amount=-1000,
    )
    with pytest.raises(Exception) as e:
        activity_environment = ActivityEnvironment()
        activities = PizzaOrderActivities()
        await activity_environment.run(activities.send_bill, bill)
    assert "invalid charge amount" in str(e)
