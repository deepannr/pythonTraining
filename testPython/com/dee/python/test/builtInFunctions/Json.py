import json
print("Json:", dir(json))
data = {"Name": "DeeS", "Age": 38}
print("Type:", type(data))
json_data = json.dumps(data)
print("Type:", type(json_data))
print("JSON data:", json_data)