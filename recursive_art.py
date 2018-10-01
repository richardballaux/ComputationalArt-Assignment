"""Mini-project 2
@author: Richard Ballaux"""

import random
import math
from PIL import Image


def build_random_function(min_depth, max_depth):
    """Build a random function.

    Builds a random function of depth at least min_depth and depth at most
    max_depth. (See the assignment write-up for the definition of depth
    in this context)

    Args:
        min_depth: the minimum depth of the random function
        max_depth: the maximum depth of the random function

    Returns:
        The randomly generated function represented as a nested list.
        (See the assignment writ-eup for details on the representation of
        these functions)
    """
    depth = random.randint(min_depth,max_depth)
    #print('depth',depth)
    functionNumber = random.randint(0,5)
    #print('functionNumber',functionNumber)
    if depth == 1:
        return random.choice([["x"],["y"]])
        #choose randomly between x or y
    else:
        #if depth is different from 1 go deeper
        if functionNumber == 0:
            #product
            return ["prod",build_random_function(depth-1,depth-1),build_random_function(depth-1,depth-1)]
        if functionNumber == 1:
            return ["avg",build_random_function(depth-1,depth-1),build_random_function(depth-1,depth-1)]
        if functionNumber == 2:
            return ["cos_pi",build_random_function(depth-1,depth-1)]
        if functionNumber == 3:
            return ["sin_pi",build_random_function(depth-1,depth-1)]

        if functionNumber == 4:
            #power 2
            return ["power2",build_random_function(depth-1,depth-1)]
        if functionNumber == 5:
            #sqrt
            return ["sqrt",build_random_function(depth-1,depth-1)]
        if functionNumber == 6:
            # just x
            return ["x"]
        if functionNumber == 7:
            # just y
            return ["y"]

#print(build_random_function(3,5))


def evaluate_random_function(f, x, y):
    """Evaluate the random function f with inputs x,y.

    The representation of the function f is defined in the assignment write-up.

    Args:
        f: the function to evaluate
        x: the value of x to be used to evaluate the function
        y: the value of y to be used to evaluate the function

    Returns:
        The function value

    Examples:
        >>> evaluate_random_function(["x"],-0.5, 0.75)
        -0.5
        >>> evaluate_random_function(["y"],0.1,0.02)
        0.02

    """
    if f[0] == "prod":
        return evaluate_random_function(f[1],x,y)*evaluate_random_function(f[2],x,y)
    if f[0] == "avg":
        return 0.5*(evaluate_random_function(f[1],x,y)+evaluate_random_function(f[2],x,y))
    if f[0] == "cos_pi":
        return math.cos(math.pi*evaluate_random_function(f[1],x,y))
    if f[0] == "sin_pi":
        return math.sin(math.pi*evaluate_random_function(f[1],x,y))
    if f[0] == "x":
        return x
    if f[0] == "y":
        return y
    if f[0] == "power2":
        return math.pow(evaluate_random_function(f[1],x,y),2)
    if f[0] == "sqrt":
        return math.sqrt(math.fabs(evaluate_random_function(f[1],x,y)))
    #filled_in_string =  f[0].replace("x",str(x))
    #filled_in_string = filled_in_string.replace("y",str(y))
    #return eval(filled_in_string)


def remap_interval(val,
                   input_interval_start,
                   input_interval_end,
                   output_interval_start,
                   output_interval_end):
    """Remap a value from one interval to another.

    Given an input value in the interval [input_interval_start,
    input_interval_end], return an output value scaled to fall within
    the output interval [output_interval_start, output_interval_end].

    Args:
        val: the value to remap
        input_interval_start: the start of the interval that contains all
                              possible values for val
        input_interval_end: the end of the interval that contains all possible
                            values for val
        output_interval_start: the start of the interval that contains all
                               possible output values
        output_inteval_end: the end of the interval that contains all possible
                            output values

    Returns:
        The value remapped from the input to the output interval

    Examples:
        >>> remap_interval(0.5, 0, 1, 0, 10)
        5.0
        >>> remap_interval(5, 4, 6, 0, 2)
        1.0
        >>> remap_interval(5, 4, 6, 1, 2)
        1.5
    """
    return (val-input_interval_start)*(output_interval_end-output_interval_start)/(input_interval_end-input_interval_start) + output_interval_start;



def color_map(val):
    """Maps input value between -1 and 1 to an integer 0-255, suitable for use as an RGB color code.

    Args:
        val: value to remap, must be a float in the interval [-1, 1]

    Returns:
        An integer in the interval [0,255]

    Examples:
        >>> color_map(-1.0)
        0
        >>> color_map(1.0)
        255
        >>> color_map(0.0)
        127
        >>> color_map(0.5)
        191
    """
    # NOTE: This relies on remap_interval, which you must provide
    color_code = remap_interval(val, -1, 1, 0, 255)
    return int(color_code)


def test_image(filename, x_size=350, y_size=350):
    """Generate a test image with random pixels and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (random.randint(0, 255),  # Red channel
                            random.randint(0, 255),  # Green channel
                            random.randint(0, 255))  # Blue channel

    im.save(filename)


def generate_art(filename, x_size=350, y_size=350):
    """Generate computational art and save as an image file.

    Args:
        filename: string filename for image (should be .png)
        x_size, y_size: optional args to set image dimensions (default: 350)
    """
    # Functions for red, green, and blue channels - where the magic happens!
    red_function = build_random_function(7,9)
    print(red_function)
    green_function = build_random_function(7,9)
    print(green_function)
    blue_function = build_random_function(7,9)
    print(blue_function)

    # Create image and loop over all pixels
    im = Image.new("RGB", (x_size, y_size))
    pixels = im.load()
    for i in range(x_size):
        for j in range(y_size):
            x = remap_interval(i, 0, x_size, -1, 1)
            y = remap_interval(j, 0, y_size, -1, 1)
            pixels[i, j] = (
                color_map(evaluate_random_function(red_function, x, y)),
                color_map(evaluate_random_function(green_function, x, y)),
                color_map(evaluate_random_function(blue_function, x, y))
            )

    im.save(filename)


if __name__ == '__main__':
    import doctest
    #doctest.testmod()
    #doctest.run_docstring_examples(evaluate_random_function,globals(),verbose=True)
    for i in range(35,40):
        name = "myart"+str(i)+".png"
        generate_art(name,1920,1080)
    #print(evaluate_random_function(["x**2+5*y"],2.2,5.3))
