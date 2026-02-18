#copy binary file
import shutil

source = "E:/LinkedIn/VL-JEPA image.jpg";
target = "E:/LinkedIn/Copied VL-JEPA image.jpg";
shutil.copyfile(source, target)
print(source + " is copied to " + target)
