# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.23

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:

# Disable VCS-based implicit rules.
% : %,v

# Disable VCS-based implicit rules.
% : RCS/%

# Disable VCS-based implicit rules.
% : RCS/%,v

# Disable VCS-based implicit rules.
% : SCCS/s.%

# Disable VCS-based implicit rules.
% : s.%

.SUFFIXES: .hpux_make_needs_suffix_list

# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

#Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /root/cmake-3.23/bin/cmake

# The command to remove a file.
RM = /root/cmake-3.23/bin/cmake -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /ueransim/UERANSIM

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /ueransim/UERANSIM/cmake-build-release

# Include any dependencies generated for this target.
include CMakeFiles/devbnd.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/devbnd.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/devbnd.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/devbnd.dir/flags.make

CMakeFiles/devbnd.dir/src/binder.cpp.o: CMakeFiles/devbnd.dir/flags.make
CMakeFiles/devbnd.dir/src/binder.cpp.o: ../src/binder.cpp
CMakeFiles/devbnd.dir/src/binder.cpp.o: CMakeFiles/devbnd.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/ueransim/UERANSIM/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/devbnd.dir/src/binder.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/devbnd.dir/src/binder.cpp.o -MF CMakeFiles/devbnd.dir/src/binder.cpp.o.d -o CMakeFiles/devbnd.dir/src/binder.cpp.o -c /ueransim/UERANSIM/src/binder.cpp

CMakeFiles/devbnd.dir/src/binder.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/devbnd.dir/src/binder.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /ueransim/UERANSIM/src/binder.cpp > CMakeFiles/devbnd.dir/src/binder.cpp.i

CMakeFiles/devbnd.dir/src/binder.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/devbnd.dir/src/binder.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /ueransim/UERANSIM/src/binder.cpp -o CMakeFiles/devbnd.dir/src/binder.cpp.s

# Object files for target devbnd
devbnd_OBJECTS = \
"CMakeFiles/devbnd.dir/src/binder.cpp.o"

# External object files for target devbnd
devbnd_EXTERNAL_OBJECTS =

libdevbnd.so: CMakeFiles/devbnd.dir/src/binder.cpp.o
libdevbnd.so: CMakeFiles/devbnd.dir/build.make
libdevbnd.so: CMakeFiles/devbnd.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/ueransim/UERANSIM/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX shared library libdevbnd.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/devbnd.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/devbnd.dir/build: libdevbnd.so
.PHONY : CMakeFiles/devbnd.dir/build

CMakeFiles/devbnd.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/devbnd.dir/cmake_clean.cmake
.PHONY : CMakeFiles/devbnd.dir/clean

CMakeFiles/devbnd.dir/depend:
	cd /ueransim/UERANSIM/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /ueransim/UERANSIM /ueransim/UERANSIM /ueransim/UERANSIM/cmake-build-release /ueransim/UERANSIM/cmake-build-release /ueransim/UERANSIM/cmake-build-release/CMakeFiles/devbnd.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/devbnd.dir/depend

