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
