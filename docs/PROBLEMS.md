# Problems

### 1. Threads / sockets / subrocesses
The problem here is simple, how should i handle the start of the applications
##

### 2. Handle console, applications, childrens
How can i handle all the connections with console, applications and children
Possible solution:
 - [ ] create 3 different subprocesses, one for the childrens, one for the applications and one for the console
 - [ ] on every subprocess create a socket to handle connection to their target
 - [ ] then send loggers to the first cardianl socket to log the data
 - [ ] make a script to route the commands from a target to another (like from console to application, if there is a command to close all apps)
##

### 3.
##
