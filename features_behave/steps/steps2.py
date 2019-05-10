from behave import when, then, given
import time

# For feature file 2
@when(u': subtract method is called')
def step_impl(context):
    print("Subtract method is invoked")


@then(u': It should return difference of numbers')
def step_impl(context):
    print("Difference of numbers is returned")


@when(u': divide method is called')
def step_impl(context):
    print("Divide method is invoked")


@then(u': It should return result of division')
def step_impl(context):
    print("Result of division of numbers is returned")
