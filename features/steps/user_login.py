from behave import *


@given("at the login screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("an existing user submits the correct username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@then('the system should return "Success" as the authentication status of the user')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("an existing user submits the incorrect username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass


@when("an unknown user submits some username and password")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass