from datetime import datetime

from assertpy import assert_that, soft_assertions
from behave import use_step_matcher, step
from dateutil.parser import parse

from requests import Session
from requests.auth import HTTPBasicAuth

use_step_matcher("re")

class HttpMethods:
    def __init__(self, url:str=' https://httpbin.org'):
        self.url = url
        self.session = Session()
        self.session.headers.update({"Content-Type": "application/json"})
        self.session.headers.update({"Accept": "application/json"})

    def delete(self):
        return self.session.delete(f'{self.url}/delete')

    def get(self):
        return self.session.get(f'{self.url}/get')

    def patch(self):
        return self.session.patch(f'{self.url}/patch')

    def post(self):
        return self.session.post(f'{self.url}/post')

    def put(self):
        return self.session.put(f'{self.url}/put')

    # basic auth
    def basic_auth(self, username:str='olle', password:str='liten'):
        #self.session.auth = (username, password)
        basic = HTTPBasicAuth('user', 'pass')
        #return self.session.get(f'{self.url}/basic-auth'/{username}/{password}')
        return self.session.get(f'{self.url}/basic-auth', auth=basic)


    # status code
    def delete_status_code(self, status_code:int):
        return self.session.delete(f'{self.url}/status/{status_code}')

    # request inspection
    def headers(self):
        return self.session.get(f'{self.url}/headers')

    def ip(self):
        return self.session.get(f'{self.url}/ip')

    def user_agent(self):
        return self.session.get(f'{self.url}/user-agent')

@step("we delete")
def step_impl(context):
    context.response = context.http_methods.delete()


@step("we should get a 200 status code")
def step_impl(context):
    with soft_assertions():
        assert_that(context.response.status_code).is_http_ok()
        assert_that(parse(context.response.headers['Date'])).is_type_of(datetime)

@step("setup for http methods")
def step_impl(context):
        context.http_methods = HttpMethods()


@step("we get")
def step_impl(context):
    context.response = context.http_methods.get()


@step("we head")
def step_impl(context):
        context.response = context.http_methods.head()



@step("we options")
def step_impl(context):
        context.response = context.http_methods.options()


@step("we patch")
def step_impl(context):
        context.response = context.http_methods.patch()



@step("we post")
def step_impl(context):
        context.response = context.http_methods.post()



@step("we put")
def step_impl(context):
        context.response = context.http_methods.put()


@step("we should get a Unauthorized")
def step_impl(context):
            assert_that(context.response.status_code).is_http_not_found()
