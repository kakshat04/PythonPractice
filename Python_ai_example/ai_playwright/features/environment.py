from utils.types import CustomContext
from playwright.sync_api import sync_playwright
import json
import logging
import allure
from allure_commons.types import AttachmentType

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def before_all(context:CustomContext):
    with open("config//env.json", "r") as json_file:
        logger.info("starting playwright")
        env_vars = json.load(json_file)
    context.browser_type = env_vars.get("browser", "chromium")
    context.headless_mode = env_vars.get("headless", False)

    context.playwright = sync_playwright().start()
    context.is_api_test = False
    

def before_scenario(context:CustomContext, scenario):
    logger.info(f"starting scenario: {scenario.name}")
    if "api" in scenario.tags:
        context.is_api_test = True
    else:
        context.is_api_test = False
        context.browser = context.playwright[context.browser_type].launch(headless=False, args=["--start-maximized"])
        context.page = context.browser.new_page(no_viewport=True)

def after_scenario(context:CustomContext, scenario):
    logger.info(f"finished scenario: {scenario.name[:-8]} & {scenario.status.error} ########")
    if scenario.status == "error" and context.is_api_test:
        screenshot_path = f"screenshot/{scenario.name[:-8].replace(" ", "_")}.png"
        context.page.screenshot(path=screenshot_path)
        logger.info(f"captured screenshot for failed scenario : {screenshot_path}")

        #attach screenshot
        with open(screenshot_path, "r") as image_file:
            logger.info("#################")
            allure.attach(image_file.read(), name=scenario.name, attachment_type=AttachmentType.png)

        context.page.wait_for_timeout(2000)
        context.page.close()

def after_all(context:CustomContext):
    logger.info("finished all scenarios, stopping playwright")
    context.browser.close()
    context.playwright.stop()
