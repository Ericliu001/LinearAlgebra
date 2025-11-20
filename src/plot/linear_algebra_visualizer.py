"""
Interactive Linear Algebra Visualization Script
Allows users to choose 2D or 3D equations and adjust constants using text boxes
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets import TextBox, Button
import sys


class LinearAlgebraVisualizer:
    def __init__(self):
        # Use a single figure window for the entire app
        self.fig = plt.figure(figsize=(12, 9))
        self._widgets = []  # keep references to widgets to avoid GC
        self.fig.canvas.mpl_connect('close_event', self.on_window_close)

    def on_window_close(self, _event):
        """Exit when the single window is closed."""
        print("\nWindow closed. Exiting program...")
        plt.close('all')
        sys.exit(0)

    def visualize_2d_equation(self):
        """Interactive 2D linear equation with text box controls"""
        print("\n2D Linear Equation - Use text boxes to adjust coefficients")
        print("Equation form: ax + by = c")

        # Initial values
        a_init, b_init, c_init = 2.0, 3.0, 6.0

        # Prepare figure
        self.fig.clf()
        self.fig.set_size_inches(12, 9, forward=True)
        ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.1, right=0.75, bottom=0.15, top=0.92)

        def update():
            """Update the plot based on text box values"""
            try:
                a = float(textbox_a.text)
                b = float(textbox_b.text)
                c = float(textbox_c.text)
            except ValueError:
                return  # Skip update if values are invalid

            ax.clear()

            x = np.linspace(-10, 10, 200)

            # Plot the line
            if abs(b) > 0.001:
                y = (c - a*x) / b
                ax.plot(x, y, 'b-', linewidth=2.5, label=f'{a:.2f}x + {b:.2f}y = {c:.2f}')
            elif abs(a) > 0.001:
                # Vertical line
                x_val = c / a
                ax.axvline(x=x_val, color='b', linewidth=2.5, label=f'{a:.2f}x = {c:.2f}')
            else:
                # Degenerate case
                ax.text(0, 0, 'Invalid equation (a and b cannot both be 0)',
                       ha='center', va='center', fontsize=14, color='red')

            # Add grid and axes
            ax.axhline(y=0, color='k', linewidth=0.8, alpha=0.3)
            ax.axvline(x=0, color='k', linewidth=0.8, alpha=0.3)
            ax.grid(True, alpha=0.3, linestyle='--')

            ax.set_xlim(-10, 10)
            ax.set_ylim(-10, 10)
            ax.set_aspect('equal')
            ax.legend(fontsize=12, loc='upper left')
            ax.set_title(f'2D Linear Equation: {a:.2f}x + {b:.2f}y = {c:.2f}',
                        fontsize=16, fontweight='bold', pad=20)
            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('y', fontsize=12)

            self.fig.canvas.draw_idle()

        # Create text boxes on the right side
        text_box_width = 0.15
        text_box_height = 0.05
        right_margin = 0.80

        ax_text_a = self.fig.add_axes([right_margin, 0.75, text_box_width, text_box_height])
        ax_text_b = self.fig.add_axes([right_margin, 0.65, text_box_width, text_box_height])
        ax_text_c = self.fig.add_axes([right_margin, 0.55, text_box_width, text_box_height])

        textbox_a = TextBox(ax_text_a, 'a = ', initial=f'{a_init:.2f}',
                           textalignment='center')
        textbox_b = TextBox(ax_text_b, 'b = ', initial=f'{b_init:.2f}',
                           textalignment='center')
        textbox_c = TextBox(ax_text_c, 'c = ', initial=f'{c_init:.2f}',
                           textalignment='center')

        # Connect text boxes to update function
        textbox_a.on_submit(lambda _text: update())
        textbox_b.on_submit(lambda _text: update())
        textbox_c.on_submit(lambda _text: update())

        # Add instructions text
        self.fig.text(right_margin + text_box_width/2, 0.85, 'Adjust Constants:',
                ha='center', fontsize=14, fontweight='bold')
        self.fig.text(right_margin + text_box_width/2, 0.45,
                'Type a value and\npress ENTER to update',
                ha='center', fontsize=10, style='italic', alpha=0.7)

        # Add return to menu button
        ax_menu = self.fig.add_axes([right_margin, 0.25, text_box_width, 0.06])
        btn_menu = Button(ax_menu, 'Return to Menu', color='lightblue')
        btn_menu.on_clicked(lambda _event: self.show_main_menu())

        # Store widgets to prevent garbage collection
        self._widgets = [textbox_a, textbox_b, textbox_c, btn_menu]

        # Initial plot
        update()

    def visualize_3d_equation(self):
        """Interactive 3D plane equation with text box controls"""
        print("\n3D Plane Equation - Use text boxes to adjust coefficients")
        print("Equation form: ax + by + cz = d")

        # Initial values
        a_init, b_init, c_init, d_init = 2.0, 3.0, 1.0, 6.0

        # Prepare figure with 3D subplot
        self.fig.clf()
        self.fig.set_size_inches(14, 9, forward=True)
        ax = self.fig.add_subplot(111, projection='3d')
        self.fig.subplots_adjust(left=0.05, right=0.70, bottom=0.1, top=0.95)

        def update():
            """Update the plot based on text box values"""
            try:
                a = float(textbox_a.text)
                b = float(textbox_b.text)
                c = float(textbox_c.text)
                d = float(textbox_d.text)
            except ValueError:
                return  # Skip update if values are invalid

            # Clear only the 3D axis
            ax.clear()

            # Create meshgrid
            x = np.linspace(-10, 10, 30)
            y = np.linspace(-10, 10, 30)
            X, Y = np.meshgrid(x, y)

            # Calculate Z and plot the plane
            if abs(c) > 0.001:
                Z = (d - a*X - b*Y) / c
                ax.plot_surface(X, Y, Z, alpha=0.7, cmap='viridis',
                              edgecolor='none', antialiased=True)

                # Draw normal vector
                # Find a point on the plane
                if abs(c) > 0.001:
                    point = np.array([0, 0, d/c])
                elif abs(b) > 0.001:
                    point = np.array([0, d/b, 0])
                elif abs(a) > 0.001:
                    point = np.array([d/a, 0, 0])
                else:
                    point = np.array([0, 0, 0])

                # Scale normal vector for visualization
                normal = np.array([a, b, c])
                norm_mag = np.linalg.norm(normal)
                if norm_mag > 0:
                    normal_scaled = normal / norm_mag * 5
                    ax.quiver(point[0], point[1], point[2],
                            normal_scaled[0], normal_scaled[1], normal_scaled[2],
                            color='red', arrow_length_ratio=0.15, linewidth=3,
                            label='Normal Vector')
            else:
                ax.text(0, 0, 0, 'Invalid equation\n(c cannot be 0 for this view)',
                       ha='center', va='center', fontsize=14, color='red')

            ax.set_xlabel('X', fontsize=12, labelpad=10)
            ax.set_ylabel('Y', fontsize=12, labelpad=10)
            ax.set_zlabel('Z', fontsize=12, labelpad=10)
            ax.set_xlim([-10, 10])
            ax.set_ylim([-10, 10])
            ax.set_zlim([-10, 10])
            ax.set_title(f'3D Plane: {a:.2f}x + {b:.2f}y + {c:.2f}z = {d:.2f}',
                        fontsize=16, fontweight='bold', pad=20)
            ax.legend(loc='upper right', fontsize=10)

            self.fig.canvas.draw_idle()

        # Create text boxes on the right side
        text_box_width = 0.15
        text_box_height = 0.05
        right_margin = 0.75

        ax_text_a = self.fig.add_axes([right_margin, 0.75, text_box_width, text_box_height])
        ax_text_b = self.fig.add_axes([right_margin, 0.65, text_box_width, text_box_height])
        ax_text_c = self.fig.add_axes([right_margin, 0.55, text_box_width, text_box_height])
        ax_text_d = self.fig.add_axes([right_margin, 0.45, text_box_width, text_box_height])

        textbox_a = TextBox(ax_text_a, 'a = ', initial=f'{a_init:.2f}',
                           textalignment='center')
        textbox_b = TextBox(ax_text_b, 'b = ', initial=f'{b_init:.2f}',
                           textalignment='center')
        textbox_c = TextBox(ax_text_c, 'c = ', initial=f'{c_init:.2f}',
                           textalignment='center')
        textbox_d = TextBox(ax_text_d, 'd = ', initial=f'{d_init:.2f}',
                           textalignment='center')

        # Connect text boxes to update function
        textbox_a.on_submit(lambda _text: update())
        textbox_b.on_submit(lambda _text: update())
        textbox_c.on_submit(lambda _text: update())
        textbox_d.on_submit(lambda _text: update())

        # Add instructions text
        self.fig.text(right_margin + text_box_width/2, 0.85, 'Adjust Constants:',
                ha='center', fontsize=14, fontweight='bold')
        self.fig.text(right_margin + text_box_width/2, 0.35,
                'Type a value and\npress ENTER to update',
                ha='center', fontsize=10, style='italic', alpha=0.7)

        # Add return to menu button
        ax_menu = self.fig.add_axes([right_margin, 0.20, text_box_width, 0.06])
        btn_menu = Button(ax_menu, 'Return to Menu', color='lightblue')
        btn_menu.on_clicked(lambda _event: self.show_main_menu())

        # Store widgets to prevent garbage collection
        self._widgets = [textbox_a, textbox_b, textbox_c, textbox_d, btn_menu]

        # Initial plot
        update()

    def show_main_menu(self):
        """Display simplified main menu"""
        # Clear and rebuild the single window for the menu
        self.fig.clf()
        self.fig.set_size_inches(10, 7, forward=True)
        self.fig.suptitle('Interactive Linear Algebra Visualizer',
                    fontsize=20, fontweight='bold')

        # Remove axes
        ax = self.fig.add_subplot(111)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        # Add title text
        ax.text(5, 8, 'Choose Number of Variables:',
               ha='center', fontsize=16, fontweight='bold')

        # Add description
        ax.text(5, 7, 'Select how many variables you want to work with',
               ha='center', fontsize=12, style='italic', alpha=0.7)

        # Create 2D button
        ax_2d = self.fig.add_axes([0.15, 0.45, 0.3, 0.15])
        btn_2d = Button(ax_2d, '2 Variables\n(2D Linear Equation)',
                       color='lightblue')

        # Create 3D button
        ax_3d = self.fig.add_axes([0.55, 0.45, 0.3, 0.15])
        btn_3d = Button(ax_3d, '3 Variables\n(3D Plane Equation)',
                       color='lightgreen')

        # Exit button
        ax_exit = self.fig.add_axes([0.35, 0.20, 0.3, 0.1])
        btn_exit = Button(ax_exit, 'Exit Program', color='lightcoral')

        # Store buttons to prevent garbage collection
        self._widgets = [btn_2d, btn_3d, btn_exit]

        # Connect buttons to functions
        def launch_viz(viz_func):
            """Replace menu with the selected visualization"""
            viz_func()

        btn_2d.on_clicked(lambda _event: launch_viz(self.visualize_2d_equation))
        btn_3d.on_clicked(lambda _event: launch_viz(self.visualize_3d_equation))
        btn_exit.on_clicked(lambda _event: self.on_window_close(None))

        # Add instructions
        ax.text(5, 1.2, 'Click a button to start visualizing equations!',
               ha='center', fontsize=11, style='italic')
        ax.text(5, 0.6, 'You can adjust constants using text boxes in the visualization',
               ha='center', fontsize=10, alpha=0.6)

        self.fig.canvas.draw_idle()

    def run(self):
        """Main run loop"""
        print("\n" + "=" * 60)
        print("Interactive Linear Algebra Visualizer")
        print("Choose between 2D (2 variables) or 3D (3 variables)")
        print("=" * 60)

        self.show_main_menu()
        plt.show()


if __name__ == '__main__':
    visualizer = LinearAlgebraVisualizer()
    visualizer.run()
