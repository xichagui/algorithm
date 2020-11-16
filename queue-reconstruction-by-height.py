class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda x: (-x[0], x[1]))
        n = len(people)
        res = []
        for person in people:
            res.insert(person[1], person)
            # res[person[1]: person[1]] = [person]
        return res
    
