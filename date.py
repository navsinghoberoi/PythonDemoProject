import time
import calendar

print("Current epoch value = ", time.time())

timeStructure = time.localtime(time.time())
print("Current time structure :", timeStructure)


# Print current local time #
localtime = time.asctime(time.localtime(time.time()))
print("Local current time :", localtime)

# Print calendar #
print(calendar.month(2018,9))




