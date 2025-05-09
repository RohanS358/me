
# System calls

System calls are interfaces provisioned by the operating system to allow user-level applications to interact with low-level hardware components & make use of all the services provided by the kernel, which is a core component and the heart of an operating system that manages all the hardware and the services provided by the OS.

These system calls are essential for every process to interact with the kernel and properly use the services provided by it. System calls are an interface between a process and the operating system. And they're the only way to switch from user mode to kernel mode.
## Types of System Calls

Services provided by an OS are typically related to any kind of operation that a user program can perform like creation, termination, forking, moving, communication, etc. Similar types of operations are grouped into one single system call category. System calls are classified into the following categories:

![[Pasted image 20250509112400.png]]

---
## 1. File System Operations

These system calls are made while working with files in OS, File manipulation operations such as creation, deletion, termination etc.

- **open():** Opens a file for reading or writing. A file could be of any type like text file, audio file etc.
- **read():** Reads data from a file. Just after the file is opened through open() system call, then if some process want to read the data from a file, then it will make a read() system call.
- **write():** Writes data to a file. Wheneve the user makes any kind of modification in a file and saves it, that's when this is called.
- **close():** Closes a previously opened file.
- **seek():** Moves the file pointer within a file. This call is typically made when we the user tries to read the data from a specific position in a file. For example, read from line - 47. Than the file pointer will move from line 1 or wherever it was previously to line-47.

#### example
##### read() function 

- **kernel** - high privilege mode 
- **user** - low privilege mode

1. push n bytes
2. push &buffer 
3. push file descriptor
4. call read
5. put syscall # in reg 
6. trap ( interrupt ) to kernel
7. dispatch envelop
8. works ....
9. sys call handler
10. return to caller
11. increment stack pointer
## 2. Process Control

These types of system calls deal with process creation, process termination, process allocation, deallocation etc. Basically manages all the process that are a part of OS.

- **fork():** Creates a new process (child) by duplicating the current process (parent). This call is made when a process makes a copy of itself and the parent process is halted temporarily until the child process finishes its execution.
- **exec():** Loads and runs a new program in the current process and replaces the current process with a new process. All the data such as stack, register, heap memory everything is replaced by a new process and this is known as [overlay](https://www.geeksforgeeks.org/overlays-in-memory-management/). For example, when you execute a java byte code using command - java "filename". Then in the background, exec() call will be made to execute the java file and JVM will also be executed.
- **wait():** The primary purpose of this call is to ensure that the parent process doesn't proceed further with its execution until all its child processes have finished their execution. This call is made when one or more child processes are forked.
- **exit()**: It simply terminates the current process.
- **kill():** This call sends a signal to a specific process and has various purpose including - requesting it to quit voluntarily, or force quit, or reload configuration.

## 3. Memory Management

These types of system calls deals with memory allocation, deallocation & dynamically changing the size of a memory allocated to a process. In short, the overall management of memory is done by making these system calls.

- **brk():** Changes the data segment size for a process in [HEAP Memory](https://www.geeksforgeeks.org/what-is-a-memory-heap/). It takes an address as argument to define the end of the heap and explicitly sets the size of HEAP.
- **sbrk():** This call is also for memory management in heap, it also takes an argument as an integer (+ve or -ve) specifying whether to increase or decrease the size respectively.
- **mmap(): Memory** Map - It basically maps a file or device into main memory and further into a process's address space for performing operations. And any changes made in the content of a file will be reflected in the actual file.
- **munmap():** Unmaps a memory-mapped file from a process's address space and out of main memory
- **mlock() and unlock():** memory lock defines a mechanism through which certain pages stay in memory and are not swapped out to the swap space in the disk. This could be done to avoid page faults. Memory unlock is the opposite of lock, it releases the lock previously acquired on pages.

## 4. Interprocess Communication (IPC)

When two or more process are required to communicate, then various [IPC](https://www.geeksforgeeks.org/inter-process-communication-ipc/) mechanism are used by the OS which involves making numerous system calls. Some of them are :

- **pipe():** Creates a unidirectional communication channel between processes. For example, a parent process may communicate to its child process through a pipe making a parent process as input source of its child process.
- **socket():** Creates a network socket for communication. Processes in same or other networks can communicate through this socket, provided that they have necessary network permissions granted.
- **shmget():** It is short for - 'shared-memory-get'. It allows one or more processes to share a portion of memory and achieve interprocess communication.
- **semget():** It is short for - 'semaphore-get'. This call typically manages the coordination of multiple processes while accessing a shared resource that is, the critical section.
- **msgget():** It is short for - 'message-get'. IPC mechanism has one of the fundamental concept called - 'message queue' which is a queue data structure inside memory through which various processes communicate with each other. This message queue is allocated through this call allowing other processes a structured way of communication for data exchange purpose.

## 5. Device Management

The device management system calls are used to interact with various peripherial devices attached to the PC or even the management of the current device.

- **SetConsoleMode():** This call is made to set the mode of console (input or output). It allows a process to control various console modes. In windows, it is used to control the behaviour of command line.
- **WriteConsole():** It allows us to write data on console screen.
- **ReadConsole():** It allows us to read data from console screen (if any arguments are provided).
- **open():** This call is made whenever a device or a file is opened. A unique file descriptor is created to maintain the control access to the opened file or device.
- **close():** This call is made when the system or the user closes the file or device.
---
## **Importance of System Calls** 

- **Efficient Resource Management:** System Calls help your computer manage its resources efficiently. They allocate and manage memory so programs run smoothly without using up too many resources. This is important for [multitasking](https://www.geeksforgeeks.org/difference-between-multitasking-multithreading-and-multiprocessing/) and overall performance.
- **Security and Isolation:** System Calls ensure that one program cannot interfere with or access the memory of another program. This enhances the security and stability of your device.
- **Multitasking Capabilities:** System Calls support multitasking, allowing multiple programs to run simultaneously. This improves productivity and makes it easy to switch between applications.
- **Enhanced Control:** System Calls provide a high level of control over your device’s operations. They allow you to start and stop processes, manage files, and perform various system-related tasks.
- **Input/Output (I/O) Operations:** System Calls enable communication with input and output devices, such as your keyboard, mouse, and screen. They ensure that these devices work effectively.
- **Networking and Communication:** System Calls facilitate networking and communication between different applications. They make it easy to transfer data over networks, browse the web, send emails, and connect online.

#### Services provided by system calls
1. Process creation and management
2. Main memory management
3. File Access, Directory and File management
4. Device handling (I/O)
5. Protection 
6. Networking .etc


--- 

## Posix Standard

---
Bootloader 
