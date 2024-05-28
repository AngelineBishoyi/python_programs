import json
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print(type(python_obj))
j_str = {'4': 5, '6': 7, '1': 3, '2': 4}
print(json.dumps(j_str,sort_keys=True,indent=4))

json1= '{"a":  1, "a":  2, "a":  3, "a": 4, "b": 1, "b": 2}'
print("Original Python object:")
print(json1)
py_ob = json.loads(json1)
print("\nUnique Key in a JSON object:")
print(type(py_ob))
print(py_ob)

with open(demo)