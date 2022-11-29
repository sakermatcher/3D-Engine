from engine import convertV

dims= [2,10,2] #pyramid dims (length, height, width) : (x,y,z)
pc= [30,5,1] #perspective coordinates
pa= [2, 0, 0] #perspective angles

points= []

move= [[0,0],[0, dims[0]],[dims[2], dims[0]], [dims[2], 0]]

print("    3D    |    2D    ")

for zx in move:
    points.append(convertV(zx[1],0,zx[0], pc, pa))
    print([zx[1],0,zx[0]], '|', points[-1])

points.append(convertV(dims[0]/2, dims[1], dims[2]/2, pc, pa))
print([dims[0]/2, dims[1], dims[2]/2], '|', points[-1])


print('\nGeogebra:\n\n', f'polygon({"{"}{str(points[:4])[1:-1]}{"}"})', '\n\n', f'point({"{"}{str(points[4])[1:-1]}{"}"})', '\n')