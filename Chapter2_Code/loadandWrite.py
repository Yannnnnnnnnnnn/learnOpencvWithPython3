import cv2
import numpy

#use 0 or 1 to close or open part example
exec_test_one = 0
exec_test_two = 1

#Test one
#generate a image and show
if exec_test_one == 0:
    #generate a image using randomint
    img = numpy.random.randint(0,255,dtype=numpy.uint8,size=(255,255,3))
    #convert into HSV
    img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #print(img)
    cv2.imshow('test',img)
    cv2.waitKey()
    cv2.destroyAllWindows()
 
#Test two
#read a image and write in a different extention
if exec_test_two == 1:
    img =
