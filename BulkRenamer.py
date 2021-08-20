import os

def renamer():
    i = 1
    path = "C:\\Users\\User\\Desktop\\College_Finder\\rename\\images\\"			#path of the folder
    for filename in os.listdir(path):											#for loop to apply the rename to all images
        names = f"image {i}.jpg"												#new names 
        src = path + filename
        dest = path + names
        
        os.rename(src,dest)
        i = i + 1
    
if __name__ == "__main__":
    renamer()

