import sys

print(sys.path)

print(sys.version)


if sys.platform.startswith('freebsd'):
    print('Welcome to FreeBSD OS')
elif sys.platform.startswith('linux'):
    print('Welcome to Linux OS')
elif sys.platform.startswith('win32'):
    print('Welcome to Microsoft Windows OS')
elif sys.platform.startswith('darwin'):
    print('Welcome to Mac OSX')
else:
    print('Sistema nao reconhecido...')
