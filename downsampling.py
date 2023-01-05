import bpy
import math
import random

D = bpy.data
image_file = 'grouch.jpeg'
img = D.images[image_file]

width = img.size[0]
height = img.size[1]

res_x = 40
res_y = 40

set_width = width//res_x
set_height = height//res_y
offset_x = (width%res_x)//2
offset_y = (height%res_y)//2

x = 0 
y = 0
grey = 0
index = 0
pixels = [0,0,0]

for out_x in range(res_x):
    for out_y in range(res_y):
        for i in range(30): # takes 30 from the set sample space
            x = math.floor(offset_x + set_width * (out_x + random.random()))
            y = math.floor(offset_y + set_height * (out_y + random.random()))
            index = (y * width + x) * 4
            for j in range(3):
                pixels[j] += img.pixels[index+j]
        # take averages
        for k in range(3):
            grey+=pixels[k]
            pixels[k]/=30
        grey/=90
        
        # object creation
        bpy.ops.mesh.primitive_cube_add(size=1, location=(out_x, out_y, grey * 10))
        
        # material mapping
        mat_name = "Material" + str(index)
        mat = bpy.data.materials.new(name = mat_name)
        mat.use_nodes = True
        principled = mat.node_tree.nodes["Principled BSDF"]
        principled.inputs[0].default_value = (pixels[0], pixels[1], pixels[2], 1)
        cube = bpy.context.active_object
        cube.data.materials.append(mat)
            

'''target = [150, 33] # X, Y
print ("Target vector: ", target)

# target.Y * image width + target.X * 4 (as the table Pixels contains separate RGBA values)
index = ( target[1] * width + target[0] ) * 4

# aggregate the read pixel values into a nice array
pixel = [
    img.pixels[index], # RED
    img.pixels[index + 1], # GREEN
    img.pixels[index + 2], # BLUE
    img.pixels[index + 3] # ALPHA
]


for x in range(start_x, start_x + 50, 1):
    for y in range(start_y, start_y+50, 1):
        # object creation
        index = (y * width + x) * 4
        height = (img.pixels[index] + img.pixels[index+1] + img.pixels[index+2])/3 * 20
        bpy.ops.mesh.primitive_cube_add(size=1, location = (x-start_x,y-start_y,height/2), scale=(1, 1, 1))
        
        # coloring
        mat_name = "Material" + str(index)
        mat = bpy.data.materials.new(name = mat_name)
        mat.use_nodes = True
        principled = mat.node_tree.nodes["Principled BSDF"]
        principled.inputs[0].default_value = (img.pixels[index], img.pixels[index+1], img.pixels[index+2], img.pixels[index+3])
        cube = bpy.context.active_object
        cube.data.materials.append(mat)
#local_pixels = list[img.pixels[]]'''