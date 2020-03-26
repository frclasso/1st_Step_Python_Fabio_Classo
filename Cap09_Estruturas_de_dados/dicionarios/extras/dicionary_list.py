#!/usr/bin/env python3

"""Loading the dishwasher"""

# dirt dishes in the sink
sink = ['bowl', 'plate', 'cup']

for dish in list(sink):
    print('Putting {} in the dishwasher'.format(dish))
    sink.remove(dish)
print()
print('Sink:',sink)