# Primer
# github.com/smcclennon/Primer
ver = '1.1.0'
proj = 'Primer'


import os, time
from distutils.version import LooseVersion as semver


if os.name == 'nt':
    Windows = True
else:
    Windows = False



if Windows:
    import ctypes, urllib.request, json
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
                if semver(data['tag_name'][1:]) > semver(ver)]
            updateAttempt = 3
        except:
            latest = '0'
    if semver(latest) > semver(ver):
        print('Update available!      ')
        print(f'Latest Version: v{latest}\n')
        for release in releases:
            print(f'{release[0]}:\n{release[1]}\n')
        confirm = input(str('Update now? [Y/n] ')).upper()
        if confirm != 'N':
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
    with open(f"{proj}.config", "r") as f:
        config=f.readlines()
        total=int(config[0])
        found=int(config[1])-1
        num=int(config[2])+1
except:
    with open(f"{proj}.config", "w") as f:
        f.write('0\n1')
    with open(f"{proj}.config", "r") as f:
        config=f.readlines()
    print(f'Created {proj}.config')
    total=int(config[0])
    found=int(config[1])-1


def updateFile(f):
    try:
        if f == 'all':
            with open(f"{proj}.txt", "a") as f:
                f.write('\n'+str(num))
            with open(f"{proj}.config", "w") as f:
                f.write(f'{total}\n{found}\n{num}')
        elif f == 'txt':
            with open(f"{proj}.txt", "a") as f:
                f.write('\n'+str(num))
        elif f == 'config':
            with open(f"{proj}.config", "w") as f:
                f.write(f'{total}\n{found}\n{num}')
    except Exception as e:
        print(f'\n{e}\nThis was likely caused by prime numbers being generated too quickly.')
        time.sleep(0.1)
        if str(e)[-2] == 't': #.tx(t)
            updateFile('txt')
            print('\n- Storage file updated')
        elif str(e)[-2] == 'g': #.confi(g)
            updateFile('config')
            print('\n- Config file updated')
        else:
            input('updateFile() Unknown fatal error')
            exit()
        print('File system is now up to date!\n')

if Windows: os.system('cls')
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
        if Windows: taskDuration = round(time.time() - taskStart, 2) 

        if invalid == 0:
            if not Windows: taskDuration = round(time.time() - taskStart, 2) 
            nR = 'true'
            found = found + 1
            if Windows:
                print(f'Found Prime [#{found:,}]!  -->  {num:,}  <--  {calculations:,} calculations in {taskDuration} seconds')
            else:
                print(f'{proj} v{ver} >>  Found Prime [#{found:,}]!  --> {num:,} <--  [Total: {total:,}] {calculations:,} calculations in {taskDuration} seconds')
            calculations = 0
            updateFile('all')
            break
    
    num = num + 1
    invalid = 0
    if Windows:
        ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Total Calculations: {total:,}  ---  Elapsed: {round(float(taskDuration), 1)}s  ---  Testing: {num:,}')
    # https://stackoverflow.com/questions/5676646
