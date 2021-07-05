#!/usr/bin/env python3


class CircuitBreaker:
    def __init__(self, max_amps):
        self.capacity = max_amps  # max capacity in amps
        self.load = 0

    def connect(self, amps):
        if self.load + amps > self.capacity:
            raise Exception("Connect will exceed capacity.")
        elif self.load + amps < 0:
            raise Exception("Connect will cause negative load.")
        else:
            self.load += amps

# create a 20A circuit breaker
cb = CircuitBreaker(20)

