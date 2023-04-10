from engine import convertV

dims= [3,4,3] #cube dims xyz
pc= [10,10,10] #perspective coordinates
pa= [2, 45, -80] #perspective angles
s= [1,0,2]

points= []

move= [[s[0],s[2]],[s[0], dims[2]+s[2]],[dims[0]+s[0], dims[2]+s[2]], [dims[0]+s[0], s[2]]]

print("    3D    |    2D    ")

for y in [0, dims[1]]:
    for xz in move:
        points.append(convertV(xz[0],y,xz[1], pc, pa))
        print([xz[0],y,xz[1]], '|', points[-1])

print('\nGeogebra:\n\n', f'polygon({"{"}{str(points[:4])[1:-1]}{"}"})', '\n\n', f'polygon({"{"}{str(points[4:])[1:-1]}{"}"})', '\n')