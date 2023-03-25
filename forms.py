from engine import convertV

class polygon():
    def __init__(self, points):
        self.points= points
        

class cube():
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
        self.vertices= {0:[1,2,4], 3:[1,2,7], 5:[4,7,1], 6:[4,7,2]}
        for y in [self.start[1], self.dims[1]+self.start[1]]:
            for z in [self.start[2], self.dims[2]+self.start[2]]:
                for x in [self.start[0], self.dims[0]+self.start[0]]:
                    self.points.append(convertV(x,y,z, pc, pa))

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