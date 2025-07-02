import json
name=input()
age=int(input())
data={"name":name,"age":age}
stringify_json=json.dumps(data)
print("serialized",stringify_json)