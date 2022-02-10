a_dict = {"name":"kyle","address":"Boyd GRSC"}
a_dict['Phone'] = "706-583-8166"
a_dict['Phone'] = "706-583-8167"
print(list(a_dict.items())[2])
a_var = "name"
print(a_dict[a_var])

print("name" in a_dict)

#a_list = [1,2,3]

#print(4 in a_list)

print(list(a_dict.keys()))
print("kyle" in list(a_dict.values()))

a_dict = {}

a_dict["key1"] = {}
a_dict["key2"] = {}

a_dict["key1"]["values"] = []
a_dict["key1"]["single_value"] = 3

a_dict["key1"]["values"].append(4)
print(a_dict)

