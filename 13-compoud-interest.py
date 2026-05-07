#14.Calculate compound interest
principal = 10000
rate = 5
time = 2
print(f"principal = {principal}")
print(f"rate = {rate}")
print(f"time = {time}")
amount = int(principal *(1 + rate/100)**time)
compound_int = amount - principal
print(f"compound_int = {compound_int}")



