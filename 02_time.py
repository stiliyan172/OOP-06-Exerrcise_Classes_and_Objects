class Time:
    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, new_hours: int, new_minutes: int, new_seconds: int):
        self.hours = new_hours
        self.minutes = new_minutes
        self.seconds = new_seconds

    def get_time(self):
        return f"{self.hours}:{self.minutes}:{self.seconds}"

    def next_second(self):
        total_time = self.hours * 3600 + self.minutes * 60 + self.seconds
        if total_time >= 86399:
            total_time -= 86400
        total_time += 1
        self.hours = total_time // 3600
        leading_zero_hours = 0 if self.hours < 10 else ""
        self.minutes = (total_time - (self.hours * 3600)) // 60
        leading_zero_minutes = 0 if self.minutes < 10 else ""
        self.seconds = total_time - (self.hours * 3600 + self.minutes * 60)
        leading_zero_seconds = 0 if self.seconds < 10 else ""
        return f"{leading_zero_hours}{self.hours}:{leading_zero_minutes}{self.minutes}:{leading_zero_seconds}{self.seconds}"


time = Time(9, 30, 59)
print(time.next_second())

time = Time(10, 59, 59)
print(time.next_second())

time = Time(23, 59, 59)
print(time.next_second())
