import os

print os.name
print os.path.abspath(".")
print os.listdir('..')
print [x for x in os.listdir('..') if os.path.isdir(x)]