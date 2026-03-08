# Dictionary
# info= {
#     "name": "Ahmad",
#     "age": 22,
#     "subjects": ["English","Math","Computer"],
#     "is_adult": True,
#     "marks" :887
# }
# print(type(info))
# print(info)
# info["name"]="Ali"
# print(info)

# Nested dictionary
# info= {
#     "name": "Ahmad",
#     "age": 22,
#     "subjects": {
#         "Eng":89,
#         "Math":87,
#         "Com":94
#     },
#     "is_adult": True,
#     "marks" :887
# }
# print(info["subjects"])

# Methods
# info= {
#     "name": "Ahmad",
#     "age": 22,
#     "subjects": ["English","Math","Computer"],
#     "is_adult": True,
#     "marks" :887
# }
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("subjects"))

# Sets
# collection={1,2,2,3,4,4}
# print(collection)
# print(len(collection))
# collection.add(8)
# print(collection)
# collection.remove(2)
# print(collection)
# collection.clear()
# print(collection)

# Union
# set1={1,2,3,6,8}
# set2={2,4,6,8,9}
# print(set1.union(set2))

# Intersection
# set1={1,2,3,6,8}
# set2={2,4,6,8,9}
# print(set1.intersection(set2))

# Practice question
# marks = {}
# x=int(input("Enter phy marks : "))
# marks.update({"Phy":x})
# x=int(input("Enter che marks : "))
# marks.update({"Che":x})
# x=int(input("Enter math marks : "))
# marks.update({"Math":x})
# print(marks)