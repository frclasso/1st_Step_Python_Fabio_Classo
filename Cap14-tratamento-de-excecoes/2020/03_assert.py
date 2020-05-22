#!/usr/bin/env python3


def KelvinToFahreinheit(Teperature):
    assert (Teperature >= 0), 'Colder than absolute zero'
    return ((Teperature-273)*1.8)+32

print(KelvinToFahreinheit(273))
print(KelvinToFahreinheit(505.78))
#print(KelvinToFahreinheit(0))
#print(KelvinToFahreinheit(-5))