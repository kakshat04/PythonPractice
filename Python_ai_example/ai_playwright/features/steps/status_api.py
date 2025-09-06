from behave.api.pending_step import StepNotImplementedError
from behave import given, then, when
from utils.types import CustomContext
import requests
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@given('The base URL is "{base_url}"')
def step_impl(context: CustomContext, base_url):
    context.base_url = base_url


@when('A user sends a GET request to "{endpoint}" endpoint')
def step_impl(context: CustomContext, endpoint):
    url = f'{context.base_url}{endpoint}'
    response = requests.get(url=url)
    print(response)


@then('The response status code should be 200')
def step_impl(context):
    raise StepNotImplementedError('Then The response status code should be 200')


@then('The response should contain "OPERATIONAL"')
def step_impl(context):
    raise StepNotImplementedError('Then The response should contain "OPERATIONAL"')