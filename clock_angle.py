
time='18:00'
num_hour=int(time[:2])
num_minute=5.5*int(time[3:5])
print(num_hour,num_minute)
angle=float(0)
if num_hour>12:
	num_hour-=12
	print(num_hour)
num_hour=num_hour*30

angle=abs(num_minute-num_hour)
print(angle)
if angle>180:
	angle=360-angle
return angle


def clock_angle(time):
    return 0


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert clock_angle("02:30") == 105, "02:30"
    assert clock_angle("13:42") == 159, "13:42"
    assert clock_angle("01:42") == 159, "01:42"
    assert clock_angle("01:43") == 153.5, "01:43"
    assert clock_angle("00:00") == 0, "Zero"
    assert clock_angle("12:01") == 5.5, "Little later"
    assert clock_angle("18:00") == 180, "Opposite"

    print("Now that you're finished, hit the 'Check' button to review your code and earn sweet rewards!")
