from behave.__main__ import main as behave_main
import os

if __name__ == "__main__":
    os.makedirs("reports", exist_ok=True)
    behave_main(
        [
            "--tags", "@regression"
            "--format", "allure_behave.formatter:AllureFormatter",
            "--outfile", "reports/allure-results"
        ]
    )