from CylinderBucket import CylinderBucket
bucket = CylinderBucket(50,5)
print(bucket._maxvolume)
#CylinderBucket.fill(bucket,150)
print(bucket.fill(4000))
print(bucket.fill_level())