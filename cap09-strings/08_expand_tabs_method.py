#!/usr/bin/python3

"""Description
The expandtabs() method returns a copy of the string in which the tab characters ie. '\t'
are expanded using spaces, optionally using the given tabsize (default 8)..

Syntax
str.expandtabs(tabsize=8)
"""
str = "this is\tstring example....wow!!!"
print ("Original string: " + str)
print ("Defualt exapanded tab: " + str.expandtabs())
print ("Double exapanded tab: " + str.expandtabs(16))