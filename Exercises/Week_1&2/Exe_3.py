"""
Write an algorithm to find the maximum of three numbers. Ask the user to enter
three different numbers, then compare them and print the largest value.
"""

_FN = float(input("Enter the First Number: "))
_SN = float(input("Enter the Second Number: "))
_TN = float(input("Enter the Third Number: "))


MaxN= _FN

if ( _SN > MaxN ) :
    MaxN = _SN
if ( _TN > MaxN) :
    MaxN = _TN

print (MaxN)
