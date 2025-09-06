"""
Given a test result JSON like:

{
  "test_login": "passed",
  "test_register": "failed",
  "test_api_status": "skipped",
  "test_turbine_output": "passed"
}

Write a script to:

Count how many tests passed, failed, or were skipped.

Print a summary like:
Passed: 2, Failed: 1, Skipped: 1
"""

import json

data = json.loads(open('test_report.json').read())
print(data)

passed = 0
failed = 0
skipped = 0
for data, result in data.items():
    if result == "passed":
        passed += 1
    elif result == "failed":
        failed += 1
    elif result == "skipped":
        skipped += 1
    else:
        print("Invalid result")
print("Passed: {}, Failed: {}, Skipped: {}".format(passed, failed, skipped))