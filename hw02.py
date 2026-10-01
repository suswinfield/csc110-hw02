# ------------------------------------------------------
#        Name: Susannah Winfield
#       Peers: (add any collaborators)
#  References: https://www.geeksforgeeks.org/python/how-to-use-a-variable-from-another-function-in-python/
# ------------------------------------------------------
"""user input for x and y

first list item displays "give me x:" and saves the user input as an integer named x.
second item displays "give me y:" and saves the user input as an integer named y.

Returns:
integers x and y
"""
def read_two_ints():
    x,y = [int(input("give me x: ")),int(input("give me y: "))]
    return x,y
"""computes $\frac{a * b}{a + b}$ for user input x and y

for any a and b, computes a*b and a+b and saves them as local variables
prints both the numerator and the denominator
divides a*b by a+b and saves that value as a global variable

    a_times_b = a*b
    a_plus_b = a+b
    ab_multadd = (a*b)/(a+b)
    
Returns:
    ab_multadd (float)
"""
def compute_multadd(a, b):
    #ab_multadd is global so it can be used in print_fancy
    global ab_multadd
    #computes numerator(first) and denominator(second)
    a_times_b,a_plus_b = [a*b,a+b]
    #divides numerator by denominator
    ab_multadd = a_times_b/a_plus_b
    #display numerator and denominator results
    print("mult result:",a_times_b,"\n""add result:",a_plus_b,end="\n\n")
    return ab_multadd
"""displays final computation

prints 16 asterisks, a, b, ab_multadd, and 16 equal signs in that order

    a = first number in compute_multadd
    b = second number in compute_multadd
    ab_multadd = return of compute_multadd
    
Returns nothing
"""
def print_fancy(a, b, ab_multadd):
    #prints, a, b, and the final answer in that order
    print("*"*16,"\n""RESULTS:","\n""first number:",a,"\n""second number:",b,"\n""multadd result:",ab_multadd)
    print("="*16,end="\n\n")
"""calls every function

runs read_two_ints and saves the user inputted integers x and y
runs compute_multadd for x and y, then saves that value as xy_multadd
    x = user input for x
    y = user input for y
    xy_multadd = value of compute_multadd for user input x and y
    print_fancy(x,y,xy_multadd) = runs print_fancy for given x and y
    
Returns nothing
"""
def main ():
    #calls the funnction read_two_ints and saves x and y
    x,y = read_two_ints()
    #saves the xy_multadd output for x and y given above
    xy_multadd = compute_multadd(x,y)
    #displays the output, x, and y from above
    print_fancy(x,y,xy_multadd)
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
