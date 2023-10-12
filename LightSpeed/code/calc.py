import math

lightSpeed = 299792458  #m/s
lightSpeedKm = 299792.458 #km/s
yearInSec = 31536000

def earthTime(time, speed):
    r1 = 1-speed*speed/lightSpeed/lightSpeed
    result = float(time/math.sqrt(r1))
    print("Distance km " + str(float((time * speed)/1000)))
    print("Distance light years: " + str(float((time * speed) /lightSpeed / yearInSec)))
    print("Distance light years: " + str(float((time * speed)/1000) / 0.00000000000010570))
    return result

def timeForTravel (distance, speed):
    distMilKm = float(1000000 * distance)
    speedInKm = float(speed*lightSpeedKm)
    return float(distMilKm / speedInKm)

print("Time to the Mars:")
print(timeForTravel(450, 0.9))

result = earthTime(17625600, 0.999999*lightSpeed)

print("Seconds: "+ str(round(result, 0)))
print("Minutes: "+ str(round(result/60, 3)))
print("Hours: "+ str(round(result/3600 , 3)))
print("Days: "+ str(round(result/86400, 3)))
print("Weeks: "+ str(round(result/604800 , 3)))
print("Months: "+ str(round(result/2592000 , 3)))
print("Years: "+ str(round(result/31526000 , 1)))

# 150 000 000 km from Sun to Earth
# light travel 8 min 20sec or 500sec

#distance to Mars 382 050 000 km
#Alpha Centauri 4,36 light year

