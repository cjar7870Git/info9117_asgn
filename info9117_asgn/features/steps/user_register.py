from behave import *
import re


@given ("at the register screen")
def step_impl(context):
    context.browser.get(context.address + "/register")
    register_found = re.search("register", context.browser.page_source, re.IGNORECASE)
    assert register_found

@when("I submit a unique {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)

@when("I submit an existing {username} and {password}")
def step_impl(context, username, password):
    """
    :type context: behave.runner.Context
    :type username: str
    :type password: str
    """
    submit_username_password(context, username, password)

@then('the system should return "{text}" as the registration status of the user')
def step_impl(context, text):
    """
    :type context: behave.runner.Context
    """
    assert text in context.response


def submit_username_password(context, username, password):
    username_field = context.browser.find_element_by_name("username")
    password_field = context.browser.find_element_by_name("password")
    username_field.send_keys(username)
    password_field.send_keys(password)
    username_field.submit()
    context.response = context.browser.page_source

