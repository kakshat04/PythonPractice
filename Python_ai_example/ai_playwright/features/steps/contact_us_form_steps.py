from behave import given, when, then
from utils.types import CustomContext
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# --- Navigation ---
@given('the user navigates to the Contact Us page')
def step_navigate_contact_us(context: CustomContext):
    context.page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")

# --- Data entry (parameterized) ---
@when('the user fills in "{field}" field with value "{value}"')
def step_fill_field(context:CustomContext, field, value):
   field_selector = f"[name={field}]"
   if value == "\\n":
       logger.info(f"Skipping {field} since value is {value}")
       return
   context.page.wait_for_selector(field_selector)
   context.page.fill(field_selector, value)
   logger.info(f"Filled {field} with {value}")


# --- Click actions (supports both phrasings) ---
@when('the user clicks the "{button}" button')
def step_click_button(context: CustomContext, button):
    button_selector = f"[value={button}]"
    context.page.wait_for_selector(button_selector)
    context.page.click(button_selector)

# --- Assertions: messages ---
@then('the user should see the success message saying "{message}"')
def step_see_success_message(context: CustomContext, message):
    success_message_selector = f'//*[contains(text(), "{message}")]'
    try:
        context.page.wait_for_selector(success_message_selector, timeout=2000)
        assert context.page.is_visible(success_message_selector)
        logger.info(f"Success Message '{message}' found")
    except TimeoutError:
        logger.error(f"Success Message '{message}' not found")
        assert False, f"Success Message '{message}' not found"

@then('the user should see an error message saying "{message}"')
def step_see_error_message(context, message):
    error_message_selector = f'//body[contains(., "{message}")]'
    try:
        context.page.wait_for_selector(error_message_selector, timeout=2000)
        assert context.page.is_visible(error_message_selector)
        logger.info(f"Error Message '{message}' found")
    except TimeoutError:
        logger.error(f"Error Message '{message}' not found")
        assert False, f"Error Message '{message}' not found"

# --- Assertions: reset behavior ---
@then('all fields in the form are cleared')
def step_fields_cleared(context):
    fields = ["first_name", "last_name", "email", "message"]
    all_cleared = True
    for field in fields:
        field_selector = f"[name={field}]"
        value = context.page.input_value(field_selector)
        if value != "":
            all_cleared = False
            logger.error(f"{value} field is not cleared")
            return all_cleared
        else:
            logger.info(f"{value} field is cleared successfully")
    return all_cleared

@then('the user should see the expected message saying "{expected_message}"')
def verify_expected_message(context: CustomContext, expected_message):
    message_selector = f'//*[contains(text(), "{expected_message}")] | //body[contains(., "{expected_message}")]'
    try:
        context.page.wait_for_selector(message_selector, timeout=2000)
        assert context.page.is_visible(message_selector)
        logger.info(f"Expected Message '{expected_message}' found")
    except TimeoutError:
        logger.error(f"Expected  Message '{expected_message}' not found")
        assert False, f"Expected  Message '{expected_message}' not found"