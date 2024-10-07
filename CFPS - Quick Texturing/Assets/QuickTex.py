import bpy, extcolors, sys

# Path to the image
image = "C:/Path/To/Image.png"

# Tolerance to differentiate the colors
tolerance = 30
# Number of colors to sample / number of materials that need colors
num_mat = 4

mat = 1

# Function to cnvert from linear color to rgb
def lin2rgb(color):
    if(color <= 0.0404482362771082):
        new_color = color / 12.92
    else:
        new_color = pow(((color + 0.055) / 1.055), 2.4)
    return new_color

# Extract colors from image

colors_x = extcolors.extract_from_path(image, tolerance, num_mat)

# Clean up the output color string
colors_pre_list = str(colors_x).replace('([(','').split(', (')[0:num_mat]

df_rgb = [i.split('), ')[0] + ')' for i in colors_pre_list]

for i in df_rgb:
    
    R = i.split(',')[0].replace('(', '')
    R = float(R) / 256
    
    G = i.split(',')[1]
    G = float(G) / 256
    
    B = i.split(',')[2].replace(')', '')
    B = float(B) / 256

    # Convert colors
    R = lin2rgb(R)
    G = lin2rgb(G)
    B = lin2rgb(B)
    
    # Get material name
    mat_name = "Mat " + str(mat)
    
    # Changes base color to RGB
    bpy.data.materials[mat_name].node_tree.nodes["RGB"].outputs[0].default_value = (R, G, B, 1)
    
    #next material
    mat = mat + 1

# Change image texture in material
image_mat = bpy.data.materials["Image"]
image_tex = image_mat.node_tree.nodes["Image Texture"]
image_tex.image = bpy.data.images.load(image)

print('done!')
