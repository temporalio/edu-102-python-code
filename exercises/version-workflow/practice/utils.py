from shared import PizzaOrder, Customer, Address, Pizza


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


def create_pizza_order_for_test() -> PizzaOrder:
    pizza_order = create_pizza_order()
    pizza_order.items = pizza_order.items[:-1]
    return pizza_order
