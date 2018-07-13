print("##############Learning Sets Class###############")
empty_set = set()
print("empty_set: ",empty_set)
alpha=set(('a','b','c','d', 'Z', 'K'))
print("alpha: ", alpha)
dup_list=['a','b','b','c','d','d','e']
print("dup_list: ", dup_list)
beta = set(dup_list)
print('beta -> ', beta)
uniq_list = list(beta)
print("Uniq_list ", uniq_list)

print("alpha: ", alpha)

print("beta -> ", beta)

print("#######Union of two sets#########")
gamma=alpha.union(beta)

print("Gamma -> ",gamma)

print("Another way of UNION is using | ")
gamma1=alpha | beta
print("Gamma - another way of union -> ", gamma1)

print("#####Using Intersection ####")
delta=alpha.intersection(beta)
print("delta -> ", delta)

print("#####Using Intersection with & ####")
delta1=alpha & beta
print("delta using & ",delta1)

print("#####Finding Difference between sets using difference########")
epsilon=alpha.difference(beta)
print("epsilon -> ",epsilon)
print("###Finding difference using - ")
epsilon= alpha - beta
print("epsilon -> ", epsilon)

print("Symmetric difference is UNION - Intersection")
eta=alpha.symmetric_difference(beta)
print("eta -> ",eta)

print("Epsilon -> ", epsilon)
print("delta -> ", delta)
print("ets -> ",eta)
print("Epsilon isdisjoint delta -> ", epsilon.isdisjoint(delta))
print("Epsilon isdisjoint eta -> ",epsilon.isdisjoint(eta))
print("epsilon issubset eta -> ",epsilon.issubset(eta))
print("epsilon issubset beta -> ",epsilon.issubset(beta))

print("########frozenset are immutable####")
feta=frozenset(eta)
print("feta -> ",feta)


zeta =set()
print("zeta ", zeta)
zeta.add(3)
print("zeta - after adding 3", zeta)
zeta.add(3)
print("zeta - after adding 3 once again, can't add duplicate ", zeta)
zeta.add(4)
print("zeta ", zeta)

print("Gamma -> ", gamma)

print("discarding value from set")
gamma.discard('K')
print("Gamma -> ", gamma)
print("discarding a value from set whihc is not present - no error raised")
gamma.discard('m')
print("Removing  a value from set which is not present - error raised")
gamma.remove('b')

print("Reference of set changes when we make changes to original set")
set_ref=zeta
print("set_ref - > ",set_ref)
set_copy=zeta.copy()
print("set copy -> ", set_copy)
print("Clearing zeta will clear set_ref only")
zeta.clear()
print("set_ref - > ",set_ref)
print("set copy -> ", set_copy)



















