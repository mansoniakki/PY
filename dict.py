empty_dict=dict()
print("empty_dict: ", empty_dict)
empty_dict={}
print("empty_dict: ", empty_dict)

print("Assigning value to dict")
dict_syn={'k1':'v1','k2':'v2'}
print("dict_syn: ", dict_syn)

print("assigning additional value to dict")
dict_syn['k3']='v3'
print("dict_syn: ", dict_syn)
print("Deleting the column")
del(dict_syn['k3'])
print("dict_syn: ", dict_syn)
print("changing value")
dict_syn['k1']= 100
print("dict_syn: ", dict_syn)
dict_syn['k2']= 50
print("dict_syn: ", dict_syn)
print("Using Reference and Copy")
dict_ref=dict_syn
dict_copy=dict.copy(dict_syn)
print("dict_syn: ", dict_syn)
print("dict_copy: ", dict_copy)
print("clearing original dict")#
dict_syn.clear()
print("dict_syn: ", dict_syn)
print("dict_copy: ", dict_copy)

print("making a list of keys from the dict")
key_list=dict_copy.copy().keys()
value_list = dict_copy.copy().values()

print("key_list ",key_list)
print("key_value",value_list)

mapping = zip(key_list, value_list)

print("mapping", mapping)
dict_new=dict(mapping)
print("dict_new: ", dict_new)