# There are 2N people a company is planning to interview. The cost of flying the i-th person to city A is costs[i][0], and the cost of flying the i-th person to city B is costs[i][1].

# Return the minimum cost to fly every person to a city such that exactly N people arrive in each city.

 

# Example 1:

# Input: [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.

# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people interviewing in each city.

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        List3 = []
        x = int(len(costs))
        x = x/2
        m = 0
        n = 0
        sum = 0
        for each in costs:
            List3.append(abs(each[0] - each[1]))
        List1 = [x for _, x in sorted(zip(List3, costs))]
        List1.reverse()
        for each in List1:
            if each[0] <= each[1]:
                sum= sum + each[0]
                m += 1
                if m == x:
                    t = List1.index(each)
                    for i in range(t+1, len(costs)):
                        sum = sum + List1[i][1]
                    break
                else:
                    continue
            else:
                sum = sum+ each[1]
                n += 1
                if n == x:
                    t = List1.index(each)
                    for i in range(t+1, len(costs)):
                        sum = sum + List1[i][0]
                    break
                else:
                    continue
        return sum
        