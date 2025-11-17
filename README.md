# Interactive Linear Algebra Visualizer

An interactive Python script that allows you to visualize linear algebra concepts in 2D and 3D space with custom input values.

## Features

### 2D Visualizations (2 Variables)
1. **Vectors**: Vector addition and subtraction with parallelogram visualization
2. **Linear Equation**: Single line (ax + by = c)
3. **System of Linear Equations**: Two lines with intersection point solution
4. **Linear Transformation**: Apply 2x2 matrices to vectors

### 3D Visualizations (3 Variables)
1. **Vectors**: Vector addition and cross product
2. **Plane**: Single plane with normal vector (ax + by + cz = d)
3. **System of Planes**: Intersection of two planes
4. **Linear Transformation**: Apply 3x3 matrices to vectors

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python main.py
```

### Interactive Menu

The program will guide you through:

1. **Choose dimension**: Select 2D (2 variables) or 3D (3 variables)
2. **Choose visualization type**: Pick from vectors, equations/planes, or transformations
3. **Enter your values**: Input coefficients, constants, or vector components
4. **View the plot**: The visualization will be displayed
5. **Modify or save**: You can:
   - Modify values and refresh the diagram
   - Save the current plot as a PNG image
   - Return to the main menu

### Example Usage

**2D Linear Equation Example:**
```
Choose: 2 Variables (2D)
Choose: Linear Equation
Enter a: 2
Enter b: 3
Enter c: 6
```
This will plot the line 2x + 3y = 6

**3D Vector Example:**
```
Choose: 3 Variables (3D)
Choose: Vectors
Enter v1: (1, 0, 0)
Enter v2: (0, 1, 0)
```
This will show vector addition and cross product

**System of Equations Example:**
```
Choose: 2 Variables (2D)
Choose: System of Linear Equations
Equation 1: 2x + y = 5
Equation 2: x - y = 1
```
This will show both lines and their intersection point (2, 1)

## Features

- Real-time visualization with custom inputs
- Ability to modify values and refresh plots
- Save visualizations as high-resolution PNG images
- Automatic solution calculation for systems of equations
- Additional information (determinants, dot products, cross products)
- Error handling for invalid inputs

## Requirements

- Python 3.7+
- NumPy
- Matplotlib

## Tips

- For linear equations, coefficients can be positive or negative
- For transformations, try identity matrix [[1,0],[0,1]] first to see basis vectors
- The plot automatically scales to fit your data
- You can rotate 3D plots by clicking and dragging
