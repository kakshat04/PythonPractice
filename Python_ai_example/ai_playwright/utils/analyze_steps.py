from utils.openai_utils import generate_message

def analyze_steps(file_path):
    try:
        with open(file_path, "r") as file:
            steps = file.read()
    except FileNotFoundError:
        print(f"Error :: {file_path} not found")
        return
    

    environment_context = """
    The automation framework is already set up to initialize Playwright in environment.py.
    This includes setting up the browser, creating a new page, and managing teardown processes.
    Avoid reinitializing Playwright in step definitions as it is redundant.
    You can access the current page using 'context.page'.
    """

    prompt = f"""
    {environment_context}

    Analyze following behave steps definition.
    For each unimplemented steps, provide python code to implement it, using playwright for browser automation

    Behave steps:
    {steps}
    """

    suggestions = generate_message(prompt)
    print(suggestions)


if __name__ == "__main__":
    analyze_steps("features/steps/contact_us_form_steps.py")
