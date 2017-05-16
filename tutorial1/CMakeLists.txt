cmake_minimum_required(VERSION 2.8.3)
project(tutorial1)

## Add support for C++11, supported in ROS Kinetic and newer
add_definitions(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)


###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES tutorial1
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
    include/tutorial1
    ${catkin_INCLUDE_DIRS}
)

# set source, header for the serial manager node
set(SERIAL_MANAGER_SOURCES
	# your sources
)

set(SERIAL_MANAGER_HEADERS
	# your headers
)

# set source, header for the haptics node
set(HAPTIC_NODE_SOURCES
	# your sources
)

set(HAPTIC_NODE_HEADERS
	# your headers
)

## Declare a C++ library
add_library(arduino_serial
	# source files
)

## Declare c++ executables
# add executable
# add_executable(serial_manager ${SERIAL_MANAGER_SOURCES} ${SERIAL_MANAGER_HEADERS})
# link necessary libraries
# target_link_libraries(serial_manager arduino_serial ${catkin_LIBRARIES})

# add executable
# add_executable(haptic_node ${HAPTIC_NODE_SOURCES} ${HAPTIC_NODE_HEADERS})
# link necessary libraries
# target_link_libraries(haptic_node ${catkin_LIBRARIES} usb-1.0 hidapi-libusb mccusb)