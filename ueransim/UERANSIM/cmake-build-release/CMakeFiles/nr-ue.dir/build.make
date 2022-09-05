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
include CMakeFiles/nr-ue.dir/depend.make
# Include any dependencies generated by the compiler for this target.
include CMakeFiles/nr-ue.dir/compiler_depend.make

# Include the progress variables for this target.
include CMakeFiles/nr-ue.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/nr-ue.dir/flags.make

CMakeFiles/nr-ue.dir/src/ue.cpp.o: CMakeFiles/nr-ue.dir/flags.make
CMakeFiles/nr-ue.dir/src/ue.cpp.o: ../src/ue.cpp
CMakeFiles/nr-ue.dir/src/ue.cpp.o: CMakeFiles/nr-ue.dir/compiler_depend.ts
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/ueransim/UERANSIM/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/nr-ue.dir/src/ue.cpp.o"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -MD -MT CMakeFiles/nr-ue.dir/src/ue.cpp.o -MF CMakeFiles/nr-ue.dir/src/ue.cpp.o.d -o CMakeFiles/nr-ue.dir/src/ue.cpp.o -c /ueransim/UERANSIM/src/ue.cpp

CMakeFiles/nr-ue.dir/src/ue.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/nr-ue.dir/src/ue.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /ueransim/UERANSIM/src/ue.cpp > CMakeFiles/nr-ue.dir/src/ue.cpp.i

CMakeFiles/nr-ue.dir/src/ue.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/nr-ue.dir/src/ue.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /ueransim/UERANSIM/src/ue.cpp -o CMakeFiles/nr-ue.dir/src/ue.cpp.s

# Object files for target nr-ue
nr__ue_OBJECTS = \
"CMakeFiles/nr-ue.dir/src/ue.cpp.o"

# External object files for target nr-ue
nr__ue_EXTERNAL_OBJECTS =

nr-ue: CMakeFiles/nr-ue.dir/src/ue.cpp.o
nr-ue: CMakeFiles/nr-ue.dir/build.make
nr-ue: src/lib/libcommon-lib.a
nr-ue: src/ue/libue.a
nr-ue: src/lib/libcommon-lib.a
nr-ue: src/utils/libutils.a
nr-ue: src/ext/libext.a
nr-ue: src/asn/ngap/libasn-ngap.a
nr-ue: src/asn/rrc/libasn-rrc.a
nr-ue: src/asn/asn1c/libasn-asn1c.a
nr-ue: CMakeFiles/nr-ue.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/ueransim/UERANSIM/cmake-build-release/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable nr-ue"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/nr-ue.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/nr-ue.dir/build: nr-ue
.PHONY : CMakeFiles/nr-ue.dir/build

CMakeFiles/nr-ue.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/nr-ue.dir/cmake_clean.cmake
.PHONY : CMakeFiles/nr-ue.dir/clean

CMakeFiles/nr-ue.dir/depend:
	cd /ueransim/UERANSIM/cmake-build-release && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /ueransim/UERANSIM /ueransim/UERANSIM /ueransim/UERANSIM/cmake-build-release /ueransim/UERANSIM/cmake-build-release /ueransim/UERANSIM/cmake-build-release/CMakeFiles/nr-ue.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/nr-ue.dir/depend
