#!/bin/sh
# Primer++
# github.com/smcclennon/Primer
# Tested with MacOS Catalina 10.15.4 with Apple clang 11.0.3

echo Warning: This build command has only been tested on MacOS Catalina 10.15.4 with Apple clang 11.0.3
echo This is MacOS only and may not work on other versions of MacOS (and/or) Apple clang
echo Building...
# [GCC 4.2.1] g++ Primer++.cpp Primer++.h json.hpp -std=c++11
# chmod +x build.sh
clang++ Primer++.cpp -o Primer++ -std=c++17
echo Build complete!
./Primer++