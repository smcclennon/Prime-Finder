<p align="center"><img style="width: 20%;" src="https://smcclennon.github.io/assets/images/P%2B%2B256.png" alt="Primer++ logo"/></img></p>

<h2 align="center">Primer++</h2>
<p align="center"><small>Rewritten from the ground up in C++ with stability and performance improvements</small></p>


[![build (Windows)](https://github.com/smcclennon/Primer/workflows/build%20(Windows)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Windows)")
[![build (MacOS)](https://github.com/smcclennon/Primer/workflows/build%20(MacOS)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(MacOS)")
[![build (Linux)](https://github.com/smcclennon/Primer/workflows/build%20(Linux)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Linux)")
[![build (Python)](https://github.com/smcclennon/Primer/workflows/build%20(Python)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Python)")
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6dfa8cbba0284a2298ce7fa7fa1e265c)](https://www.codacy.com/manual/smcclennon/Primer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=smcclennon/Primer&amp;utm_campaign=Badge_Grade)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/smcclennon/Primer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smcclennon/Primer/context:cpp)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/smcclennon/Primer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smcclennon/Primer/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/a4e85e15988e4dab380f/maintainability)](https://codeclimate.com/github/smcclennon/Primer/maintainability)
[![License](https://img.shields.io/github/license/smcclennon/Primer)](license)
[![FOSSA license Status](https://app.fossa.com/api/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer.svg?type=shield)](https://app.fossa.com/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer?ref=badge_shield)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/smcclennon/Primer?include_prereleases)](https://github.com/smcclennon/Primer/releases)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/smcclennon/Primer/latest)](https://github.com/smcclennon/Primer/commits)
[![GitHub last commit](https://img.shields.io/github/last-commit/smcclennon/Primer)](https://github.com/smcclennon/Primer/commits)
[![Github download count](https://img.shields.io/github/downloads/smcclennon/Primer/total.svg)](https://GitHub.com/smcclennon/Primer/releases/)
[![HitCount](https://hits.dwyl.com/smcclennon/Primer.svg)](https://hits.dwyl.com/smcclennon/Primer)

## Features
| Feature                                                                 |               Primer++                |            Primer (Python)            |
|:------------------------------------------------------------------------|:-------------------------------------:|:-------------------------------------:|
| Speed                                                                   |               **Fast**                |                 Slow                  |
| CPU Architecture                                                        |                32/64-bit                 |        Same as Python install         |
| OS Compatability                                                        |            Windows, Linux             |     All Python 3.6+ supported OSs     |
| Cross-compatiblity with other versions of Primer                        |                   ✅                   |                   ✅                   |
| Multi-threaded                                                          |                   ❌                   |                   ❌                   |
| Automatic updates (Windows)                                             |                   ❌                   |                   ✅                   |
| Automatic old (`pre 1.2.0`) config migration <small><i>*1</i>           |                   ❌                   |                   ✅                   |
| Automatic config generation                                             |                   ✅                   |                   ✅                   |
| Console Window Title Support (Windows) <small><i>*2</i></small>         |                   ✅                   |                   ✅                   |
| Generate prime numbers <small><i>*3</i></small>                         |                   ✅                   |                   ✅                   |
| Save prime numbers to a file <small><i>*4</i></small>                   |                   ✅                   |                   ✅                   |
| Keep track of generation statistics                                     |                   ✅                   |                   ✅                   |
| Generation statistic: Total Calculations                                |                   ✅                   |                   ✅                   |
| Generation statistic: Prime numbers found                               |                   ✅                   |                   ✅                   |
| Generation statistic: Latest prime found                                |                   ✅                   |                   ✅                   |
| Save generation stats to a config <small><i>*5</i></small>              |                   ✅                   |                   ✅                   |
| Pretty print config (easier to read & edit) <small><i>*6</i></small>    |                   ✅                   |                   ❌                   |
| Load generation stats from the config on start <small><i>*7</i></small> |                   ✅                   |                   ✅                   |
| Language                                                                |            C++ (GCC 8.1.0)            |              Python 3.6+              |
| Created                                                                 |             7th May 2020              |          26th November 2019           |
| Build Success (master)                                                  | [![build (C++)](https://github.com/smcclennon/Primer/workflows/build%20(C++)/badge.svg?branch=master)](https:///github.com/smcclennon/Primer/actions?query=workflow%3A"build+(C%2B%2B)") | [![build (Python)](https://github.com/smcclennon/Primer/workflows/build%20(Python)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Python)") |
| **Download Requirements** | Windows, Linux | [Python 3.6+](https://www.python.org/downloads/) |
| Direct download links | <a href="#downloads"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ release"></a> | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer.py"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer (Python) release"></a> |

1. If you're upgrading to Primer++ from Primer (Python) [`1.1.0`](https://github.com/smcclennon/Primer/releases/tag/v1.1.0) or older, please run Primer (Python) [`1.2.0`](https://github.com/smcclennon/Primer/releases/download/v1.2.0/Primer.py) (or [newer](https://github.com/smcclennon/Primer/releases/latest/download/Primer.py)) to automatically migrate your old config (`Primer.config`) to `Primer_config.json`.

2. Primer will display the current number being prime-tested, and how long it has been since the last prime was found in the console window title (when it has taken `more than 20 seconds to find a new prime`. This is to prevent Primer from slowing down early on when calculating small primes)

3. To calculate primes, Primer will try to divide the test number between numbers 2-itself.

    ```python
    Test_number =  7
    7 / 3 != whole number
    7 / 4 != whole number
    7 / 5 != whole number
    7 / 6 != whole number
    Test_number must be prime!

    Test_number += 2

    Test_number: 9
    9 / 3 == whole number
    Test number is not prime!
    ```
4. Primer will save the prime numbers it finds to `Primer.txt` (each prime on a new line)

5. Primer will save generation statistics to `Primer_config.json` (as soon as the statistics are updated)

6. Pretty printed config has all values expanded, and makes it much easier to read.

   Pretty Print:
   ```json
    {
        "debugging": {
            "Force Unix": "False"
        },
        "statistics": {
            "Latest Prime": 0,
            "Primes Found": 0,
            "Total Calculations": 0
        }
    }
   ```

   Non-pretty Print:

   ```json
   {"debugging": {"Force Unix": "False"}, "statistics": {"Latest Prime": 0, "Primes Found": 0, "Total Calculations": 0}}
   ```
   The reason why Primer (Python) doesn't pretty print is because I haven't found an efficient way to do so.

7. Loading generation statistics (`Primer_config.json`) on start means that when you close the application, starting it up again will return to the state it was in when it closed. This allows you to pickup where you left off.

</br>

## Downloads
| Edition      |   Primer++   |    Primer++     | Primer++  | Primer++  |        Primer        |
|:-------------|:------------:|:---------------:|:---------:|:---------:|:--------------------:|
| OS           | **Windows**  |   **Windows**   | **Linux** | **MacOS** | **Python-supported** |
| Architecture |    32-bit    |     64-bit      |  64-bit   |  64-bit   |    Python Install    |
| Filename     | Primer++.exe | Primer++_32.exe | Primer++  | Primer++  |    Primer&#46;py     |
| CI   | Untested | [![build (Windows)](https://github.com/smcclennon/Primer/workflows/build%20(Windows)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Windows)") | [![build (Linux)](https://github.com/smcclennon/Primer/workflows/build%20(Linux)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Linux)") | [![build (MacOS)](https://github.com/smcclennon/Primer/workflows/build%20(MacOS)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(MacOS)") | [![build (Python)](https://github.com/smcclennon/Primer/workflows/build%20(Python)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Python)") |
| Download | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer++.exe"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ 32-bit Windows release"></a> | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer++_32.exe"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ 64-bit Windows release"> | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer++"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ 64-bit Linux release"></a> | Unavailable | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer.py"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer (Python) release"></a> |

MacOS pre-compiled binary unavailable due to complications with statically linking [`Primer++.hpp`](src/Primer++.hpp) and [`json.hpp`](src/json.hpp) with [`Primer++.cpp`](src/Primer++.cpp). Because of this, it is currently only possible to run Primer++ on MacOS by building it yourself with the build instructions below.

</br>

### Building on Windows
- Follow Prerequisits steps 2-4 on the [Visual Studio Code documentation](https://code.visualstudio.com/docs/cpp/config-mingw) to install [MinGW](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download)
- Clone the repository (or place [`Primer++.cpp`](src/Primer++.cpp), [`Primer++.hpp`](src/Primer++.hpp), [`Primer++_resource.o`](obj/Primer++_resource.o) ([`Primer++_x32_resource.o`](obj/Primer++_x32_resource.o)), [`json.hpp`](src/json.hpp), [`makefile`](makefile) and [`build.bat`](build.bat) in the same directory)
- 64-bit: Run [`build.bat`](build.bat) (or open a terminal in that directory and run `mingw32-make`)
- 32-bit: Open a terminal in that directory and run `mingw32-make 32-bit=true`
- Output executable: [`Primer++.exe`](https://github.com/smcclennon/Primer/releases/latest/download/Primer++.exe) ([`Primer++_32.exe`](https://github.com/smcclennon/Primer/releases/latest/download/Primer++_32.exe))

| Build OSs Tested    | GCC version (local) | Local Success | CI Success |
|:--------------------|:--------------------|:-------------:|:----------:|
| Windows 10 (64-bit) | GCC 8.1.0 (MinGW)   |  ✅ (v1.2.2)   | [![build (Windows)](https://github.com/smcclennon/Primer/workflows/build%20(Windows)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Windows)") |

</br>

### Building on Linux and MacOS
- Clone the repository (or place [`Primer++.cpp`](src/Primer++.cpp), [`Primer++.hpp`](src/Primer++.hpp), [`json.hpp`](src/json.hpp) and [`makefile`](makefile) in the same directory)
- Open a terminal in that directory and run `make` (or execute [`Build.sh`](Build.sh))
- Run Primer with `./Primer++` (or double-click the compiled executable in a file explorer)
- Output executable: [`Primer++`](https://github.com/smcclennon/Primer/releases/latest/download/Primer++)

| Build OSs Tested       | GCC version (local) | Local Success | CI Success |
|:-----------------------|:--------------------|:-------------:|:----------:|
| MacOS Catalina 10.15.4 | Apple clang 11.0.3  |  ✅ (v1.2.2)   | [![build (MacOS)](https://github.com/smcclennon/Primer/workflows/build%20(MacOS)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(MacOS)") |
| Fedora 28              | GCC 8.3.1           |  ✅  (v1.2.2)  | Untested |
| Ubuntu                 |                     |   Untested    | [![build (Linux)](https://github.com/smcclennon/Primer/workflows/build%20(Linux)/badge.svg?branch=master)](https://github.com/smcclennon/Primer/actions?query=workflow%3A"build+(Linux)") |

</br>

| Common Build Errors    |   OS   | How to fix them                                | Verified Fix |
|:-----------------------|:------:|:-----------------------------------------------|:------------:|
| `cannot find -lstdc++` | Fedora | Run `sudo yum install libstdc++-static`        |      ✅       |
| `cannot find -lm`      | Fedora | Run `sudo yum install glibc-static`            |      ✅       |
| `cannot find -lc`      | Fedora | Run `sudo yum install glibc-static`            |      ✅       |
| *Other Errors*         |  All   | Try removing `--static` from the build command |              |

</br>

*Written in C++ with (MinGW) GCC 8.1.0 on Windows 10*

</br>
</br>
</br>

# Primer (Python)
A python script that generates prime numbers

## Screenshots
![Windows version](https://smcclennon.github.io/assets/images/screenshots/Primer/windows.png)
![Unix version](https://smcclennon.github.io/assets/images/screenshots/Primer/unix.png)

*Written in Python 3.8 on Windows 10*

<a href="https://www.freepik.com/free-photos-vectors/menu">Menu vector created by freepik - www.freepik.com</a>
