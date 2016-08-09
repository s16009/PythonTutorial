import sys
print(sys.argv)

print('Hello Python')
print('open logfile...')

sys.stderr.write('WANING: log file not found starting a new one\n')

print('finish')