#Image Editor
#Setup Code
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
print("5. Crop")
print("6. Add Watermark")
choice = input("Enter your choice (1-6): ")


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


#Crop
elif choice == "5":
    print("Enter the crop area:")
    left = int(input("Left coordinate: "))
    upper = int(input("Upper coordinate: "))
    right = int(input("Right coordinate: "))
    lower = int(input("Lower coordinate: "))
    crop_area = (left, upper, right, lower)
    cropped_image = image.crop(crop_area)
    cropped_image.show()


#Add Watermark to the image
elif choice == "6":
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




#The choice is not correct
else:
    print("Invalid choice!")
    x=1


# Save the manipulated image if the correct choice is selected
if choice in ["1", "2", "3", "4", "5", "6"]:
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
            cropped_image.save(output_path)
        elif choice == "6":
            watermarked_image.save(output_path)
        print("Manipulated image saved successfully.")
    else:
        print("Output path is required to save the manipulated image.")
