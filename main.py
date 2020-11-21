import PIL.image

#list of characters for output image 
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

#resize image 
def resize_image(image, new_width=100):
   width, height = image.size
   ratio = height / width 
   new_height = int(new_width * ratio)
   resized_image = image.resize((new_width, new_height))
   return(resized_image)

#convert image pixels to grayscale 
def gray(image):
   grayscale_image = image.convert("L")
   return(grayscale_image)

#convert pixels to ASCII characters
def pixels_to_ascii(image):
   pixels = image.getdata()
   characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
   return(characters)

def main():
   path = input("Enter a valid pathname to an image:\n")  
try: 
   image = PIL.Image.open(path)
except: 
   print(path, "is not a valid pathname to an image.")

new_image_data = pixels_to_ascii(gray(resize_image(image)))

pixel_count = len(new_image_data)
ascii_image = "\n".join(new_image_data[i:(i+new_width)] for i in range(0, pixels_to_ascii, new_width)

print(ascii_image)

with open("ascii_image.txt", "w") as f: 
   f.write(ascii_image)

