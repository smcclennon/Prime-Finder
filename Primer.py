# Primer
# github.com/smcclennon/Primer
ver = '1.0.2'
proj = 'Primer'


import os, ctypes, time, urllib.request, json

ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Checking for updates...')

updateAttempt = 0
print('Checking for updates...', end='\r')
try:  # Remove previous version if just updated
    with open(f'{proj}.tmp', 'r') as content_file:
        oldFile = str(content_file.read())
        # If the old version has the current filename, don't delete
        if oldFile != os.path.basename(__file__):
            os.remove(oldFile)
    os.remove(f'{proj}.tmp')
except:
    pass
while updateAttempt < 3:
    updateAttempt = updateAttempt+1
    try:
        with urllib.request.urlopen("https://smcclennon.github.io/update/api/3") as url:
            repo = []
            for line in url.readlines():
                repo.append(line.decode().strip())
            apiLatest = repo[0]  # Latest release details
            proj = repo[1]  # Project name
            ddl = repo[2]  # Direct download
            apiReleases = repo[3]  # List of patch notes
        with urllib.request.urlopen(apiLatest) as url:
            data = json.loads(url.read().decode())
            latest = data['tag_name'][1:]
        del data  # Prevent overlapping variable data
        release = json.loads(urllib.request.urlopen(
            apiReleases).read().decode())
        releases = [
            (data['tag_name'], data['body'])
            for data in release
            if data['tag_name'][1:] > ver][::-1]
        updateAttempt = 3
    except:
        latest = '0'
if latest > ver:
    print('Update available!      ')
    print(f'Latest Version: v{latest}\n')
    for release in releases:
        print(f'{release[0]}:\n{release[1]}\n')
    confirm = input(str('Update now? [Y/n] ')).upper()
    if confirm == '' or confirm == 'Y':
        latestFilename = f'{proj} v{latest}.py'
        # Download latest version to cwd
        print(f'Downloading "{latestFilename}"...')
        urllib.request.urlretrieve(ddl, latestFilename)
        # Write the current filename to LTFO.tmp
        f = open(f'{proj}.tmp', 'w')
        f.write(str(os.path.basename(__file__)))
        f.close()
        os.system(f'"{latestFilename}"')  # Open latest version
        exit()





total=0
num=2
invalid=0
found=0
calculations=0
taskDuration='0'
attempts='...'
config=[]





try:
    # https://stackoverflow.com/questions/3346430
    with open(f"{proj}.txt", "rb") as f:
        #first = f.readline()        # Read the first line.
        f.seek(-2, os.SEEK_END)     # Jump to the second last byte.
        while f.read(1) != b"\n":   # Until EOL is found...
            f.seek(-2, os.SEEK_CUR) # ...jump back the read byte plus one more.
        num = int(f.readline().decode('utf-8')) #get the latest prime number
except:
    with open(f"{proj}.txt", "w") as f:
        f.write(f'== {proj} v{ver} ==\ngithub.com/smcclennon/{proj}')

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
try:
    # https://stackoverflow.com/questions/549109
    import win32api, win32con
    win32api.SetFileAttributes(f'{proj}.config',win32con.FILE_ATTRIBUTE_HIDDEN)  # Try to hide the config file
except:
    pass


os.system('cls')
nR='true' # New Round, track when a prime has just been found in the loop
while True:
    if nR=='true':
        taskStart=time.time()
        nR='false'
    while invalid==0:
        for i in range(2,num):
            total=total+1
            calculations=calculations+1
            if num % i == 0: # If number is divisible by a number other than 1 or itself
                invalid = 1
        taskDuration=round(time.time()-taskStart, 2)
        # https://stackoverflow.com/questions/5676646
        ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Total Calculations: {total:,}  ---  Elapsed: {round(float(taskDuration), 1)}s  ---  Testing: {num:,}')
        if invalid==0:
            nR='true'
            found=found+1
            print(f'Found Prime #{found:,}!  --- >  {num:,}  < ---  {calculations:,} calculations in {taskDuration} seconds')
            calculations=0
            with open(f"{proj}.txt", "a") as f:
                f.write('\n'+str(num))
            with open(f"{proj}.config", "w") as f:
                f.write(f'{total}\n{found}')
            break
    num=num+1
    invalid=0