# Primer
# github.com/smcclennon/Primer
ver = '1.2.2'
proj = 'Primer'


import os, time, json


invalid=0
found=0
round_calculations=0  # Calculations for the current prime
task_duration = 0
previous_task_duration = 0
attempts = '...'
config = {
    "statistics": {
        "Total Calculations": 0,
        "Primes Found": 0,
        "Latest Prime": 0
    },
    "debugging": {
        "Force Unix": "False"
    }
}


if os.name == 'nt':
    Windows = True
else:
    Windows = False

try:
    with open(f"{proj}_config.json", "r") as config_file:
        config = json.load(config_file)
        #config["statistics"]["Primes Found"] -= 1
        config["statistics"]["Latest Prime"] += 1
except:
    try:
        with open(f"{proj}_config.json", "w") as config_file:
            json.dump(config, config_file)
        print(f'Created {proj}_config.json')
        # Attempt to convert an old config into a new one
        with open(f"Primer.config", "r") as old_config_file:
            oldconfig=old_config_file.readlines()
            config["statistics"]["Total Calculations"]=int(oldconfig[0])
            config["statistics"]["Primes Found"]=int(oldconfig[1])
            config["statistics"]["Latest Prime"]=int(oldconfig[2])
        with open(f"{proj}_config.json", "w") as config_file:
            json.dump(config, config_file)
        print('Old config successfully migrated')
    except:
        pass

if config["debugging"]["Force Unix"] == 'True':
    Windows = False








# Updater: Used to check for new releases on GitHub
# github.com/smcclennon/Updater
# OS function used for detecting OS type (nt, posix, java), clearing console window, restart the script
from distutils.version import LooseVersion as semver  # as semver for readability
import urllib.request # access the GitHub API
import platform  # Consistantly detect MacOS

# Disable SSL certificate verification for MacOS (very bad practice, I know)
# https://stackoverflow.com/a/55320961
if platform.system() == 'Darwin':  # If MacOS
    import ssl
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context

if os.name == 'nt':
    import ctypes  # set Windows console window title
    ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Checking for updates...')

updateAttempt = 0  # Keep track of failed attempts
print('Checking for updates...', end='\r')
while updateAttempt < 3:  # Try to retry the update up to 3 times if an error occurs
    updateAttempt = updateAttempt+1
    try:
        with urllib.request.urlopen("https://smcclennon.github.io/update/api/3") as internalAPI:
            repo = []
            for line in internalAPI.readlines():
                repo.append(line.decode().strip())
            apiLatest = repo[0]  # Latest release details
            proj = repo[1]  # Project name
            ddl = repo[2]  # Direct download link
            apiReleases = repo[3]  # List of patch notes
        with urllib.request.urlopen(apiLatest) as githubAPILatest:
            data = json.loads(githubAPILatest.read().decode())
            latest = data['tag_name'][1:]  # remove 'v' from version number (v1.2.3 -> 1.2.3)
        del data  # Prevent overlapping variable data
        release = json.loads(urllib.request.urlopen(  # Get latest patch notes
            apiReleases).read().decode())
        releases = [  # Store latest patch notes in a list
            (data['tag_name'], data['body'])
            for data in release
            if semver(data['tag_name'][1:]) > semver(ver)]
        updateAttempt = 3
    except:  # If updating fails 3 times
        latest = '0'
if semver(latest) > semver(ver):
    print('Update available!      ')
    print(f'Latest Version: v{latest}\n')
    for release in releases:
        print(f'{release[0]}:\n{release[1]}\n')
    confirm = input(str('Update now? [Y/n] ')).upper()
    if confirm != 'N':
        print(f'Downloading {proj} v{latest}...')
        urllib.request.urlretrieve(ddl, os.path.basename(__file__))  # download the latest version to cwd
        import sys; sys.stdout.flush()  # flush any prints still in the buffer
        os.system('cls||clear')  # Clear console window
        os.system(f'"{__file__}"' if os.name == 'nt' else f'python3 "{__file__}"')
        time.sleep(0.2)
        quit()









def updateFile(category):
    try:
        if category == 'all':
            with open(f"{proj}.txt", "a") as prime_list:
                prime_list.write('\n'+str(config["statistics"]["Latest Prime"]))
            with open(f"{proj}_config.json", "w") as config_file:
                json.dump(config, config_file)

        elif category == 'txt':
            with open(f"{proj}.txt", "a") as prime_list:
                prime_list.write('\n'+str(config["statistics"]["Latest Prime"]))

        elif category == 'config':
            with open(f"{proj}_config.json", "w") as config_file:
                json.dump(config, config_file)

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
new_round = 'true' # New Round, track when a prime has just been found in the loop
while True:
    if new_round == 'true':
        task_start = time.time()
        new_round = 'false'

    while invalid == 0:
        if int(str(config["statistics"]["Latest Prime"])[-1]) % 2 == 0:  # If number is even (ends in 0, 2, 4, 6, 8)
            config["statistics"]["Total Calculations"] += 1
            round_calculations += 1
            invalid = 1  # Skip processing the number
            break

        for i in range(3,config["statistics"]["Latest Prime"]):
            config["statistics"]["Total Calculations"] += 1
            round_calculations += 1
            if config["statistics"]["Latest Prime"] % i == 0: # If number is divisible by a number other than 1 or itself
                round_calculations += 1
                invalid = 1
        if Windows:
            task_duration = round(time.time() - task_start, 2)
            previous_task_duration = task_duration

        if invalid == 0:
            if not Windows: task_duration = round(time.time() - task_start, 2)
            new_round = 'true'
            config["statistics"]["Primes Found"] += 1
            if Windows:
                print(f'Found Prime [#{config["statistics"]["Primes Found"]:,}]!  -->  {config["statistics"]["Latest Prime"]:,}  <--  {round_calculations:,} calculations in {task_duration} seconds')
            else:
                print(f'{proj} v{ver} >>  Found Prime [#{config["statistics"]["Primes Found"]:,}]!  --> {config["statistics"]["Latest Prime"]:,} <--  [Total: {config["statistics"]["Total Calculations"]:,}] {round_calculations:,} calculations in {task_duration} seconds')
            calculations = 0
            updateFile('all')
            break

    config["statistics"]["Latest Prime"] += 1
    invalid = 0
    if Windows and previous_task_duration > 5:
        task_duration = round(time.time() - task_start, 2)
        if task_duration > 60:
            ctypes.windll.kernel32.SetConsoleTitleW(f'   == {proj} v{ver} ==   Total Calculations: {config["statistics"]["Total Calculations"]:,}  ---  Elapsed: {round(float(task_duration), 1)}s  ---  Testing: {config["statistics"]["Latest Prime"]:,}')
    # https://stackoverflow.com/questions/5676646
