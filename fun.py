from PIL import Image

# Open the original image
original_image = Image.open("data/sanjukta.jpeg")
width, height = original_image.size

# Create a new image with the same size
new_image = Image.new("RGB", (width, height))

# Get the pixel data as a list of tuples
original_pixels = list(original_image.getdata())
#print(original_pixels)

for i,j,k in original_pixels:
    print(i)

print(len(original_pixels))

# Modify the pixel data (for example, invert the colors)
new_pixels = [(r + 20, 20 + g, 200 + b) for r, g, b in original_pixels]

# Put the modified pixel data into the new image
new_image.putdata(new_pixels)

# Save the new image
new_image.save("modified_image.jpg")