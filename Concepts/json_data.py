import json

json_data = '[{"ID":10,"Name":"Pankaj","Role":"CEO"},' \
            '{"ID":20,"Name":"David Lee","Role":"Editor"}]'

json_data = '{"username": "KumarRaJ", "active": true, "subscribers": 237612, "order_total": 39.99, "movies_watcghed": ["RRR", "titanic", "superman"], "favoirurte_food": ["fish rice", "chicken grilled", "fruits shake"], "workout_format": ["yoga", "boxing", "core -workout"],' \
            ' "company_employeed": ["Shell", "Telstra", "Cisco"]}'

json_object = json.loads(json_data)
json_formatted_str = json.dumps(json_object, indent=2)
print(json_formatted_str)