cmake_minimum_required(VERSION 3.10)
project(string)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(string
        Assistance.h
        LinkList.h
        Node.h
        String.h
        TestString.cpp)
