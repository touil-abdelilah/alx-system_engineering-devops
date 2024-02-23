# Understanding Processes and Signals

Welcome to the README on Processes and Signals! This guide will help you understand the concepts of processes, PIDs, signals, and commands related to process management in Unix-like operating systems.

## Introduction

In Unix-like operating systems, a process is an instance of a running program. Each process is assigned a unique identifier called a Process ID (PID). Processes communicate with each other and the operating system through signals, which are used to convey information or request actions.

## Key Concepts

### Process ID (PID)

- A Process ID (PID) is a unique identifier assigned to each running process.
- It is used by the operating system to track and manage processes.

### Process

- A process is an instance of a running program.
- It consists of the program's code, data, and resources, such as memory and CPU time.

### Finding a Process' PID

- Use the `ps` command to list processes along with their PIDs.
- Alternatively, use `pgrep` to search for processes by name and retrieve their PIDs.

### Killing a Process

- Use the `kill` command followed by the PID to terminate a process.
- Alternatively, use `pkill` followed by the process name to kill processes by name.

### Signals

- Signals are software interrupts used to communicate with processes.
- They can be used to request actions, such as terminating a process or reloading configuration files.

### Non-Ignorable Signals

- Two signals, `SIGKILL` and `SIGSTOP`, cannot be ignored by processes.
- `SIGKILL` forces termination of a process, while `SIGSTOP` suspends a process.

## Explaining Commands

### `ps`

- The `ps` command is used to list currently running processes.
- It provides information such as PID, terminal associated with the p
### `pgrep`

- `pgrep` is used to search for processes by name and retrieve their PIDs.
- It is commonly used in scripts to automate process management tasks.

### `pkill`

- `pkill` is used to send signals to processes based on their name.
- It terminates or signals processes matching the specified criteria.

### `kill`

- The `kill` command is used to send signals to processes.
- By default, it sends the `SIGTERM` signal, which requests termination of a process.

### `exit`

- `exit` is a command used to exit a shell session or terminate a script.
- It returns control to the parent process or shell.

### `trap`

- `trap` is a shell command used to set up actions to be taken when signals are received.
- It allows scripts to handle signals gracefully, such as cleaning up resources before exiting
