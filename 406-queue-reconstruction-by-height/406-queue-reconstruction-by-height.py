class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        
        #ind -> how many greater ahead
        
        #pos >= ind
        
        #7 7 6 52 5 4
        
        people.sort(key = lambda x: -(x[0]<<11) + x[1])
        #e = None
        for i in xrange(len(people)):
            k =  i - people[i][1]
            if k > 0:
                e = people.pop(i)
                people.insert(i - k, e)
            #print(people, e, i, k, i - k)
        return people
        
        