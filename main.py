#Setup Code
#Get PIL installed for Python at https://pillow.readthedocs.io/en/stable/installation.html
from PIL import Image, ImageFilter
x=0

# Ask the user for the image path
image_path = input("Enter the path of the image: ")
image = Image.open(image_path)


# Display original image
image.show()


# Ask the user for the desired feature
print("Choose an image manipulation feature:")
print("1. Resize")
print("2. Rotate")
print("3. Apply Blur Filter")
print("4. Convert to Grayscale")
print("5. Add Watermark")
#If incorrect choice is provided then program will stop execution
choice = input("Enter your choice (1-5): ")


# Perform the selected image manipulation feature


#Resize the image
if choice == "1":
    width = int(input("Enter the new width: "))
    height = int(input("Enter the new height: "))
    resized_image = image.resize((width, height))
    resized_image.show()


#Rotate the image
elif choice == "2":
    angle = int(input("Enter the rotation angle (in degrees): "))
    rotated_image = image.rotate(angle)
    rotated_image.show()


#Apply Blur Filter
elif choice == "3":
    filtered_image = image.filter(ImageFilter.BLUR)
    filtered_image.show()


#Convert to Grayscale
elif choice == "4":
    grayscale_image = image.convert("L")
    grayscale_image.show()


#Add Watermark to the image
elif choice == "5":
    watermark_path = input("Enter the path of the watermark image: ")
    if watermark_path:
        watermark = Image.open(watermark_path).convert("RGBA")
        watermark = watermark.resize(image.size)
        watermarked_image = Image.new("RGBA", image.size)
        watermarked_image.paste(image, (0, 0))
        watermarked_image = Image.blend(watermarked_image, watermark, alpha=0.5)
        watermarked_image.show()
    else:
        print("Watermark path is required for the watermark option.")




#The choice is invalid so the code ends
else:
    print("Invalid choice!")
    x=1


# Save the manipulated image if the correct choice is selected
if choice in ["1", "2", "3", "4", "5"]:
    output_path = input("Enter the output path to save the manipulated image: ")
    if output_path:
        # Save the image using the output_path
        if choice == "1":
            resized_image.save(output_path)
        elif choice == "2":
            rotated_image.save(output_path)
        elif choice == "3":
            filtered_image.save(output_path)
        elif choice == "4":
            grayscale_image.save(output_path)
        elif choice == "5":
            watermarked_image.save(output_path)
        print("Manipulated image saved successfully.")
    else:
        print("Output path is required to save the manipulated image.")
