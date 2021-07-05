
from num2words import num2words

numero = 1217.5


def converte_extenso(amount):

    amount_str = '1.217,50'

    if amount_str.count('.') == 1:
        if ',' in amount_str:
            unidade_milhar, unidade_centenas_centavos = amount_str.split('.')
            unidade_centenas, centavos = unidade_centenas_centavos.split(',')
            value = '{} mil {} reais e {} centavos'.format(num2words(int(unidade_milhar), lang='pt-BR'),
                                                           num2words(int(unidade_centenas), lang='pt-BR'),
                                                           num2words(int(centavos), lang='pt-BR'))
        else:
            unidade_milhar, unidade_centenas = amount_str.split('.')
            value = '{} mil {} reais e zero centavos'.format(num2words(int(unidade_milhar), lang='pt-BR'),
                                                             num2words(int(unidade_centenas), lang='pt-BR'))
        return value.upper()
    if amount_str.count('.') == 2:
        if ',' in amount_str:
            unidade_milhao, unidade_milhar, unidade_centenas_centavos = amount_str.split('.')
            unidade_centenas, centavos = unidade_centenas_centavos.split(',')
            value = '{} milhão(ões) {} mil {} reais e {} centavos'.format(
                num2words(int(unidade_milhao), lang='pt-BR'),
                num2words(int(unidade_milhar), lang='pt-BR'),
                num2words(int(unidade_centenas), lang='pt-BR'),
                num2words(int(centavos), lang='pt-BR'))
        else:
            unidade_milhao, unidade_milhar, unidade_centenas = amount_str.split('.')
            value = '{} milhão(ões) {} mil {} reais e zero centavos'.format(
                num2words(int(unidade_milhao), lang='pt-BR'),
                num2words(int(unidade_milhar), lang='pt-BR'),
                num2words(int(unidade_centenas), lang='pt-BR'))

        return value.upper()


print(converte_extenso(numero))