from pprint import pprint

from assertpy import assert_that
from behave import use_step_matcher,step

use_step_matcher("re")


@step("we get headers")
def step_impl(context):
    context.response = context.http_methods.headers()

from pydantic import BaseModel
from ipaddress import IPv4Address

class MyModel(BaseModel):
    ip: IPv4Address

@step("we shold read stuff")
def step_impl(context):
    pprint(context.response.json())
    print('*'*80)
    pprint(context.response.headers)


@step("we get ip addr")
def step_impl(context):
    context.response = context.http_methods.ip()


@step("we verify ip addr")
def step_impl(context):
    my_instance = MyModel(ip=context.response.json()['origin'])
    print(my_instance)


@step("we get user agent")
def step_impl(context):
    context.response = context.http_methods.user_agent()


@step("we verify user agent")
def step_impl(context):
    assert_that(context.response.json()['user-agent']).is_equal_to('python-requests/2.31.0')