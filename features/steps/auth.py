from behave import use_step_matcher, step

use_step_matcher("re")


@step("we get basic auth")
def step_impl(context):
    context.response = context.http_methods.basic_auth()