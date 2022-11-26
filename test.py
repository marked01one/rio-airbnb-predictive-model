import pytest as test

x = ['2 private Half-bath', 'Private half-bath', 'Shared half-bath']

for i in x:
    print(bath_clean(i)["bathroom_type"])