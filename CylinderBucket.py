import math
class CylinderBucket:
    def __init__(self,height_cm,radius_cm):
        # Input: height of the cylinder, and the radius of the cylinder
        # Output: an initialized cylinder, with properties height, radius
        self.__maxvolume = (math.pi)*(radius_cm**2)*(height_cm)
        self.height = height_cm
        self.radius = radius_cm
        self.__currentheight = 0
        self.__area = math.pi*self.radius**2
        pass
    def fill(self,quantity_cm3):
        # Input: a volume of water to fill the bucket with
        # Output: the amount of water put in, less any that spilled over

        #convert volume to height
        height = quantity_cm3/self.__area

        #determine how much spilled over by height
        if self.__currentheight + height > self.height:
            height_over = self.__currentheight + height - self.height
            volume_over = height_over*self.__area
            self.__currentheight = self.height
            return quantity_cm3 - volume_over
        else:
            self.__currentheight += height
            return quantity_cm3
        pass
    def fill_level(self):
        # Input: None
        # Output: the height of the water so far
        return self.__currentheight
        pass
