from playwright.sync_api import sync_playwright
from utils.openai_utils import generate_message, load_prompt

def check_navigation():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, args=["--start-maximized"])
        page = browser.new_page(no_viewport=True)
        page.goto("https://webdriveruniversity.com/Contact-Us/contactus.html")
        print(page.title())
        browser.close()

def generate_gherkin_scenarios():
    prompt = load_prompt("contact_us_form")
    gherkin_scenarios = generate_message(prompt)

    feature_file_path = "features/contact_us_form.feature"
    try:
        with open(feature_file_path, "x") as file:
            file.write(gherkin_scenarios)
            print(f"{feature_file_path} was successfully generated")
    except FileExistsError:
        print(f"{feature_file_path}  already exist")



if __name__ == '__main__':
    # check_navigation()
    # prompt = "Generate Gherkin scenario for testing login page"
    # print(check_openai_response(prompt))
    print(generate_gherkin_scenarios())