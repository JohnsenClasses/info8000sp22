from CylinderBucket import CylinderBucket
bucket = CylinderBucket(50,5)
#CylinderBucket.fill(bucket,150)
print(bucket.fill(4000))
print(bucket.fill_level())
#illustrating that you can only access the "hidden" internal __maxvolume through a special name
print(bucket._CylinderBucket__maxvolume)
try:
	print(bucket.__maxvolume) #this line fails
except:
	print("Failed, because __maxvolume is hidden")
