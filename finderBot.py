from engine import convertV

def finder(pc, pa, poly):
    """
    A bot that automatically finds the angle to put a polygon in frame
    """
    dirX= 1
    dirY= 1
    point= convertV(poly[0], poly[1], poly[2], pc, pa)
    x, y= point[0], point[1]

    pa= [pa[0], pa[1]+dirX, pa[2]]
    newX= convertV(poly[0], poly[1], poly[2], pc, pa)[0]
    if abs(500 - x) < abs(500 - newX):
        dirX= -1
        rightDirX= -1
    else:
        rightDirX= 1
        x= newX

    while True:
        pa= [pa[0], pa[1]+rightDirX, pa[2]]
        newX= convertV(poly[0], poly[1], poly[2], pc, pa)[0]

        if abs(500 - x) < abs(500 - newX):
            break
        else:
            print('x', newX)
            x= newX
        
    pa= [pa[0], pa[1], pa[2]+dirY]
    newY= convertV(poly[0], poly[1], poly[2], pc, pa)[1]
    if abs(500 - y) < abs(500 - newY):
        dirY= -1
        rightDirY= -1
    else:
        rightDirY= 1
        y= newY

    while True:
        pa= [pa[0], pa[1], pa[2]+rightDirY]
        newY= convertV(poly[0], poly[1], poly[2], pc, pa)[1]

        if abs(500 - y) < abs(500 - newY):
            break
        else:
            print('y', newY)
            y= newY

    return pa





print(finder([150,5000,150], [100, 0, -45], [150,0,150]))
