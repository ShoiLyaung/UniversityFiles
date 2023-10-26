cmake_minimum_required(VERSION 3.24)
project(link_list)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)

add_executable(link_list
        Assistance.h
        LinkList.h
        Node.h
        TestLinkList.cpp)
