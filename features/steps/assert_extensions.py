import requests
from assertpy import add_extension


def is_http_ok(self):
    if requests.codes.ok != self.val:
        self.error(f"{self.val} is not equal to {requests.codes.ok}")
    return self


def is_http_internal_server_error(self):
    if requests.codes.internal_server_error != self.val:
        self.error(
            f"{self.val} is not equal to {requests.codes.internal_server_error}"
        )
    return self


def is_http_bad_request(self):
    if requests.codes.bad_request != self.val:
        self.error(f"{self.val} is not equal to {requests.codes.bad_request}")
    return self


def is_http_live_delay_pending(self):
    if requests.codes.payment_required != self.val:
        self.error(
            f"{self.val} is not equal to {requests.codes.payment_required}"
        )
    return self


def is_http_not_found(self):
    if requests.codes.not_found != self.val:
        self.error(f"{self.val} is not equal to {requests.codes.not_found}")
    return self

def is_http_not_authorized(self):
    if requests.codes.unauthorized != self.val:
        self.error(f"{self.val} is not equal to {requests.codes.unauthorized}")
    return self

def add_assert_extensions():
    add_extension(is_http_ok)
    add_extension(is_http_bad_request)
    add_extension(is_http_live_delay_pending)
    add_extension(is_http_internal_server_error)
    add_extension(is_http_not_found)
    add_extension(is_http_not_authorized)
