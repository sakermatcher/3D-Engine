from engine import convertV
from pygame import surface, BLEND_RGBA_MULT


class polygon():
    def __init__(self, pointa, pointb, pointc):
        """
        Points are in format [x,y,z]
        """
        self.points3D= [pointa, pointb, pointc]

    def render(self, pc, pa):
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

        print([minX[0], minY[0]])

        if minX[0] > 0 and maxX[0] < 1000 and minY[0] > 0 and maxY[0] < 1000: #if the polygon is within the screen

            width= maxX[0] - minX[0]
            height= maxY[0] - minY[0]
            
            #Generate each point in a edge between the points
            A= []
            B= []
            C= []

            for i, points in enumerate([[a, b], [b, c], [c, a]]):
                if points[1][1] < points[0][1]: #if the second point is lower than the first
                    ordered= [points[1], points[0]]
                else:
                    ordered= points
                for y in range(1, ordered[1][1] - ordered[0][1]): #for each y value between the two points
                    if i == 0:
                        C.append([int(ordered[1][0] - ordered[0][0] * y / abs(points[0][1] - points[1][1]) + ordered[0][0]), y])
                    elif i==1:
                        A.append([int(ordered[1][0] - ordered[0][0] * y / abs(points[0][1] - points[1][1]) + ordered[0][0]), y])
                    elif i==2:
                        B.append([int(ordered[1][0] - ordered[0][0] * y / abs(points[0][1] - points[1][1]) + ordered[0][0]), y])

            #Generate the surface
            surf= surface.Surface((width, height))
            surf.fill((0,0,0,0), None, BLEND_RGBA_MULT)
            for i in A:
                surf.set_at((i[0], i[1]), (255,0,0))
            for i in B:
                surf.set_at((i[0], i[1]), (0,255,0))
            for i in C:
                surf.set_at((i[0], i[1]), (0,0,255))
            for i in [a,b,c]:
                surf.set_at((i[0], i[1]), (255,255,255))
            return [surf, [minX[0], minY[0]]]  
        else:
            return [surface.Surface((0, 0)), [0,0]]
        
def polygonMaker(points, connections):
    """
    Send a list of points and a list of connections with three points and it will return a list of polygons
    """

    polys= []
    for i in connections:
        polys.append(polygon(points[i[0]], points[i[1]], points[i[2]]))

    return polys



class cube():
    connections= [[1,2,0],[1,2,3],[3,6,2],[6,3,7],[4,7,6],[4,7,5],[1,4,5],[4,1,0],[3,5,1],[3,5,7],[7,4,0],[2,4,6]] #connections between points

    def __init__(self, dims, start):
        """
        dims= [3,4,3] #cube dims xyz\n
        start= [1,0,2]
        """
        self.dims= dims
        self.start= start
        self.generatePolygons()

    def generatePolygons(self):
        self.points= []
        for y in [self.start[1], self.dims[1]+self.start[1]]:
            for z in [self.start[2], self.dims[2]+self.start[2]]:
                for x in [self.start[0], self.dims[0]+self.start[0]]:
                    self.points.append([x,y,z])

        self.polygons= polygonMaker(self.points, cube.connections)

class pol():
    connections= [[1,2,0]] #connections between points

    def __init__(self):
        self.points= [[0,0,0],[300,300,300],[300,0,300]]
        self.polygons= polygonMaker(self.points, pol.connections)
        

class pyramid():
    def __init__(self, dims, start):
        """
        dims= [3,4,3] #cube dims xyz\n
        start= [1,0,2]
        """
        self.dims= dims
        self.start= start

    def render(self, pc, pa):
        """
        pc= [10,10,10] #perspective coordinates\n
        pa= [2, 45, -45] #perspective angles\n
        """
        self.points= []
        for z in [self.start[2], self.start[2]+self.dims[2]]:
            for x in [self.start[0], self.start[0]+self.dims[0]]:
                self.points.append(convertV(x,self.start[1],z, pc, pa))
        self.points.append(convertV(self.dims[0]/2+self.start[0], self.dims[1]+self.start[1], self.dims[2]/2+self.start[2], pc, pa))
        self.vertices={4:[0,1,2,3], 0:[1,2], 3:[1,2]}