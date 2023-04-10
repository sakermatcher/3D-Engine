from engine import convertV
from pygame import surface

class line():
    def __init__(self, pointa, pointb) -> None:
        #Prevent division by zero
        if pointa[0] - pointb[0] == 0: #if the line is vertical
            self.m= 90
        else:
            self.m= (pointa[1] - pointb[1])/(pointa[0] - pointb[0])

        self.b= pointa[1] - (self.m*pointa[0])
        self.minX= min({pointa[0]:'a', pointb[0]:'b'}.items())
        self.maxX= max({pointa[0]:'a', pointb[0]:'b'}.items())
        self.minY= min({pointa[1]:'a', pointb[1]:'b'}.items())
        self.maxY= max({pointa[1]:'a', pointb[1]:'b'}.items())
        print(pointa, pointb)


    def solveForX(self, y):
        """
        y= mx + b
        Given Y, solve for X
        """
        x= (y - self.b)/self.m
        return x

    def solveForY(self, x):
        """
        y= mx + b
        Given X, solve for Y
        """
        y= self.m*x + self.b
        return y

    def toPoints(self, surf, clr) -> surface:
        """
        Generate all points in the line
        """
        if self.maxX[0] - self.minX[0] > self.maxY[0] - self.minY[0]: #if the line is more horizontal than vertical
            if self.maxX[0]>1000:
                self.maxX= (1000, self.maxX[1])
            if self.minX[0]<0:
                self.minX= (0, self.minX[1])

            if self.maxX[0] < 0 or self.minX[0] > 1000:
                return surf

            for x in range(self.minX[0], self.maxX[0]):
                y= int(self.solveForY(x))
                if y <= 1000 and y >= 0:
                    surf.set_at((x,y), clr)

        else: #if the line is more vertical than horizontal
            if self.maxY[0]>1000:
                self.maxY= (1000, self.maxY[1])
            if self.minY[0]<0:
                self.minY= (0, self.minY[1])

            if self.maxY[0] < 0 or self.minY[0] > 1000:
                return surf

            for y in range(self.minY[0], self.maxY[0]):
                x= int(self.solveForX(y))
                if x <= 1000 and x >= 0:
                    surf.set_at((x, y), clr)

        return surf
        
class polygon():
    def __init__(self, pointa, pointb, pointc):
        """
        Points are in format [x,y,z]
        """
        self.points3D= [pointa, pointb, pointc]

    def render(self, pc, pa, surf):
        """
        Convert the 3D points to 2D points
        pc= perspective coordinates [x, y, z]
        pa= perspective angles [distance, angleX, angleY]
        """

        #Generate the 2D points
        a =convertV(self.points3D[0][0], self.points3D[0][1], self.points3D[0][2], pc, pa)
        b =convertV(self.points3D[1][0], self.points3D[1][1], self.points3D[1][2], pc, pa)
        c =convertV(self.points3D[2][0], self.points3D[2][1], self.points3D[2][2], pc, pa)

        minX= min({a[0]:'a', b[0]:'b', c[0]:'c'}.items())
        maxX= max({a[0]:'a', b[0]:'b', c[0]:'c'}.items())
        minY= min({a[1]:'a', b[1]:'b', c[1]:'c'}.items())
        maxY= max({a[1]:'a', b[1]:'b', c[1]:'c'}.items())

        print([minX[0], minY[0]], [maxX[0], maxY[0]])
            #Generate each point in a edge between the points

        for i in ([[a, b, (255,0,0)], [b, c, (0,255,0)], [c, a, (0,0,255)]]):
            surf= line(i[0], i[1]).toPoints(surf, i[2])

        for i in [a,b,c]:
            if i[0] <= 1000 and i[0] >= 0 and i[1] <= 1000 and i[1] >= 0:
                surf.set_at((i[0], i[1]), (255,255,255))

        return surf
        
def polygonMaker(points, connections, polRules):
    """
    Send a list of points and a list of connections with three points and it will return a list of polygons
    """

    polys= []
    for i in connections:
        polys.append(polygon(points[i[0]], points[i[1]], points[i[2]]))

    return polys

class form():
    def __init__(self, points, polygonConnections, polRules, perPolRules= False):
        """
        points= [[x,y,z],[x,y,z]]\n
        connections= [[point1, point2, point3],[point1, point2, point3]]\n
        """
        self.points= points
        if perPolRules:
            for i in polRules:
                self.polygons= polygonMaker(self.points, polygonConnections, i)
        else:
            self.polygons= polygonMaker(self.points, polygonConnections, polRules)

    def render(self, pc, pa, surf):
        for i in self.polygons:
            surf= i.render(pc, pa, surf)

class preSets():
    def cube(dims:any, start):
        """
        dims= [x,y,z]\n
        start= [x,y,z]
        """

        points= []
        for y in [start[1], dims[1]+start[1]]:
            for z in [start[2], dims[2]+start[2]]:
                for x in [start[0], dims[0]+start[0]]:
                    points.append([x,y,z])

        connections= [[1,2,0],[1,2,3],[3,6,2],[6,3,7],[4,7,6],[4,7,5],[1,4,5],[4,1,0],[3,5,1],[3,5,7],[7,4,0],[2,4,6]] #connections between points

        return form(points, connections, 'FACE')

    def pyramid(dims:any, start):
        points= []
        for z in [start[2], start[2]+dims[2]]:
            for x in [start[0], start[0]+dims[0]]:
                points.append([x, start[1], z])
        points.append([start[0]+dims[0]/2, start[1]+dims[1], start[2]+dims[2]/2])

        connections= [[0,3,1],[0,3,2],[0,1,4],[1,3,4],[3,2,4],[2,0,4]] #connections between points

        return form(points, connections, ['FACE','FACE','CUSTOM','CUSTOM','CUSTOM','CUSTOM'])

    def pol(points:any):
        connections= [[1,2,0]] #connections between points
        return form(points, connections, 'FACE')
            