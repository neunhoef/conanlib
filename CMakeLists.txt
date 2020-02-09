project(conanlib CXX)

cmake_minimum_required(VERSION 3.5)
set(CMAKE_CXX_STANDARD 17)

add_library(conanlib conanlib.cpp)
target_include_directories(conanlib PUBLIC
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:${CMAKE_INSTALL_PREFIX}/include>
)

install(
    DIRECTORY   include
    DESTINATION .
)

install(TARGETS conanlib
    EXPORT conanlib-targets
    RUNTIME DESTINATION bin
    LIBRARY DESTINATION lib
    ARCHIVE DESTINATION lib
)

#install(
#    EXPORT conanlib-targets
#    FILE conanlib-config.cmake
#    NAMESPACE arango::
#    DESTINATION ${CMAKE_INSTALL_PREFIX}
#)
