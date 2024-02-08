from collections import heapq
class Point:
    def __init__(self, point):
        self.point = point
        self.distance = (point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return self.distance < other.distance
    

def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    point_objects = []
    
    for point in points:
        point_objects.append(Point(point))
    
    heapq.heapify(point_objects)

    res = []
    for _ in range(k):
        res.append(heapq.heappop(point_objects).point)
    
    return res