#!/usr/bin/env python3

specials = {'Sunday':'spinach',
            'Monday': 'mushrom',
            'Tuesday':'pepperoni',
            'Wednesday':'veggie',
            'Thursday':'bbq chiken',
            'Friday':'sausage',
            'Saturday':'Hawaiian'
            }


def order(day):
    pizza = specials[day]
    print('Order the {} pizza.'.format(pizza))

order('Saturday')