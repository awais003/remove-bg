from rembg import remove, new_session
from PIL import Image

session = new_session("u2net")

# load image
input_image = Image.open("image.avif")

# remove background
output_image = remove(input_image, session=session)

# save the output image
output_image.save("output.png")

print("Background removed successfully")