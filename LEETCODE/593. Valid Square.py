# class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def get_length(x,y):
            length = (x[0]-y[0])**2 + (x[1]-y[1])**2
            return length
        def check_point(a,b,c,d):
            lists = []
            lists.append(get_length(a,b))
            lists.append(get_length(a,c))
            lists.append(get_length(a,d))
            return lists
        list1 = check_point(p1,p2,p3,p4)
        list2 = check_point(p2,p1,p3,p4)
        list3 = check_point(p3,p1,p2,p4)
        list4 = check_point(p4,p1,p3,p2)
        if set(list1) == set(list2) and set(list2) == set(list3) and set(list3) == set(list4) and len(set(list1)) == 2:
            return True
        else:
            return False
                               
            