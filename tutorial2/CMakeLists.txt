cmake_minimum_required(VERSION 2.8.3)
project(tutorial2)

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
#  LIBRARIES tutorial2
#  CATKIN_DEPENDS roscpp rospy std_msgs
#  DEPENDS system_lib
)

###########
## Build ##
###########

## specify qt packages and directories
find_package(Qt5Widgets REQUIRED)
include_directories(${Qt5Widgets_INCLUDES})

## Specify additional locations of header files
## Your package locations should be listed before other locations
# include_directories(include)
include_directories(
  include/tutorial2
  ${catkin_INCLUDE_DIRS}
)

# set source, header for the control panel
set(CONTROL_PANEL_SOURCES
    src/control_panel.cpp
    src/control_panel_node.cpp
)

set(CONTROL_PANEL_HEADERS
    include/tutorial2/control_panel.h
)

set(CONTROL_PANEL_FORMS
    ui/control_panel.ui
)

# create qt moc headers for GUI
qt5_wrap_cpp(MOC_SOURCES ${CONTROL_PANEL_HEADERS})
qt5_wrap_ui(FORMS_HEADERS ${CONTROL_PANEL_FORMS})
include_directories(${CMAKE_CURRENT_SOURCE_DIR} ${CMAKE_CURRENT_BINARY_DIR})

# add executable for the GUI
add_executable(control_panel
    ${CONTROL_PANEL_SOURCES} ${CONTROL_PANEL_HEADERS}
    ${MOC_SOURCES} ${FORMS_HEADERS}
)
target_link_libraries(control_panel ${catkin_LIBRARIES})
qt5_use_modules(control_panel Widgets)
