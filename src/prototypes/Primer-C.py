# Primer Compatability version
# github.com/smcclennon/Primer
ver = '1.0.3C'
proj = 'Primer-C'


import time, os


total=0
num=3
invalid=0
found=0
calculations=0
attempts='...'
config=[]

try:
    # https://stackoverflow.com/questions/3346430
    with open(f"{proj}.txt", "rb") as f:
        #first = f.readline()        # Read the first line.
        f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
        while f.read(1) != b"\n":   # Until EOL is found...
            f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
        num = int(f.readline().decode('utf-8')) # get the latest prime number
except:
    print(f'Unable to load data from "{proj}.txt", the file may not exist, or we are unable to parse it due to your OS')
    wipe=input('Generate new file? [y/N]: ').lower()
    if wipe == 'y':
        with open(f"{proj}.txt", "w") as f:
            f.write(f'== {proj} v{ver} ==\ngithub.com/smcclennon/Primer')
    else:
        exit()

try:
    with open(f"{proj}.config", "r") as f:
        config=f.readlines()
        total=int(config[0])
        found=int(config[1])-1
except:
    with open(f"{proj}.config", "w") as f:
        f.write('0\n1')
    with open(f"{proj}.config", "r") as f:
        config=f.readlines()
    print(f'Created {proj}.config')
    total=int(config[0])
    found=int(config[1])-1




nR = 'true' # New Round, track when a prime has just been found in the loop
while True:
    if nR == 'true':
        taskStart = time.time()
        nR = 'false'

    while invalid == 0:
        if int(str(num)[-1]) % 2 == 0:  # If number is even (ends in 0, 2, 4, 6, 8)
            total = total + 1
            calculations = calculations + 1
            invalid = 1  # Skip processing the number
            break

        for i in range(3,num):
            total = total + 1
            calculations = calculations + 1
            if num % i == 0: # If number is divisible by a number other than 1 or itself
                invalid = 1

        if invalid==0:
            taskDuration = round(time.time() - taskStart, 2)
            nR = 'true'
            found = found + 1
            print(f'== {proj} v{ver} ==  Found Prime [#{found:,}]!  ---> {num:,} <---  {calculations:,} calculations in {taskDuration} seconds  --- Total Calculations: {total:,}')
            calculations = 0
            with open(f"{proj}.txt", "a") as f:
                f.write('\n'+str(num))
            with open(f"{proj}.config", "w") as f:
                f.write(f'{total}\n{found}')
            break

    num=num+1
    invalid=0
