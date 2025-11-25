import pytest
from customer import Customer
from coffee import Coffee
from order import Order


def setup_function(function):
    Customer.all.clear()
    Coffee.all.clear()
    Order.all.clear()


def test_customer_name_validation():
    with pytest.raises(TypeError):
        Customer(123)
    with pytest.raises(ValueError):
        Customer("")
    with pytest.raises(ValueError):
        Customer('a' * 16)
    c = Customer('Tom')
    assert c.name == 'Tom'


def test_create_order_and_relations():
    c = Customer('Sam')
    coff = Coffee('Mocha')
    order = c.create_order(coff, 4.0)
    assert order in Order.all
    assert order in c.orders()
    assert order in coff.orders()


def test_most_aficionado():
    a = Customer('A')
    b = Customer('B')
    coffee = Coffee('Flatwhite')

    a.create_order(coffee, 5.0)
    a.create_order(coffee, 3.0)
    b.create_order(coffee, 2.0)
    assert Customer.most_aficionado(coffee) is a

