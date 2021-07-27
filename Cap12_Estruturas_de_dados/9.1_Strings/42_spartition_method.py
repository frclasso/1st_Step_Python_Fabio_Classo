#!/urs/bin/env python3

# Divide a string baseada no separador fornecido

print('foo.bar'.partition('.'))

print('foo@@bar@@baz'.partition('@@'))

print('foo.ba.baz'.partition('@@'))  # Caso nao encontre, retorna duas 9.1_Strings vazias
