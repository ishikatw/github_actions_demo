from behave import given, when, then
from calculator import Calculator

@given("I have a calculator")
def step_impl_given_calculator(context):
    context.calculator =Calculator()

@when("I add {a:d} and {b:d}")
def step_impl_when_add(context, a, b):
    context.result = context.calculator.add(a, b)

@when("I subtract {a:d} from {b:d}")
def step_impl_when_subtract(context, a, b):
    context.result = context.calculator.subtract(b, a)

@then("the result should be {expected:d}")
def step_impl_then_result(context, expected):
    assert context.result == expected, f"Expected {expected}, but got {context.result}"
