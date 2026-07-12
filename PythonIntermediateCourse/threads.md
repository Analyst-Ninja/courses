#### Threads: 
- An entity within the process that can be scheduled (also known as 'lightweight process') 
- A process can spawn multiple threads

##### Advantages 
+ All threads within the process share the same memory
+ Lightweight
+ Starting a thread is faster that strating a process
+ `Great for I/O bound Tasks` -> eg. for read/write data on hard drive or I/O on the network
##### Disadvantages 
- Threading is limited by GIL: Only 1 thread at a time
- No effect for CPU bound Tasks
- Not Interruptable/ Killable --> `Memory Leaks` can be there
- Careful with `race conditions` :  It occurs when 2 or more threads are trying to modify the same variable at the same time