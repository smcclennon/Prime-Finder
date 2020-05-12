# Compiler settings
CC = g++
CXXFLAGS = -std=c++17 -pedantic -Wall -Wextra -Wcast-align -Wcast-qual -Wctor-dtor-privacy -Wdisabled-optimization -Wformat=2 -Winit-self -Wmissing-declarations -Wmissing-include-dirs -Wold-style-cast -Woverloaded-virtual -Wredundant-decls -Wshadow -Wsign-conversion -Wsign-promo -Wstrict-overflow=5 -Wswitch-default -Wundef -Werror -Wno-unused
EXTRACXXFLAGS = --static -Wlogical-op -Wnoexcept -Wstrict-null-sentinel

# Project settings
APPNAME = Primer++
EXT = .cpp
SRCDIR = src
OBJDIR = obj
OUT = $(APPNAME)

# OS-specific settings
ifeq ($(OS),Windows_NT)  # is Windows_NT on XP, 2000, 7, Vista, 10...
	detected_OS := Windows
	windows_delete_command = del
else
	detected_OS := $(shell uname)
endif

ifeq ($(detected_OS),Windows)
	CXXFLAGS += $(EXTRACXXFLAGS)
	RESOURCE = $(OBJDIR)/$(APPNAME)_resource.o
	ifeq ($(32-bit),true)
		OUT = $(APPNAME)_32
		RESOURCE = $(OBJDIR)/$(APPNAME)_x32_resource.o
		CXXFLAGS += -m32
	endif
else
	UNAME_S := $(shell uname -s)
	ifneq ($(UNAME_S),Darwin)
		CXXFLAGS += $(EXTRACXXFLAGS)
	endif
endif



$(info    OS is $(detected_OS))

$(APPNAME):

# Building .c/.cpp
	$(CC) -c $(SRCDIR)/$@.cpp -o $(OBJDIR)/$(OUT).o $(CXXFLAGS)
	$(CC) $(OBJDIR)/$(OUT).o $(RESOURCE) -o $(OUT) $(CXXFLAGS)

.PHONY: clean
clean:
ifeq ($(detected_OS),Windows)
	$(windows_delete_command) $(OBJDIR)\$(OUT).o
else
	rm $(OBJDIR)/$(OUT).o
endif