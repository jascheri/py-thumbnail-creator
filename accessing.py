import urllib as net

def createThumbnail(imageUrl, path):
    """
    createThumbnail() pulls a picture from the internet, creates a thumbnail and saves it to the computer.
    
    Parameter:
        imageUrl(string): URL to a picture file on the web
        path(string): Path to save the images to
    """
   
    #Retrieves the image from the web and saves it to the user's path
    data = net.urlretrieve(imageUrl, path + "fullPicture.jpg")
    
    #Retrieves the full path to the image file
    file = getMediaPath("fullPicture.jpg")
    
    #Creates a picture from the file path
    picture = makePicture(file)
    show(picture)
    
    #Creates a thumbnail of the picture and saves it to the user's specified path
    writePictureTo(shrinkImage(picture,8), path + "thumbnail.jpg")
    
          
def shrinkImage(oldImage, scale):
    """
    shrinkImage() scales down a provided image by the specified scale.
    
    Parameters:
        oldImage(picture): The image that you sat to scale down
        scale(int): The ratio that you want to scale down. 
        
    Returns: picture scaled down
    """
    
    #Get the dimensions of the old Image
    width = getWidth(oldImage)
    height = getHeight(oldImage)
    
    #Create a new image for the scale
    canvas = makeEmptyPicture(int(width/scale), int(height/scale))
    printNow("New Image Dimensions: " + str(int(width/scale)) + "," + str(int(height/scale)))
    #The Scale Loops
    oY = 0
    for nY in range(0, int(height/scale)):
        oX = 0
        for nX in range(0, int(width/scale)):
            tempColor = getColor(getPixel(oldImage, oX, oY))
            setColor(getPixel(canvas, nX, nY), tempColor)
            oX = oX + scale
        oY = oY + scale
    show(canvas)
    return(canvas)

#Starts the program
createThumbnail("http://www.hww.ca/kaboom/images/Mammals/Chipmunk.jpg", setMediaPath())


