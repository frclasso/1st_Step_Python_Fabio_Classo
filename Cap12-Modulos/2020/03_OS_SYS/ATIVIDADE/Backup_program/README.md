The problem
===========

The problem we want to solve is:
I want a program which creates a backup of all my important files.


Although, this is a simple problem, there is not enough information for us to get started
with the solution. A little more analysis is required. For example, how do we specify
which files are to be backed up? How are they stored? Where are they stored?


After analyzing the problem properly, we design our program. We make a list of things
about how our program should work. In this case, I have created the following list on
how I want it to work. If you do the design, you may not come up with the same kind of
analysis since every person has their own way of doing things, so that is perfectly okay.


• The files and directories to be backed up are specified in a list.
• The backup must be stored in a main backup directory.
• The files are backed up into a zip file.
• The name of the zip archive is the current date and time.
• We use the standard zip command available by default in any standard GNU/
Linux or Unix distribution. Note that you can use any archiving command you want
as long as it has a command line interface.



