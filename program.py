from time import localtime

activities = {8: 'Sleeping',
              9: 'Commuting',
              17: 'Working',
              18: 'Commuting',
              20: 'Eating',
              22: 'Resting',
			  }

print 'Komenatrz'
print 'Komenatrz'
print 'Komenatrz'
print 'Komenatrz'
print 'Komenatrz'

for activity_time in sorted(activities.keys()):
    if hour < activity_time:
        print activities[activity_time]
        break
else:
    print 'Unknown, AFK or sleeping!'
