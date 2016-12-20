import pytz
import datetime
import random

local_time = datetime.datetime.now()
utc_time = datetime.datetime.utcnow()

available_zones = []
for zone in range(10):
	available_zones.append(pytz.all_timezones[random.randint(0, len(pytz.all_timezones) - 1)])

print('Here is the menu to select from: ')
for entry in range(len(available_zones)):
	print('{}. {}'.format(entry + 1, available_zones[entry]))

fmt = '%A %d.%m.%Y., %H:%M:%S %Z %z'
proposed_answers = [str(x) for x in range(11)]

while True:

	pick = input('\nEnter the number of the zone you wanna check time with (0 to quit): \n')
	if pick not in proposed_answers:
		#pick = input('Please be kind and read again, number from 0 - 10 required!')
		continue

	if pick == '0':
		print('Goodbye')
		break

	tz_to_display = pytz.timezone(available_zones[int(pick) - 1])
	try:
		city = str(tz_to_display).split("/")[1]
	except IndexError:
		city = str(tz_to_display).split("/")[0]
	ltimezone = pytz.utc.localize(local_time).astimezone(tz_to_display).tzname()
	ltime = pytz.utc.localize(local_time).astimezone(tz_to_display)
	print('U zoni {} trenutno je {}, a to je vremenska zona {}'.format(city, ltime.strftime(fmt), ltimezone,))
	#print(pytz.utc.localize(utc_time).astimezone(tz_to_display).tzname())
