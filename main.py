"""
Interactive Linear Algebra Visualization Script
Allows users to input their own constants and visualize linear algebra concepts
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class LinearAlgebraVisualizer:
    def __init__(self):
        self.dimension = None
        self.visualization_type = None

    def get_dimension_choice(self):
        """Ask user to choose between 2D or 3D"""
        while True:
            print("\n" + "=" * 50)
            print("Choose dimension:")
            print("1. 2 Variables (2D)")
            print("2. 3 Variables (3D)")
            print("0. Exit")
            print("=" * 50)

            choice = input("\nEnter your choice (0-2): ").strip()

            if choice == '0':
                return None
            elif choice == '1':
                return 2
            elif choice == '2':
                return 3
            else:
                print("Invalid choice. Please enter 0, 1, or 2.")

    def get_visualization_type(self, dimension):
        """Ask user what type of visualization they want"""
        while True:
            print("\n" + "=" * 50)
            if dimension == 2:
                print("Choose visualization type:")
                print("1. Vectors (addition/subtraction)")
                print("2. Linear Equation (line)")
                print("3. System of Linear Equations (2 lines)")
                print("4. Linear Transformation (matrix)")
                print("0. Back to main menu")
            else:  # 3D
                print("Choose visualization type:")
                print("1. Vectors (addition/cross product)")
                print("2. Plane (single plane)")
                print("3. System of Planes (2 planes)")
                print("4. Linear Transformation (matrix)")
                print("0. Back to main menu")
            print("=" * 50)

            choice = input("\nEnter your choice (0-4): ").strip()

            if choice in ['0', '1', '2', '3', '4']:
                return choice
            else:
                print("Invalid choice. Please try again.")

    def visualize_2d_vectors(self):
        """Interactive 2D vector visualization"""
        while True:
            print("\n" + "=" * 50)
            print("2D Vector Visualization")
            print("=" * 50)

            try:
                print("\nEnter first vector (v1):")
                v1_x = float(input("  x component: "))
                v1_y = float(input("  y component: "))

                print("\nEnter second vector (v2):")
                v2_x = float(input("  x component: "))
                v2_y = float(input("  y component: "))

                v1 = np.array([v1_x, v1_y])
                v2 = np.array([v2_x, v2_y])
                v_sum = v1 + v2
                v_diff = v1 - v2

                # Create plot
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

                # Vector addition
                ax1.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1,
                          color='r', width=0.006, label=f'v1 = ({v1[0]}, {v1[1]})')
                ax1.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1,
                          color='b', width=0.006, label=f'v2 = ({v2[0]}, {v2[1]})')
                ax1.quiver(0, 0, v_sum[0], v_sum[1], angles='xy', scale_units='xy', scale=1,
                          color='g', width=0.006, label=f'v1 + v2 = ({v_sum[0]:.1f}, {v_sum[1]:.1f})')

                # Parallelogram
                ax1.quiver(v1[0], v1[1], v2[0], v2[1], angles='xy', scale_units='xy',
                          scale=1, color='b', alpha=0.3, width=0.003)
                ax1.quiver(v2[0], v2[1], v1[0], v1[1], angles='xy', scale_units='xy',
                          scale=1, color='r', alpha=0.3, width=0.003)

                max_val = max(abs(v_sum[0]), abs(v_sum[1])) + 1
                ax1.set_xlim(-max_val, max_val)
                ax1.set_ylim(-max_val, max_val)
                ax1.set_aspect('equal')
                ax1.grid(True, alpha=0.3)
                ax1.legend()
                ax1.set_title('Vector Addition')
                ax1.set_xlabel('x')
                ax1.set_ylabel('y')

                # Vector subtraction
                ax2.quiver(0, 0, v1[0], v1[1], angles='xy', scale_units='xy', scale=1,
                          color='r', width=0.006, label=f'v1 = ({v1[0]}, {v1[1]})')
                ax2.quiver(0, 0, v2[0], v2[1], angles='xy', scale_units='xy', scale=1,
                          color='b', width=0.006, label=f'v2 = ({v2[0]}, {v2[1]})')
                ax2.quiver(0, 0, v_diff[0], v_diff[1], angles='xy', scale_units='xy', scale=1,
                          color='purple', width=0.006, label=f'v1 - v2 = ({v_diff[0]:.1f}, {v_diff[1]:.1f})')

                ax2.set_xlim(-max_val, max_val)
                ax2.set_ylim(-max_val, max_val)
                ax2.set_aspect('equal')
                ax2.grid(True, alpha=0.3)
                ax2.legend()
                ax2.set_title('Vector Subtraction')
                ax2.set_xlabel('x')
                ax2.set_ylabel('y')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            # Ask if user wants to modify
            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_2d_linear_equation(self):
        """Interactive 2D linear equation visualization"""
        while True:
            print("\n" + "=" * 50)
            print("2D Linear Equation: ax + by = c")
            print("=" * 50)

            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter constant c: "))

                if a == 0 and b == 0:
                    print("Error: Both coefficients cannot be zero.")
                    continue

                # Create plot
                fig, ax = plt.subplots(figsize=(8, 8))

                x = np.linspace(-10, 10, 100)

                if b != 0:
                    y = (c - a*x) / b
                    ax.plot(x, y, 'b-', linewidth=2, label=f'{a}x + {b}y = {c}')
                else:
                    # Vertical line
                    x_val = c / a
                    ax.axvline(x=x_val, color='b', linewidth=2, label=f'{a}x = {c}')

                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                ax.grid(True, alpha=0.3)
                ax.set_xlim(-10, 10)
                ax.set_ylim(-10, 10)
                ax.set_aspect('equal')
                ax.legend(fontsize=12)
                ax.set_title(f'Linear Equation: {a}x + {b}y = {c}', fontsize=14)
                ax.set_xlabel('x')
                ax.set_ylabel('y')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_2d_system(self):
        """Interactive system of 2D linear equations"""
        while True:
            print("\n" + "=" * 50)
            print("System of Linear Equations")
            print("Equation 1: a1*x + b1*y = c1")
            print("Equation 2: a2*x + b2*y = c2")
            print("=" * 50)

            try:
                print("\nEquation 1:")
                a1 = float(input("  a1: "))
                b1 = float(input("  b1: "))
                c1 = float(input("  c1: "))

                print("\nEquation 2:")
                a2 = float(input("  a2: "))
                b2 = float(input("  b2: "))
                c2 = float(input("  c2: "))

                # Create plot
                fig, ax = plt.subplots(figsize=(10, 10))

                x = np.linspace(-10, 10, 100)

                # Plot first equation
                if b1 != 0:
                    y1 = (c1 - a1*x) / b1
                    ax.plot(x, y1, 'b-', linewidth=2, label=f'{a1}x + {b1}y = {c1}')
                else:
                    x_val = c1 / a1 if a1 != 0 else 0
                    ax.axvline(x=x_val, color='b', linewidth=2, label=f'{a1}x = {c1}')

                # Plot second equation
                if b2 != 0:
                    y2 = (c2 - a2*x) / b2
                    ax.plot(x, y2, 'r-', linewidth=2, label=f'{a2}x + {b2}y = {c2}')
                else:
                    x_val = c2 / a2 if a2 != 0 else 0
                    ax.axvline(x=x_val, color='r', linewidth=2, label=f'{a2}x = {c2}')

                # Solve for intersection using Cramer's rule
                det = a1*b2 - a2*b1

                if abs(det) > 1e-10:  # Lines intersect at one point
                    x_sol = (c1*b2 - c2*b1) / det
                    y_sol = (a1*c2 - a2*c1) / det
                    ax.plot(x_sol, y_sol, 'go', markersize=12, label=f'Solution ({x_sol:.2f}, {y_sol:.2f})')
                    print(f"\nSolution: x = {x_sol:.4f}, y = {y_sol:.4f}")
                elif abs(a1*b2 - a2*b1) < 1e-10 and abs(a1*c2 - a2*c1) < 1e-10:
                    print("\nInfinite solutions (same line)")
                else:
                    print("\nNo solution (parallel lines)")

                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                ax.grid(True, alpha=0.3)
                ax.set_xlim(-10, 10)
                ax.set_ylim(-10, 10)
                ax.set_aspect('equal')
                ax.legend(fontsize=10)
                ax.set_title('System of Linear Equations', fontsize=14)
                ax.set_xlabel('x')
                ax.set_ylabel('y')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_2d_transformation(self):
        """Interactive 2D linear transformation"""
        while True:
            print("\n" + "=" * 50)
            print("2D Linear Transformation")
            print("Matrix: [[a, b], [c, d]]")
            print("=" * 50)

            try:
                print("\nEnter transformation matrix:")
                a = float(input("  a (top-left): "))
                b = float(input("  b (top-right): "))
                c = float(input("  c (bottom-left): "))
                d = float(input("  d (bottom-right): "))

                transform = np.array([[a, b], [c, d]])

                # Original vectors (basis vectors and a sample vector)
                vectors = np.array([[1, 0], [0, 1], [1, 1]])
                transformed = vectors @ transform.T

                # Create plot
                fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

                colors = ['r', 'g', 'b']
                labels = ['i (1,0)', 'j (0,1)', '(1,1)']

                # Original vectors
                for i, v in enumerate(vectors):
                    ax1.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
                              color=colors[i], width=0.008, label=labels[i])

                ax1.set_xlim(-3, 3)
                ax1.set_ylim(-3, 3)
                ax1.set_aspect('equal')
                ax1.grid(True, alpha=0.3)
                ax1.legend()
                ax1.set_title('Original Vectors')
                ax1.set_xlabel('x')
                ax1.set_ylabel('y')

                # Transformed vectors
                for i, v in enumerate(transformed):
                    ax2.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1,
                              color=colors[i], width=0.008,
                              label=f"({v[0]:.2f}, {v[1]:.2f})")

                max_val = max(np.max(np.abs(transformed)) + 1, 3)
                ax2.set_xlim(-max_val, max_val)
                ax2.set_ylim(-max_val, max_val)
                ax2.set_aspect('equal')
                ax2.grid(True, alpha=0.3)
                ax2.legend()
                ax2.set_title(f'After Transformation\n[[{a}, {b}], [{c}, {d}]]')
                ax2.set_xlabel('x')
                ax2.set_ylabel('y')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

                # Calculate determinant
                det = a*d - b*c
                print(f"\nDeterminant: {det:.4f}")
                print(f"Area scaling factor: {abs(det):.4f}")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_3d_vectors(self):
        """Interactive 3D vector visualization"""
        while True:
            print("\n" + "=" * 50)
            print("3D Vector Visualization")
            print("=" * 50)

            try:
                print("\nEnter first vector (v1):")
                v1_x = float(input("  x component: "))
                v1_y = float(input("  y component: "))
                v1_z = float(input("  z component: "))

                print("\nEnter second vector (v2):")
                v2_x = float(input("  x component: "))
                v2_y = float(input("  y component: "))
                v2_z = float(input("  z component: "))

                v1 = np.array([v1_x, v1_y, v1_z])
                v2 = np.array([v2_x, v2_y, v2_z])
                v_sum = v1 + v2
                v_cross = np.cross(v1, v2)

                # Create plot
                fig = plt.figure(figsize=(14, 6))

                # Vector addition
                ax1 = fig.add_subplot(121, projection='3d')

                ax1.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r',
                          arrow_length_ratio=0.1, linewidth=2, label=f'v1 = ({v1[0]}, {v1[1]}, {v1[2]})')
                ax1.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b',
                          arrow_length_ratio=0.1, linewidth=2, label=f'v2 = ({v2[0]}, {v2[1]}, {v2[2]})')
                ax1.quiver(0, 0, 0, v_sum[0], v_sum[1], v_sum[2], color='g',
                          arrow_length_ratio=0.1, linewidth=2,
                          label=f'v1+v2 = ({v_sum[0]:.1f}, {v_sum[1]:.1f}, {v_sum[2]:.1f})')

                max_val = max(np.max(np.abs(v_sum)) + 1, 2)
                ax1.set_xlim([0, max_val])
                ax1.set_ylim([0, max_val])
                ax1.set_zlim([0, max_val])
                ax1.set_xlabel('X')
                ax1.set_ylabel('Y')
                ax1.set_zlabel('Z')
                ax1.legend()
                ax1.set_title('Vector Addition')

                # Cross product
                ax2 = fig.add_subplot(122, projection='3d')

                ax2.quiver(0, 0, 0, v1[0], v1[1], v1[2], color='r',
                          arrow_length_ratio=0.1, linewidth=2, label='v1')
                ax2.quiver(0, 0, 0, v2[0], v2[1], v2[2], color='b',
                          arrow_length_ratio=0.1, linewidth=2, label='v2')
                ax2.quiver(0, 0, 0, v_cross[0], v_cross[1], v_cross[2], color='purple',
                          arrow_length_ratio=0.1, linewidth=3,
                          label=f'v1×v2 = ({v_cross[0]:.1f}, {v_cross[1]:.1f}, {v_cross[2]:.1f})')

                max_val = max(np.max(np.abs(np.concatenate([v1, v2, v_cross]))) + 1, 2)
                ax2.set_xlim([-max_val, max_val])
                ax2.set_ylim([-max_val, max_val])
                ax2.set_zlim([-max_val, max_val])
                ax2.set_xlabel('X')
                ax2.set_ylabel('Y')
                ax2.set_zlabel('Z')
                ax2.legend()
                ax2.set_title('Cross Product (perpendicular)')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

                # Print dot product
                dot_product = np.dot(v1, v2)
                print(f"\nDot product: {dot_product:.4f}")
                print(f"Cross product magnitude: {np.linalg.norm(v_cross):.4f}")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_3d_plane(self):
        """Interactive 3D plane visualization"""
        while True:
            print("\n" + "=" * 50)
            print("3D Plane: ax + by + cz = d")
            print("=" * 50)

            try:
                a = float(input("Enter coefficient a: "))
                b = float(input("Enter coefficient b: "))
                c = float(input("Enter coefficient c: "))
                d = float(input("Enter constant d: "))

                if a == 0 and b == 0 and c == 0:
                    print("Error: All coefficients cannot be zero.")
                    continue

                # Create plot
                fig = plt.figure(figsize=(10, 8))
                ax = fig.add_subplot(111, projection='3d')

                # Create meshgrid
                x = np.linspace(-10, 10, 20)
                y = np.linspace(-10, 10, 20)
                X, Y = np.meshgrid(x, y)

                # Calculate Z based on the equation
                if c != 0:
                    Z = (d - a*X - b*Y) / c
                elif b != 0:
                    # Plane parallel to z-axis
                    Z = np.outer(np.ones(20), np.linspace(-10, 10, 20))
                    Y = (d - a*X) / b * np.ones_like(Z)
                else:
                    # Plane parallel to y and z axes
                    X = (d / a) * np.ones_like(X)

                ax.plot_surface(X, Y, Z, alpha=0.6, cmap='viridis')

                # Normal vector
                normal = np.array([a, b, c])
                # Find a point on the plane
                if c != 0:
                    point = np.array([0, 0, d/c])
                elif b != 0:
                    point = np.array([0, d/b, 0])
                else:
                    point = np.array([d/a, 0, 0])

                # Scale normal for visualization
                normal_scaled = normal / np.linalg.norm(normal) * 3

                ax.quiver(point[0], point[1], point[2],
                         normal_scaled[0], normal_scaled[1], normal_scaled[2],
                         color='r', arrow_length_ratio=0.2, linewidth=3, label='Normal vector')

                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                ax.set_title(f'Plane: {a}x + {b}y + {c}z = {d}')
                ax.legend()

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

                print(f"\nNormal vector: ({a}, {b}, {c})")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_3d_system(self):
        """Interactive system of 3D planes"""
        while True:
            print("\n" + "=" * 50)
            print("System of Planes in 3D")
            print("Plane 1: a1*x + b1*y + c1*z = d1")
            print("Plane 2: a2*x + b2*y + c2*z = d2")
            print("=" * 50)

            try:
                print("\nPlane 1:")
                a1 = float(input("  a1: "))
                b1 = float(input("  b1: "))
                c1 = float(input("  c1: "))
                d1 = float(input("  d1: "))

                print("\nPlane 2:")
                a2 = float(input("  a2: "))
                b2 = float(input("  b2: "))
                c2 = float(input("  c2: "))
                d2 = float(input("  d2: "))

                # Create plot
                fig = plt.figure(figsize=(12, 10))
                ax = fig.add_subplot(111, projection='3d')

                # Create meshgrid
                x = np.linspace(-10, 10, 20)
                y = np.linspace(-10, 10, 20)
                X, Y = np.meshgrid(x, y)

                # Calculate Z for both planes
                if c1 != 0:
                    Z1 = (d1 - a1*X - b1*Y) / c1
                    ax.plot_surface(X, Y, Z1, alpha=0.4, color='blue')

                if c2 != 0:
                    Z2 = (d2 - a2*X - b2*Y) / c2
                    ax.plot_surface(X, Y, Z2, alpha=0.4, color='red')

                ax.set_xlabel('X')
                ax.set_ylabel('Y')
                ax.set_zlabel('Z')
                ax.set_title(f'Plane 1: {a1}x+{b1}y+{c1}z={d1}\nPlane 2: {a2}x+{b2}y+{c2}z={d2}')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def visualize_3d_transformation(self):
        """Interactive 3D linear transformation"""
        while True:
            print("\n" + "=" * 50)
            print("3D Linear Transformation (3x3 Matrix)")
            print("=" * 50)

            try:
                print("\nEnter transformation matrix (row by row):")
                print("Row 1:")
                a11 = float(input("  a11: "))
                a12 = float(input("  a12: "))
                a13 = float(input("  a13: "))

                print("Row 2:")
                a21 = float(input("  a21: "))
                a22 = float(input("  a22: "))
                a23 = float(input("  a23: "))

                print("Row 3:")
                a31 = float(input("  a31: "))
                a32 = float(input("  a32: "))
                a33 = float(input("  a33: "))

                transform = np.array([[a11, a12, a13],
                                     [a21, a22, a23],
                                     [a31, a32, a33]])

                # Original basis vectors
                vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
                transformed = vectors @ transform.T

                # Create plot
                fig = plt.figure(figsize=(14, 6))

                colors = ['r', 'g', 'b']
                labels = ['i', 'j', 'k']

                # Original vectors
                ax1 = fig.add_subplot(121, projection='3d')
                for i, v in enumerate(vectors):
                    ax1.quiver(0, 0, 0, v[0], v[1], v[2], color=colors[i],
                              arrow_length_ratio=0.15, linewidth=2, label=labels[i])

                ax1.set_xlim([0, 2])
                ax1.set_ylim([0, 2])
                ax1.set_zlim([0, 2])
                ax1.set_xlabel('X')
                ax1.set_ylabel('Y')
                ax1.set_zlabel('Z')
                ax1.legend()
                ax1.set_title('Original Basis Vectors')

                # Transformed vectors
                ax2 = fig.add_subplot(122, projection='3d')
                for i, v in enumerate(transformed):
                    ax2.quiver(0, 0, 0, v[0], v[1], v[2], color=colors[i],
                              arrow_length_ratio=0.15, linewidth=2,
                              label=f"{labels[i]}' = ({v[0]:.2f}, {v[1]:.2f}, {v[2]:.2f})")

                max_val = max(np.max(np.abs(transformed)) + 1, 2)
                ax2.set_xlim([0, max_val])
                ax2.set_ylim([0, max_val])
                ax2.set_zlim([0, max_val])
                ax2.set_xlabel('X')
                ax2.set_ylabel('Y')
                ax2.set_zlabel('Z')
                ax2.legend()
                ax2.set_title('Transformed Vectors')

                plt.tight_layout()
                plt.show(block=False)
                plt.pause(0.1)

                # Calculate determinant
                det = np.linalg.det(transform)
                print(f"\nDeterminant: {det:.4f}")
                print(f"Volume scaling factor: {abs(det):.4f}")

            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            choice = input("\nOptions:\n1. Modify values\n2. Save image\n0. Back to menu\nChoice: ").strip()
            if choice == '2':
                filename = input("Enter filename (without extension): ").strip()
                plt.savefig(f"{filename}.png", dpi=300, bbox_inches='tight')
                print(f"Saved as {filename}.png")
            elif choice != '1':
                plt.close()
                break
            plt.close()

    def run(self):
        """Main run loop"""
        print("\n" + "=" * 50)
        print("Interactive Linear Algebra Visualizer")
        print("=" * 50)

        while True:
            dimension = self.get_dimension_choice()

            if dimension is None:
                print("\nThank you for using the visualizer!")
                break

            viz_type = self.get_visualization_type(dimension)

            if viz_type == '0':
                continue

            if dimension == 2:
                if viz_type == '1':
                    self.visualize_2d_vectors()
                elif viz_type == '2':
                    self.visualize_2d_linear_equation()
                elif viz_type == '3':
                    self.visualize_2d_system()
                elif viz_type == '4':
                    self.visualize_2d_transformation()
            else:  # 3D
                if viz_type == '1':
                    self.visualize_3d_vectors()
                elif viz_type == '2':
                    self.visualize_3d_plane()
                elif viz_type == '3':
                    self.visualize_3d_system()
                elif viz_type == '4':
                    self.visualize_3d_transformation()


if __name__ == '__main__':
    visualizer = LinearAlgebraVisualizer()
    visualizer.run()
