current_hour=int(input('Enter the current hour:'))
wait_hours=int(input("How long do you want to wait:"))
end_time=current_hour+wait_hours
alarm_time=end_time%24
print("The alarm will sound at",str(alarm_time)+'h')