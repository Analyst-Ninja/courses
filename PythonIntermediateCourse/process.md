#### Process - An Instance of a program (eg. Python Interpreter)
##### Advatages
+ Takes the advantage of multiple CPUs
+ Separate Memory Space --> Memory is not shared between any processes
+ Great for CPU bounding process 
+ New process is started independently from other processes
+ Processes are interruptable/ killable
+ Open GIL (Global Interpreter Lock) for each process --> Avoids GIL limitations
+ Great for complex operations
##### Disadvatages
- Heavyweight
- starting a process is slower that starting a thread
- Requires More Memory
- IPC (Inter-Process Communication) is more complicated