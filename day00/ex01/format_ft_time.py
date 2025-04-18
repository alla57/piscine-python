import time

current_time = time.time()

line1 = f"Seconds since January 1, 1970: {current_time:,.4f} \
or {current_time:.2e} in scientific notation"

current_time_struct = time.localtime(current_time)
line2 = time.strftime("%b %d %Y", current_time_struct)

print(line1)
print(line2)
