# Dimension of each image in the format (width, height)
image_dimensions = [(640, 480), (700,650), (1024, 768), (1920, 1080)]

# the index of the image for which we want to find the height 
image_index = 2

image_height = image_dimensions[image_index][1]

# Enviroment grading
correct_answer = 768
if image_height != correct_answer:
    print(f"The heigt of the image at index {image_index} is incorrect")
else:
    print(f"The height of the image is correct!")


# Slicing Image filenames
# Filesname of the images
image_filenames = ['img_001.jpg', 'img_002.jpg', 'img_003.jpg', 'img_004.jpg', 'img_005.jpg']
last_three_images = image_filenames[-3:]

correct_answer = ['img_003.jpg', 'img_004.jpg', 'img_005.jpg']
if last_three_images != correct_answer:
    print("The last three imported images are incorrect")
else:
    print("The last three imported images are correct!")


# Palindrome Check on image Classifications
image_classifications = ['bal', 'krishna', 'Radha', 'Krishna', 'Bal']

is_palindrome = image_classifications == image_classifications[::-1]

# Checking
correct_answer = True
if is_palindrome != correct_answer:
    print("The image classifications are not a palindrome")
else:
    print("The image classifications are a palindrome")
    
