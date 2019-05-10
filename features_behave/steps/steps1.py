from behave import when, then, given
import time

# For feature file 1
@given(u': 2 integers')
def step_impl(context):
    time.sleep(0.5)
    print("Enter two numbers")

@when(u': sum method is called')
def step_impl(context):
    print("Sum method is invoked")


@then(u': It should return sum of numbers')
def step_impl(context):
    print("Sum of the numbers is printed")


@when(u': multiply method is called')
def step_impl(context):
    print("Multiply method is invoked")


@then(u': It should return product of numbers')
def step_impl(context):
    print("Product of numbers is returned")
    assert 1 > 2      ## This will fail

