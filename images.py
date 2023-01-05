import bpy

D = bpy.data

image_file = 'grouch.jpeg'

img = D.images[image_file]

width = img.size[0]
height = img.size[1]

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
]'''

start_x = 0
start_y = 0

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
