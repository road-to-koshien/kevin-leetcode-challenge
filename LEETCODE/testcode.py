nums = [1,2,3,4]

import itertools
res = []
for i in range(1, len(nums)+1):
    list_append = [list(x) for x in itertools.combinations(nums, i)]
    res.append(list_append)
res1 = list(itertools.chain.from_iterable(res))
print(res1)


