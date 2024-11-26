from behave import given, when, then
from calculator import add,subtract,multiply,divide 
import math

@given('the calculator is initialized')  
def step_given_calculator_initialized(context):  
    context.result = None 

@when('I add {num1:d} and {num2:d}')  
def step_add(context, num1, num2):  
    context.result = add(num1, num2)  

@when('I subtract {num1:d} from {num2:d}')  
def step_subtract(context, num1, num2):  
    context.result = subtract(num2, num1) 

@when('I multiply {num1:d} and {num2:d}')  
def step_multiply(context, num1, num2):  
    context.result = multiply(num1, num2)  

@when('I divide {num1:d} by {num2:d}')  
def step_divide(context, num1, num2):  
    context.result = divide(num1, num2)  


@then('the result should be {expected_result:d}')  
def step_check_result(context, expected_result):  
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"