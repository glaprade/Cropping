import cv2
import os

directory = '/Volumes/KINGSTON/Split channels' # file path

h = 128 # height of target image
edge = 2048 # dimension of input image
offset = int(h/2)

# list of list of parameters for different iterations in form [x, y, x_edge, y_edge]
iterations = [[0,0,edge,edge], [offset,0,edge-h,edge], [0,offset,edge,edge-h],[offset,offset,edge-h,edge-h]]

for entry in os.scandir(directory): # for image in folder
    img=cv2.imread(entry, cv2.IMREAD_UNCHANGED) # read image
    name = os.path.basename(entry) # get file name
    name_len = len(name) # get length of file name
    name = name[0:name_len-4] # remove file type

    print("starting image " + str(name) + "...")

    # set crop counter to 1
    count = 1

    for i in iterations: # for each crop iteration
        x = i[0] # set x start
        y = i[1] # set y start
        x_edge = i[2] # set x edge boundary
        y_edge = i[3] # set y edge boundary

        while y < y_edge: # while the starting y coordinate is less than the edge value
            while x < x_edge: # while the starting x coordinate is less than the edge value

                crop = img[y:y+h,x:x+h] # crop image to specified height

                img_label = "image_" + str(name) + str(count) +".tif" # create label for image

                cv2.imwrite(os.path.join("/Volumes/KINGSTON/crops", img_label), crop) # save image with new label

                count += 1 # increase crop counter
                x += h # increase the starting x coordinate value

            x = i[0] # reset the starting x coordinate value
            y += h # increase the starting y coordinate value
    print(str(name) + " finished")


