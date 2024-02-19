from time import perf_counter_ns

print(end='Please enter your name: ')
start_time = perf_counter_ns()
name = input()
stop_time = perf_counter_ns()
elapsed = (stop_time - start_time)/1_000_000_000
print(f'Hello {name}, it took you {elapsed} seconds to respond.')
