from assertpy import assert_that
from behave import *

use_step_matcher("re")


@when("setup delete to reply with (.*)")
def step_impl(context,status_code):
    context.status_code = int(status_code)
    context.response = context.http_methods.delete_status_code(context.status_code)


@then("we should this reply")
def step_impl(context):
    assert_that(context.response.status_code).is_equal_to(context.status_code)