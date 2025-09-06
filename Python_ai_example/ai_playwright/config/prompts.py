# import json

prompts = {
    "contact_us_form": """
    Feature: Contact Us Form

    Write Gherkin scenarios for testing a Contact Us form with the following details:
    - The form contains input fields: 'First Name', 'Last Name', 'Email Address', and 'Comments'.
    - All fields are mandatory.
    - The 'SUBMIT' button submits the form.
    - The 'RESET' button clears all fields.
    - The email address must be valid and contain an '@' symbol.
    - A success message is displayed for valid submissions: 'Thank You for your Message'.
    - Error messages:
      - 'Error: Invalid email address'
      - 'Error: All fields are required'.

    Generate scenarios for:
    1. Valid form submission.
    2. Missing fields.
    3. Invalid email address.
    4. Using the 'RESET' button.

    Do not use code formatting tags like ```gherkin or ```. Output plain Gherkin syntax only.
    """,
    "login_form": """
    Feature: Login Form

    Write Gherkin scenarios for testing a Login form with the following details:
    - The form contains input fields: 'Username' and 'Password'.
    - Both fields are mandatory.
    - The 'LOGIN' button attempts to log the user in.
    - The 'FORGOT PASSWORD' link navigates to the password recovery page.
    - Success message: 'Login successful'.
    - Error messages:
      - 'Error: Invalid username or password'
      - 'Error: Both fields are required'.

    Generate scenarios for:
    1. Successful login.
    2. Missing fields.
    3. Invalid username or password.
    4. Clicking on 'FORGOT PASSWORD'.

    Do not use code formatting tags like ```gherkin or ```. Output plain Gherkin syntax only.
    """
}

# Pretty-print the JSON data with indentation for readability
# print(json.dumps(prompts, indent=2)) 
