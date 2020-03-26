#!/usr/bin/env python3

"""Handling household problems"""


class EletricalError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


class PlumbingError(Exception):
    def __init__(self, device, problem):
        self.device = device
        self.problem = problem

    def __str__(self):
        return "The {} is {}!".format(self.device, self.problem)


def cause_erro(error_type):
    if error_type == 'electrical':
        raise EletricalError('circuit error', 'overloaded')
    elif error_type == 'plumbing':
        raise PlumbingError('dishwasher', 'spraying water')
    else:
        raise Exception(" a generic household problem.")
try:
    cause_erro(input('Choose between electrical or plumbing: '))
except EletricalError as e:
    print(e)
    print('Fix it myself.')
except PlumbingError as e:
    print(e)
    print('Call the plumber.')
except:
    print('Call the landlord.')