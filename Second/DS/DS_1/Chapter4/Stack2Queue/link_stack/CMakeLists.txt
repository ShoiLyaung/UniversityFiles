cmake_minimum_required(VERSION 3.22)
project(link_stack)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(link_stack
        Assistance.h
        LinkStack.h
        Node.h
        TestLinkStack.cpp)
