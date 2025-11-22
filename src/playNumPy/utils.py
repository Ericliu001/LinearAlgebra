import numpy as np
import matplotlib.pyplot as plt


def plot_lines(A_system):
    """
    Plot lines from a system of linear equations.

    Parameters:
    A_system: augmented matrix of shape (n, 3) where each row represents
              a linear equation: a*x + b*y = c
    """
    n_lines = A_system.shape[0]

    # Create x values for plotting
    x_vals = np.linspace(-10, 10, 400)

    # Create a new figure
    plt.figure(figsize=(10, 8))

    # Plot each line
    for i in range(n_lines):
        a, b, c = A_system[i]

        # Handle different cases
        if b != 0:
            # Standard case: y = (c - a*x) / b
            y_vals = (c - a * x_vals) / b
            plt.plot(x_vals, y_vals, label=f'Line {i+1}: {a:.1f}x + {b:.1f}y = {c:.1f}')
        elif a != 0:
            # Vertical line: x = c/a
            x_const = c / a
            plt.axvline(x=x_const, label=f'Line {i+1}: {a:.1f}x = {c:.1f}')
        else:
            # Degenerate case (0 = c)
            print(f"Line {i+1} is degenerate: 0 = {c:.1f}")

    # Try to find and plot the intersection point (solution)
    try:
        A_coef = A_system[:, :2]
        b_vec = A_system[:, 2]
        solution = np.linalg.solve(A_coef, b_vec)
        plt.plot(solution[0], solution[1], 'ro', markersize=10,
                label=f'Solution: ({solution[0]:.2f}, {solution[1]:.2f})')
    except np.linalg.LinAlgError:
        print("No unique solution exists (lines are parallel or coincident)")

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('System of Linear Equations')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='k', linewidth=0.5)
    plt.axvline(x=0, color='k', linewidth=0.5)
    plt.axis('equal')
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.show()