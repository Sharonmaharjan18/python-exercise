exchange_dollar_rate=float(input('Enter the current exchange dollar rate(€->$):'))
amount=float(input('Enter your amount in euro:'))
convert=amount*exchange_dollar_rate
print(amount,'€','=',convert,'$')