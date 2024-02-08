class Point:
    def __init__(self, point):
        self.point = point
        self.distance = (point[0]**2 + point[1]**2)
    
    def __lt__(self, other):
        return self.distance < other.distance
    

