import time
now = time.localtime()
hour = now.tm_hour
if hour < 8:
    print('sleeping')
elif hour < 9:
    print('commuting')
elif hour < 17:
    print('working')
elif hour < 18:
    print('commuting')
elif hour < 20:
    print('eating')
elif hour < 22:
    print('resting')
else:
    print('sleeping')
