#!/usr/bin/env python3

"""lambda function within filter to select fruits starting with "A" from a list"""

fruit = ["Apple", "Banana", "Pear", "Apricot", "Orange"]
filter_object = filter(lambda s: s[0] == "A", fruit)

print(list(filter_object))
