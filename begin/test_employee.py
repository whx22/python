import pytest

from employee import Employee

# def test_give_default_raise():
#     example_employee = Employee("Huxin", "Wang", 150000)
#     example_employee.give_raise()
#     assert example_employee.salary == 155000
#
# def test_give_custom_raise():
#     example_employee = Employee("Huxin", "Wang", 150000)
#     example_employee.give_raise(10000)
#     assert example_employee.salary == 160000

"""
Use fixture create test class
Avoid creating class repeatedly
"""

@pytest.fixture
def example_employee():
    example_employee = Employee("Huxin", "Wang", 150000)
    return example_employee

def test_give_default_raise(example_employee):
    example_employee.give_raise()
    assert example_employee.salary == 155000

def test_give_custom_raise(example_employee):
    example_employee.give_raise(10000)
    assert example_employee.salary == 160000