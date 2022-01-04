sunny = True
windy = True

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.

# Below, we've gone ahead and written some code that uses a
# conditional to print a message based on the variables above.
# Revise this code so that it uses nested conditionals instead
# of the 'and' operator. There should be _no_ instances of the
# 'and' reserved word in your code, but it should behave the
# same as it did originally.


# if sunny and not windy:
#     #print("Wear a hat!")
#
# if sunny and windy:
#     print("Enjoy the breeze!")

if sunny:
    if not windy:
        print("Wear a hat!")
    else:
        print("Enjoy the breeze!")


