# Interactive Linear Algebra Visualizer

An interactive Python script that visualizes linear equations in 2D and 3D space with **real-time text box controls** to adjust constants and see instant updates!

## Features

### Simple and Intuitive
- **Choose number of variables**: Start by selecting 2D (2 variables) or 3D (3 variables)
- **Interactive text boxes**: Adjust equation constants and see results immediately
- **Real-time visualization**: Watch how changing constants affects the equation
- **Clean interface**: Text boxes on the right side for easy access

### 2D Visualization (2 Variables)
- **Linear Equation**: Visualize lines of the form `ax + by = c`
- **Interactive Controls**:
  - Text boxes for constants `a`, `b`, and `c`
  - Type any value and press ENTER to update
  - See the line update instantly on the plot
- **Features**:
  - Grid and axes for reference
  - Automatic handling of vertical lines (when b=0)
  - Equation displayed in the title

### 3D Visualization (3 Variables)
- **Plane Equation**: Visualize planes of the form `ax + by + cz = d`
- **Interactive Controls**:
  - Text boxes for constants `a`, `b`, `c`, and `d`
  - Type any value and press ENTER to update
  - Watch the plane adjust in real-time
- **Features**:
  - 3D surface rendering with color gradient
  - Normal vector visualization (red arrow)
  - Rotatable 3D view (click and drag)
  - Equation displayed in the title

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install numpy matplotlib
```

## Usage

Run the script:
```bash
python linear_algebra_visualizer.py
```

### How It Works

1. **Main menu appears**: Choose between "2 Variables (2D)" or "3 Variables (3D)"
2. **Visualization opens**: A plot appears with text boxes on the right side
3. **Adjust constants**: Type values in the text boxes and press ENTER
4. **Watch updates**: The plot updates immediately to show the new equation
5. **Return to menu**: Click "Return to Menu" button or close the window
6. **Exit**: Click "Exit Program" from the menu or close the menu window

**Everything is GUI-based** - no command-line typing needed!

### GUI Controls

**Text Boxes**:
- Located on the right side of the visualization
- Type any numeric value (integers or decimals)
- Press ENTER to apply the value
- Plot updates automatically
- Clear instructions displayed below the text boxes

**2D Plot**:
- Shows the line `ax + by = c`
- Grid and axes help identify points
- Equal aspect ratio for accurate representation
- Legend shows the current equation

**3D Plot**:
- Shows the plane `ax + by + cz = d`
- Click and drag to rotate the 3D view
- Scroll to zoom in/out
- Red arrow shows the normal vector to the plane
- Colored surface for better visualization

### Example Workflows

**Exploring 2D Linear Equations:**
1. Start the program and click "2 Variables (2D Linear Equation)"
2. Default equation is `2x + 3y = 6`
3. Change `a` to 1 and press ENTER - see the line rotate
4. Change `b` to 0 and press ENTER - see it become a vertical line
5. Change `c` to adjust where the line intersects the axes
6. Try `a=1, b=1, c=5` to get the line `x + y = 5`

**Understanding 3D Planes:**
1. Start the program and click "3 Variables (3D Plane Equation)"
2. Default equation is `2x + 3y + z = 6`
3. Click and drag the plot to rotate it and view from different angles
4. Change `a` to 0 and press ENTER - see the plane become parallel to the x-axis
5. Change `d` to shift the plane along the normal vector
6. Try `a=1, b=0, c=0, d=5` to get a plane perpendicular to the x-axis

**Experimenting with Coefficients:**
1. In 2D: Set `a=0, b=1, c=3` to get a horizontal line at y=3
2. In 2D: Set `a=1, b=0, c=2` to get a vertical line at x=2
3. In 3D: Set `a=0, b=0, c=1, d=5` to get a horizontal plane at z=5
4. In 3D: Watch the normal vector (red arrow) change direction as you adjust a, b, c

## Key Features

- **Fully GUI-based**: Everything controlled through intuitive graphical interface
- **Simple workflow**: Choose 2D or 3D, then adjust constants
- **Text box controls**: Type exact values for precise control
- **Real-time updates**: See changes immediately when you press ENTER
- **Interactive 3D**: Rotate 3D plots by clicking and dragging
- **Normal vector display**: In 3D, see the normal vector to understand plane orientation
- **Educational**: Perfect for learning linear equations and plane geometry

## Requirements

- Python 3.7+
- NumPy
- Matplotlib

## Tips

**For 2D Linear Equations:**
- When `b ≠ 0`, the line has slope `-a/b`
- When `b = 0`, the line is vertical at `x = c/a`
- The x-intercept is at `(c/a, 0)` when `a ≠ 0`
- The y-intercept is at `(0, c/b)` when `b ≠ 0`

**For 3D Planes:**
- The normal vector is `(a, b, c)` - perpendicular to the plane
- The red arrow shows the direction the plane is "facing"
- Changing `d` shifts the plane parallel to itself
- When `c = 0`, the plane is perpendicular to the xy-plane

**Interaction:**
- Text boxes accept negative numbers (use `-` sign)
- Text boxes accept decimals (use `.` for decimal point)
- Press ENTER after typing to apply changes
- Use the "Return to Menu" button to try a different visualization
- Click and drag to rotate 3D plots for better viewing angles

## Educational Use Cases

- **Understanding linear equations**: See how coefficients affect line position and slope
- **Learning plane geometry**: Visualize how planes exist in 3D space
- **Normal vectors**: See the relationship between equation coefficients and plane orientation
- **Intercepts**: Observe where lines/planes cross the axes
- **Special cases**: Explore vertical lines, horizontal planes, etc.
- **Teaching**: Great tool for demonstrating concepts in class or homework

## Future Enhancements

Possible additions:
- System of equations (multiple lines/planes with intersection)
- Vector operations (addition, cross product)
- Linear transformations (matrices)
- Parameter ranges for animation
- Export functionality for saving images
