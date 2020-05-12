<p align="center"><img style="width: 20%;" src="https://smcclennon.github.io/assets/images/P%2B%2B256.png" alt="Primer++ logo"/></img></p>

<h2 align="center">Primer++</h2>
<p align="center"><small>Rewritten from the ground up in C++ with stability and performance improvements</small></p>

[![C/C++ CI](https://github.com/smcclennon/Primer/workflows/C/C++%20CI/badge.svg)](https://github.com/smcclennon/Primer/actions?query=workflow%3A%22C%2FC%2B%2B+CI%22)
[![Build Status](https://travis-ci.com/smcclennon/Primer.svg?branch=master)](https://travis-ci.com/smcclennon/Primer)
[![Build status](https://ci.appveyor.com/api/projects/status/58lu90c0l4020tlw?svg=true)](https://ci.appveyor.com/project/smcclennon/primer)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6dfa8cbba0284a2298ce7fa7fa1e265c)](https://www.codacy.com/manual/smcclennon/Primer?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=smcclennon/Primer&amp;utm_campaign=Badge_Grade)
[![Language grade: C/C++](https://img.shields.io/lgtm/grade/cpp/g/smcclennon/Primer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smcclennon/Primer/context:cpp)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/smcclennon/Primer.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/smcclennon/Primer/context:python)
[![Maintainability](https://api.codeclimate.com/v1/badges/a4e85e15988e4dab380f/maintainability)](https://codeclimate.com/github/smcclennon/Primer/maintainability)
[![GitHub release (latest by date including pre-releases)](https://img.shields.io/github/v/release/smcclennon/Primer?include_prereleases)](https://github.com/smcclennon/Primer/releases)
[![GitHub commits since latest release (by date)](https://img.shields.io/github/commits-since/smcclennon/Primer/latest)](https://github.com/smcclennon/Primer/commits)
[![GitHub last commit](https://img.shields.io/github/last-commit/smcclennon/Primer)](https://github.com/smcclennon/Primer/commits)
[![Github all downloads](https://img.shields.io/github/downloads/smcclennon/Primer/total.svg)](https://GitHub.com/smcclennon/Primer/releases/)
[![HitCount](https://hits.dwyl.com/smcclennon/Primer.svg)](https://hits.dwyl.com/smcclennon/Primer)

## Features
| Feature                                                                 |               Primer++                |            Primer (Python)            |
|:------------------------------------------------------------------------|:-------------------------------------:|:-------------------------------------:|
| Speed                                                                   |               **Fast**                |                 Slow                  |
| CPU Architecture                                                        |                64-bit                 |        Same as Python install         |
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
| Tested OSs                                                              | Windows 10, Fedora 28, RedHat 7.7, MacOS Catalina | Windows 10, Fedora 28, MacOS Catalina |
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
| Edition  |   Primer++   | Primer++  | Primer++  |        Primer        |
|:---------|:------------:|:---------:|:---------:|:--------------------:|
| OS       | **Windows**  | **Linux** | **MacOS** | **Python-supported** |
| Filename | Primer++.exe | Primer++  | Primer++  |    Primer&#46;py     |
| Tested   |      ✅       |     ✅     |     ❌     |          ✅           |
| Download | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer++.exe"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ release"></a> | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer++"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer++ release"></a> | Unavailable | <a href="https://github.com/smcclennon/Primer/releases/latest/download/Primer.py"><img src="https://smcclennon.github.io/update/download.png" alt="Download latest Primer (Python) release"></a> |

MacOS pre-compiled binary unavailable due to complications with statically linking [`Primer++.h`](Primer++.h) and [`json.hpp`](json.hpp) with [`Primer++.cpp`](Primer++.cpp). Because of this, it is currently only possible to run Primer++ on MacOS by building it yourself with the build instructions below.

</br>

### Building on Windows
- Follow Prerequisits steps 2-4 on the [Visual Studio Code documentation](https://code.visualstudio.com/docs/cpp/config-mingw) to install [MinGW](https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download)
- Clone the repository (or place [`Primer++.cpp`](Primer++.cpp), [`Primer++.h`](Primer++.h), [`Primer++.o`](Primer++.o), [`json.hpp`](json.hpp), [`makefile`](makefile) and [`build.bat`](build.bat) in the same directory)
- Run [`Build.bat`](build.bat) (or open a terminal in that directory and run `mingw32-make`)
- Output executable: `Primer++.exe`

| Build Tested OS     | GCC version       | Local Success | CI Success |
|:--------------------|:------------------|:-------------:|:----------:|
| Windows 10 (64-bit) | GCC 8.1.0 (MinGW) |       ✅       |     ✅      |

</br>

### Building on Linux and MacOS
- Clone the repository (or place [`Primer++.cpp`](Primer++.cpp), [`Primer++.h`](Primer++.h), [`json.hpp`](json.hpp) and [`makefile`](makefile) in the same directory)
- Open a terminal in that directory and run `make` (or execute [`Build.sh`](Build.sh))
- Run Primer with `./Primer++` (or double-click the compiled executable in a file explorer)
- Output executable: `Primer++`

| Build Tested OS        | GCC version        | Local Success | CI Success |
|:-----------------------|:-------------------|:-------------:|:----------:|
| MacOS Catalina 10.15.4 | Apple clang 11.0.3 |       ✅       |     ✅      |
| Fedora 28              | GCC 8.3.1          |       ✅       |     ✅      |
| Ubuntu                 |                    |   Untested    |     ✅      |

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
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer?ref=badge_shield)

*Written in Python 3.8 on Windows 10*

<a href="https://www.freepik.com/free-photos-vectors/menu">Menu vector created by freepik - www.freepik.com</a>


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2Fsmcclennon%2FPrimer?ref=badge_large)