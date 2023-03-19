'''
    Creating alarm application using builder pattern
'''

class Alarm:
    def __init__(self):
        self._name = None
        self._time = None
        self._duration = 1
        self._snooze = None
        self._repeat = 'None'

    def name(self, name):
        self._name = name
        return self

    def time(self, time):
        self._time = time
        self.set_next_alarm_time(time)
        return self
    
    def duration(self, duration):
        self._duration = duration
        return self
    
    def snooze(self, snooze):
        self._snooze = snooze
        return self
    
    def repeat(self, repeat):
        self._repeat = repeat
        return self
    
    def set_next_alarm_time(self, alarm_time):
        next_alarm_time = alarm_time
        self.next_alarm_time = next_alarm_time

    def __str__(self):
        alarm = f'''
            Alarm name: {self._name}
            Time: {self._time}
            Repetion Days: {self._repeat}
            Duration: {self._duration}

            Alarm would ring in: 10 mins
        '''

        return alarm
    

def main():
    alarm = Alarm() \
            .name('Jogging') \
            .time('9 AM') \
            .repeat('Mon Tue Wed') \
            .duration(3)

    print(alarm)


if __name__ == '__main__':
    main()
