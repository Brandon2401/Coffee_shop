import pytest
from coffee import Coffee
from customer import Customer
from order import Order




def setup_function():
	Customer._all.clear()
	Coffee._all.clear()
	Order._all.clear()




def test_coffee_name_validation():
  with pytest.raises(TypeError):
    Coffee(123)
with pytest.raises(ValueError):
    Coffee('ab')
c = Coffee('Americano')
assert c.name == 'Americano'




def test_num_and_avg():
  cust = Customer('C')
  coff = Coffee('Brew')
  cust.create_order(coff, 3.0)
  cust.create_order(coff, 5.0)
  assert coff.num_orders() == 2
  assert coff.average_price() == pytest.approx(4.0)