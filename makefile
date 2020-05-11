# Compiler settings
CC = g++
CXXFLAGS = -m32 -std=c++17 -pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused
EXTRACXXFLAGS = --static -Wlogical-op -Wnoexcept -Wstrict-null-sentinel

# Project settings
APPNAME = Primer++
EXT = .cpp
SRCDIR = src
OBJDIR = obj

# OS-specific settings
ifeq ($(OS),Windows_NT)  # is Windows_NT on XP, 2000, 7, Vista, 10...
    detected_OS := Windows
else
    detected_OS := $(shell uname)
endif

ifeq ($(detected_OS),Windows)
	RESOURCE = Primer++_resource.o
else
    UNAME_S := $(shell uname -s)
    ifneq ($(UNAME_S),Darwin)
        CXXFLAGS += $(EXTRACXXFLAGS)
    endif
endif



all: $(APPNAME)

# Building .c/.cpp
	$(CC) -c $<.cpp $(CXXFLAGS)
	$(CC) $<.o $(RESOURCE) -o $< $(CXXFLAGS)

ifeq ($(detected_OS),Windows)
	del $(APPNAME).o
else
	rm $(APPNAME).o
endif