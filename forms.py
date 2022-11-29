from engine import convertV

def cube(dims, pc, pa, start):
    """
    dims= [3,4,3] #cube dims xyz\n
    pc= [10,10,10] #perspective coordinates\n
    pa= [2, 45, -45] #perspective angles\n
    start= [1,0,2]
    """

    points= []
    connections= {0:[1,2,4], 3:[1,2,7], 5:[4,7,1], 6:[4,7,2]}
    for y in [start[1], dims[1]+start[1]]:
        for z in [start[2], dims[2]+start[2]]:
            for x in [start[0], dims[0]+start[0]]:
                points.append(convertV(x,y,z, pc, pa))

    return [points, connections]

def pyramid(dims, pc, pa, start):

    points= []

    for z in [start[2], start[2]+dims[2]]:
        for x in [start[0], start[0]+dims[0]]:
            points.append(convertV(x,start[1],z, pc, pa))

    points.append(convertV(dims[0]/2+start[0], dims[1]+start[1], dims[2]/2+start[2], pc, pa))
    connections={4:[0,1,2,3], 0:[1,2], 3:[1,2]}

    return[points, connections]