cmake_minimum_required(VERSION 3.0.0)
project(C8hw11 VERSION 0.1.0)

include(CTest)
enable_testing()

add_executable(C8hw11 test.cpp AvlTree.h)

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
include(CPack)
