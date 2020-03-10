#  CASO 1
# def outer():
#     x = 'outer x' # comentar essa linha (2) - Traceback NameError: name 'x' is not defined
#
#     def inner():
#         x = 'inner x' # comentar essas linha (1)
#         print(x)
#     inner()
#     print(x)


# CASO 2

def outer():
    x = 'outer x'

    def inner():
        nonlocal x # PASSA A IGNORAR A VARIAVEL LOCAL "x"
        x = 'inner x'
        print(x)
    inner()
    print(x)

outer()