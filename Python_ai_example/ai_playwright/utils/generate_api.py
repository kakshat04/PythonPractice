from utils.openai_utils import generate_message

def generate_api_tests(api_name):
    prompt = f"""
    Generate Gherkin file for testing the {api_name} API. The scenario should:
    - be prices and focus only on the Status API
    - Include Minimal steps
    - Base URL is "https://goal-tracker-api.onrender.com/"
    - endpoint is /status

    Example cases to consider:
    - successful request & response will contain "OPERATIONAL"
    """
    return generate_message(prompt)

if __name__ == "__main__":
    gherin_message = generate_api_tests("goal-tracker-api")
    print(gherin_message)

    