from behave import *

use_step_matcher("re")


@given("at the login screen")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass