cmake_minimum_required(VERSION 3.20)
project(Stack2Queue)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(link_stack)
include_directories(seq_stack)

add_executable(Stack2Queue
        link_stack/Assistance.h
        link_stack/LinkStack.h
        link_stack/Node.h
#        link_stack/TestLinkStack.cpp
        seq_stack/Assistance.h
        seq_stack/SeqStack.h
#        seq_stack/TestSeqStack.cpp
        Stack2Queue.h
        TestStack2Queue.cpp)
