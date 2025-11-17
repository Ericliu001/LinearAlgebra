"""
Interactive Matrix Visualization Script
Provides a single-window UI to visualize 2x2 or 3x3 matrices.
- 2x2: shows how a matrix transforms the unit square and basis vectors.
- 3x3: shows how a matrix transforms a cube and basis vectors in 3D.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401, needed for 3D projection
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.widgets import TextBox, Button
import sys


class MatrixVisualizer:
    def __init__(self):
        # Maintain a single figure window for the entire flow
        self.fig = plt.figure(figsize=(12, 9))
        self._widgets = []
        self.fig.canvas.mpl_connect('close_event', self.on_window_close)

    def on_window_close(self, _event):
        """Exit when the single window is closed."""
        print("\nWindow closed. Exiting program...")
        plt.close('all')
        sys.exit(0)

    # ---------- 2x2 visualization ----------
    def visualize_2x2(self):
        print("\n2x2 Matrix - Visualize transformation of the unit square")
        self.fig.clf()
        self.fig.set_size_inches(12, 9, forward=True)
        ax = self.fig.add_subplot(111)
        self.fig.subplots_adjust(left=0.08, right=0.70, bottom=0.1, top=0.92)

        # Default matrix values
        a11, a12, a21, a22 = 1.0, 0.5, -0.2, 1.2

        def update():
            """Redraw the 2D plot with the latest matrix entries."""
            try:
                m = np.array([
                    [float(tb_a11.text), float(tb_a12.text)],
                    [float(tb_a21.text), float(tb_a22.text)],
                ])
            except ValueError:
                return  # Wait until entries are valid numbers

            ax.clear()

            # Grid and axes
            ax.axhline(0, color='k', linewidth=0.8, alpha=0.4)
            ax.axvline(0, color='k', linewidth=0.8, alpha=0.4)
            ax.grid(True, linestyle='--', alpha=0.3)

            # Transformed basis vectors only
            ax.arrow(0, 0, m[0, 0], m[1, 0], head_width=0.07, length_includes_head=True,
                     color='red', alpha=0.8, label='Transformed e1')
            ax.arrow(0, 0, m[0, 1], m[1, 1], head_width=0.07, length_includes_head=True,
                     color='orange', alpha=0.8, label='Transformed e2')

            # Auto scale around basis vectors
            basis_points = np.array([
                [0, 0],
                [1, 0],
                [0, 1],
                m[:, 0],
                m[:, 1],
            ])
            max_extent = np.max(np.abs(basis_points)) + 0.5
            if max_extent < 2:
                max_extent = 2
            ax.set_xlim([-max_extent, max_extent])
            ax.set_ylim([-max_extent, max_extent])
            ax.set_aspect('equal', adjustable='box')
            ax.set_title('2x2 Matrix Transformation', fontsize=16, fontweight='bold', pad=15)
            ax.legend(loc='upper left', fontsize=10)
            ax.set_xlabel('x')
            ax.set_ylabel('y')

            self.fig.canvas.draw_idle()

        # Controls on the right
        box_w = 0.10
        box_h = 0.05
        x0 = 0.75
        y_top = 0.80
        gap = 0.07

        tb_a11 = TextBox(self.fig.add_axes([x0, y_top, box_w, box_h]), 'a11', initial=f'{a11:.2f}')
        tb_a12 = TextBox(self.fig.add_axes([x0 + box_w + 0.02, y_top, box_w, box_h]), 'a12',
                         initial=f'{a12:.2f}')
        tb_a21 = TextBox(self.fig.add_axes([x0, y_top - gap, box_w, box_h]), 'a21',
                         initial=f'{a21:.2f}')
        tb_a22 = TextBox(self.fig.add_axes([x0 + box_w + 0.02, y_top - gap, box_w, box_h]), 'a22',
                         initial=f'{a22:.2f}')

        for tb in (tb_a11, tb_a12, tb_a21, tb_a22):
            tb.on_submit(lambda _text: update())

        self.fig.text(x0 + box_w, y_top + 0.09, 'Matrix entries\n(press Enter to update)',
                      ha='center', fontsize=11, fontweight='bold')

        # Return button
        ax_menu = self.fig.add_axes([x0, 0.25, box_w * 2 + 0.02, 0.07])
        btn_menu = Button(ax_menu, 'Return to Menu', color='lightblue')
        btn_menu.on_clicked(lambda _event: self.show_main_menu())

        self._widgets = [tb_a11, tb_a12, tb_a21, tb_a22, btn_menu]
        update()

    # ---------- 3x3 visualization ----------
    def visualize_3x3(self):
        print("\n3x3 Matrix - Visualize transformation of a 3D cube")
        self.fig.clf()
        self.fig.set_size_inches(13, 9, forward=True)
        ax = self.fig.add_subplot(111, projection='3d')
        self.fig.subplots_adjust(left=0.05, right=0.70, bottom=0.08, top=0.92)

        # Default matrix
        m_init = np.array([[1.0, 0.3, 0.0],
                           [0.0, 1.0, -0.2],
                           [0.2, 0.2, 1.0]])

        def update():
            """Redraw the 3D plot with the latest matrix entries."""
            try:
                m = np.array([
                    [float(tb_11.text), float(tb_12.text), float(tb_13.text)],
                    [float(tb_21.text), float(tb_22.text), float(tb_23.text)],
                    [float(tb_31.text), float(tb_32.text), float(tb_33.text)],
                ])
            except ValueError:
                return

            ax.clear()

            def add_plane(corners, color, label=None, alpha=0.15, linestyle='-'):
                """Add a quadrilateral plane to the 3D axis."""
                poly = Poly3DCollection([corners],
                                        alpha=alpha,
                                        facecolors=color,
                                        edgecolors=color,
                                        linewidths=1.0,
                                        linestyles=linestyle)
                poly.set_label(label if label else None)
                ax.add_collection3d(poly)

            # Coordinate planes (original + transformed)
            plane_defs = {
                'XY plane': (np.array([
                    [-1, -1, 0],
                    [1, -1, 0],
                    [1, 1, 0],
                    [-1, 1, 0],
                ]), 'lightskyblue'),
                'XZ plane': (np.array([
                    [-1, 0, -1],
                    [1, 0, -1],
                    [1, 0, 1],
                    [-1, 0, 1],
                ]), 'lightgreen'),
                'YZ plane': (np.array([
                    [0, -1, -1],
                    [0, 1, -1],
                    [0, 1, 1],
                    [0, -1, 1],
                ]), 'lightcoral'),
            }

            plane_points = []
            for label, (corners, color) in plane_defs.items():
                # Original plane (lighter, no label to avoid legend noise)
                add_plane(corners, color=color, label=None, alpha=0.08, linestyle=':')
                # Transformed plane with label
                transformed_plane = corners @ m.T
                add_plane(transformed_plane, color=color, label=label, alpha=0.25, linestyle='-')
                plane_points.append(corners)
                plane_points.append(transformed_plane)

            # Basis vectors
            origin = np.zeros(3)
            ax.quiver(*origin, *m[:, 0], color='red', linewidth=2, arrow_length_ratio=0.08,
                      label='Transformed e1')
            ax.quiver(*origin, *m[:, 1], color='orange', linewidth=2, arrow_length_ratio=0.08,
                      label='Transformed e2')
            ax.quiver(*origin, *m[:, 2], color='green', linewidth=2, arrow_length_ratio=0.08,
                      label='Transformed e3')

            # Axis limits
            axis_refs = [*plane_points, origin, m.T]
            all_points = np.vstack(axis_refs)
            span = np.max(np.abs(all_points)) + 0.5
            if span < 2:
                span = 2
            ax.set_xlim([-span, span])
            ax.set_ylim([-span, span])
            ax.set_zlim([-span, span])

            ax.set_title('3x3 Matrix Transformation', fontsize=16, fontweight='bold', pad=18)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.legend(loc='upper left', fontsize=9)
            ax.view_init(elev=25, azim=35)

            self.fig.canvas.draw_idle()

        # Controls on the right (3x3 grid of text boxes)
        box_w = 0.10
        box_h = 0.05
        x0 = 0.72
        y0 = 0.78
        gap_x = box_w + 0.02
        gap_y = 0.07

        tb_11 = TextBox(self.fig.add_axes([x0, y0, box_w, box_h]), 'a11', initial=f'{m_init[0,0]:.2f}')
        tb_12 = TextBox(self.fig.add_axes([x0 + gap_x, y0, box_w, box_h]), 'a12',
                        initial=f'{m_init[0,1]:.2f}')
        tb_13 = TextBox(self.fig.add_axes([x0 + 2*gap_x, y0, box_w, box_h]), 'a13',
                        initial=f'{m_init[0,2]:.2f}')

        tb_21 = TextBox(self.fig.add_axes([x0, y0 - gap_y, box_w, box_h]), 'a21',
                        initial=f'{m_init[1,0]:.2f}')
        tb_22 = TextBox(self.fig.add_axes([x0 + gap_x, y0 - gap_y, box_w, box_h]), 'a22',
                        initial=f'{m_init[1,1]:.2f}')
        tb_23 = TextBox(self.fig.add_axes([x0 + 2*gap_x, y0 - gap_y, box_w, box_h]), 'a23',
                        initial=f'{m_init[1,2]:.2f}')

        tb_31 = TextBox(self.fig.add_axes([x0, y0 - 2*gap_y, box_w, box_h]), 'a31',
                        initial=f'{m_init[2,0]:.2f}')
        tb_32 = TextBox(self.fig.add_axes([x0 + gap_x, y0 - 2*gap_y, box_w, box_h]), 'a32',
                        initial=f'{m_init[2,1]:.2f}')
        tb_33 = TextBox(self.fig.add_axes([x0 + 2*gap_x, y0 - 2*gap_y, box_w, box_h]), 'a33',
                        initial=f'{m_init[2,2]:.2f}')

        for tb in (tb_11, tb_12, tb_13, tb_21, tb_22, tb_23, tb_31, tb_32, tb_33):
            tb.on_submit(lambda _text: update())

        self.fig.text(x0 + box_w * 1.5 + 0.02, y0 + 0.08, 'Matrix entries\n(press Enter to update)',
                      ha='center', fontsize=11, fontweight='bold')

        ax_menu = self.fig.add_axes([x0, 0.20, box_w * 3 + 0.04, 0.07])
        btn_menu = Button(ax_menu, 'Return to Menu', color='lightblue')
        btn_menu.on_clicked(lambda _event: self.show_main_menu())

        self._widgets = [
            tb_11, tb_12, tb_13,
            tb_21, tb_22, tb_23,
            tb_31, tb_32, tb_33,
            btn_menu,
        ]
        update()

    # ---------- Menu ----------
    def show_main_menu(self):
        """Display main menu in the single window."""
        self.fig.clf()
        self.fig.set_size_inches(10, 7, forward=True)
        self.fig.suptitle('Interactive Matrix Visualizer',
                          fontsize=20, fontweight='bold')

        ax = self.fig.add_subplot(111)
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')

        ax.text(5, 8, 'Choose Matrix Size:',
                ha='center', fontsize=16, fontweight='bold')
        ax.text(5, 7, 'Select a matrix type to visualize its effect',
                ha='center', fontsize=12, style='italic', alpha=0.7)

        ax_2x2 = self.fig.add_axes([0.15, 0.45, 0.3, 0.15])
        btn_2x2 = Button(ax_2x2, '2x2 Matrix\n(2D transform)', color='lightblue')

        ax_3x3 = self.fig.add_axes([0.55, 0.45, 0.3, 0.15])
        btn_3x3 = Button(ax_3x3, '3x3 Matrix\n(3D transform)', color='lightgreen')

        ax_exit = self.fig.add_axes([0.35, 0.20, 0.3, 0.1])
        btn_exit = Button(ax_exit, 'Exit Program', color='lightcoral')

        self._widgets = [btn_2x2, btn_3x3, btn_exit]

        btn_2x2.on_clicked(lambda _event: self.visualize_2x2())
        btn_3x3.on_clicked(lambda _event: self.visualize_3x3())
        btn_exit.on_clicked(lambda _event: self.on_window_close(None))

        ax.text(5, 1.2, 'Adjust matrix entries in the next screen to see the change in real time.',
                ha='center', fontsize=10, style='italic', alpha=0.8)
        self.fig.canvas.draw_idle()

    def run(self):
        print("\n" + "=" * 60)
        print("Interactive Matrix Visualizer")
        print("Choose between 2x2 (2D) or 3x3 (3D) matrix transformations")
        print("=" * 60)
        self.show_main_menu()
        plt.show()


if __name__ == '__main__':
    MatrixVisualizer().run()
