import cv2

#inputing image
source="mark.table.jpg"
destination="newmarktable.jpg"
scale_percent=50
inp=cv2.imread(source,cv2.IMREAD_UNCHANGED)

#resizing image
height=int(inp.shape[0]*scale_percent/100)
widht=int(inp.shape[1]*scale_percent/100)
output=cv2.resize(inp,(widht,height))

#outputing image
cv2.imwrite(destination,output)
