Shell Basics
Welcome to the Shell Basics README! This comprehensive guide covers fundamental concepts and commands for working with the shell in Unix-like operating systems.

General
RTFM: RTFM stands for "Read The Manual" or "Read The Fine Manual." It's a humorous way of suggesting that someone should consult the documentation before asking for help.
Shebang: The shebang is a special character sequence #! at the beginning of a script file that indicates the path to the interpreter to use when executing the script. For example:
bash
Copy code
#!/bin/bash
Shell: The shell is a command-line interface that allows users to interact with the operating system. It interprets commands entered by the user and executes them.
Terminal vs. Shell: A terminal is a program that provides a text-based interface for interacting with the shell. The shell, on the other hand, is the command interpreter that processes commands entered by the user.
Shell Prompt: The shell prompt is the text displayed in the terminal to indicate that the shell is ready to accept commands. By default, it typically ends with a $ for regular users and # for the root user.
Navigation
cd, pwd, ls:
cd: Change directory. Example:
bash
Copy code
cd /path/to/directory
pwd: Print working directory. Example:
bash
Copy code
pwd
ls: List files and directories. Example:
bash
Copy code
ls
Filesystem Navigation: Use cd to navigate the filesystem by specifying the path to the desired directory.
. and .. Directories: . represents the current directory, while .. represents the parent directory.
Working Directory: The working directory is the current directory in which the user is operating. Use pwd to print it and cd to change it.
Root Directory: The root directory is the top-level directory in the filesystem, denoted by /.
Home Directory: The home directory is the default directory for a user when they log in. Use cd with ~ or $HOME to go there.
Hidden Files: Hidden files in Unix-like systems start with a . and are not normally listed by ls. Use ls -a to list them.
cd - Command: cd - is used to change the working directory to the previous directory.
Looking Around
ls, less, file:

ls: List files and directories. Example:
bash
Copy code
ls
less: Display file contents page by page. Example:
bash
Copy code
less filename.txt
file: Determine file type. Example:
bash
Copy code
file filename.txt
Options and Arguments: Commands can accept options (flags) and arguments (parameters) to modify their behavior or specify additional information.

ls Long Format: Use ls -l to display the long format of ls, which includes detailed information about files and directories.

A Guided Tour
ln Command: The ln command is used to create links between files. It can create both symbolic links and hard links.

Symbolic Link: Create a symbolic link. Example:
bash
Copy code
ln -s target_link symbolic_link
Hard Link: Create a hard link. Example:
bash
Copy code
ln target_link hard_link
Common/Important Directories: Important directories include /bin, /usr/bin, /etc, /var, and /home, among others.

Symbolic vs. Hard Links: Symbolic links are pointers to files or directories, while hard links are directory entries pointing to the same inode.

Manipulating Files
cp, mv, rm, mkdir:

cp: Copy files and directories. Example:
bash
Copy code
cp source_file destination_directory
mv: Move or rename files and directories. Example:
bash
Copy code
mv old_name new_name
rm: Remove files and directories. Example:
bash
Copy code
rm filename
mkdir: Create directories. Example:
bash
Copy code
mkdir new_directory
Wildcards: Wildcards are characters used for pattern matching. Common wildcards include *, ?, and [ ].

Example of using wildcards:
bash
Copy code
ls *.txt
Working with Commands
type, which, help, man:
type: Display information about a command. Example:
bash
Copy code
type ls
which: Show the path to an executable. Example:
bash
Copy code
which ls
help: Provide help for built-in commands. Example:
bash
Copy code
help cd
man: Display manual pages. Example:
bash
Copy code
man ls
Reading Man Pages
Reading a Man Page: Use man followed by the name of the command to read its manual page.
Example:
bash
Copy code
man ls
Man Page Sections: Man pages are divided into sections, with each section covering a different topic. Section numbers include User commands (1), System calls (2), and Library functions (3).
Keyboard Shortcuts for Bash
Common Shortcuts: Common keyboard shortcuts for Bash include Ctrl + C to cancel the current command, Ctrl + D to exit the terminal, and Ctrl + L to clear the screen.
LTS
LTS: LTS stands for "Long-Term Support." It refers to versions of software or operating systems that receive extended support and updates over an extended period.
