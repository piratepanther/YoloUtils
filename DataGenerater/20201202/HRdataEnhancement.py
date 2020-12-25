import cv2
import os

wd = os.getcwd()

RawData_sapce_dir = os.path.join(wd, "todo/")
if not os.path.isdir(RawData_sapce_dir):
    print("No todo Raw Data!")


list = os.listdir(RawData_sapce_dir) # list image files
# print(list)
# for z in range(0,len(list)):
for z in range(0, len(list)):

    in_path = RawData_sapce_dir + list[z]
    image_path = RawData_sapce_dir + list[z].split('.')[0] + '-z.jpg'

    img = cv2.imread(in_path, 1)

    try:
        img2 = cv2.flip(img, 1)
        # img2 = cv2.flip(img, 1)
        # img3 = cv2.flip(img, 0)
        # img4 = cv2.flip(img, -1)

        cv2.imwrite(image_path, img2)

    except Exception as e:
        print(in_path, e)





