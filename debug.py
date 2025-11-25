# Quick interactive test script. Run `python debug.py`.
from customer import Customer
from coffee import Coffee


# Clear any previous class-level storage if re-running in the same process
Customer._all.clear()
Coffee._all.clear()


from order import Order
Order._all.clear()


# create sample data
alice = Customer('Alice')
bob = Customer('Bob')
latte = Coffee('Latte')
esp = Coffee('Espresso')


alice.create_order(latte, 4.5)
alice.create_order(latte, 5.0)
bob.create_order(latte, 3.0)
bob.create_order(esp, 2.5)


print('All orders:', Order.all())
print('Latte orders:', latte.num_orders())
print('Latte average:', latte.average_price())
print('Customers who ordered Latte:', latte.customers())
print('Alice coffees:', alice.coffees())
print('Most aficionado for Latte:', Customer.most_aficionado(latte))