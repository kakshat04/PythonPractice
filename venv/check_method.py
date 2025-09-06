def check_divisibility_by_3():
    new_list = [f"{number} is divisible by 3" if number % 3==0 else f"{number} is not divisible by 3"
                for number in range(1,10)]
    return new_list

print(check_divisibility_by_3())

import json
def get_user_email(json_input):
    json_data = json.loads(json_input)
    return json_data["email"]

json_input = '{"name": "John Doe", "email": "john.doe@example.com", "age": 30}'
print(get_user_email(json_input))