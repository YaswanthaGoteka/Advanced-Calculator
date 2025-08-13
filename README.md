# Advanced-Calculator
This Python script allows users to calculate various properties of common geometric shapes based on user input. It also contains a simple snippet to create a pandas DataFrame from user-entered column titles and values.

## Features
Geometry Calculator
Supports shapes:
- Triangle
- Rhombus / Diamond
- Rectangle / Square

For Triangles, calculate:
- Area
- Height
- Hypotenuse
- Base
- Altitude
- Height and Hypotenuse from angle and base
- For Rhombus/Diamond, calculate:
- Area (with one or two diagonals)
- Side length from diagonals
- Height from side length and angle

For Rectangle/Square, calculate:
- Missing side length when diagonal and one side are given
- Area and side lengths from one or two diagonals
- Diagonal length
- User-friendly input prompts and validation for shape and calculation types.

Simple DataFrame Creator (pandas)
Allows users to enter a column title and multiple values for that column.

Creates a pandas DataFrame from the entered data.

Prints the resulting DataFrame.

## Usage:
1. Run the script (uncomment and run relevant parts):

2. For geometry calculations, uncomment the geometry calculator code block.

3. For DataFrame creation, uncomment the pandas snippet.

4. Follow on-screen prompts to select shape, calculation type, and input required values.

5. View calculated results printed to the console.

## Requirements:
- Python 3
- math module (standard library)
- pandas library (only if using DataFrame snippet)

## Example Usage:
~~~
These are your options:
['triangle', 'rhombus', 'diamond', 'rectangle', 'square']
What shape do you want to find the info of? triangle
Options: ['height', 'area', 'hypotenuse', 'base', 'altitude', 'height-hypotenuse']
What do you want to find in a triangle? area
Height: 5
Base: 10
Area: 25.0
~~~

Notes: 
- The script uses basic trigonometry and geometry formulas.
- Input validation is included for most options, but careful input is recommended.
- The DataFrame creation snippet is basic and requires improvement for multiple columns or extended use.


