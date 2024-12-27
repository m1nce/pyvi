from manim import *
import numpy as np

class GradientDescentWithTangent(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1], 
            y_range=[-1, 9, 1], 
            axis_config={"include_numbers": True},
        )
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        def func(x):
            return x**2 
        graph = axes.plot(func, color=BLUE)
        graph_label = axes.get_graph_label(graph, label="f(x) = x^2")
        
        learning_rate = 0.5
        initial_x = 2.5
        num_steps = 10

        self.add(axes, labels, graph, graph_label)
        
        x_tracker = ValueTracker(initial_x)
        dot = Dot(axes.c2p(initial_x, func(initial_x)), color=RED)
        dot.add_updater(lambda d: d.move_to(axes.c2p(x_tracker.get_value(), func(x_tracker.get_value()))))
        
        tangent_line = always_redraw(
            lambda: self.get_tangent_line(axes, func, x_tracker.get_value(), length=4, color=YELLOW)
        )
        
        self.add(dot, tangent_line)

        current_x = initial_x
        for _ in range(num_steps):
            grad = 2 * current_x
            delta_x = learning_rate * grad
            next_x = current_x - delta_x
            
            self.play(x_tracker.animate.set_value(next_x), run_time=8)

            current_x = next_x

        self.wait(2)

    def get_tangent_line(self, axes, func, x, length=4, color=YELLOW):
        """
        Returns a Line object representing the tangent line at a given x-coordinate.
        """
        y = func(x)
        grad = 2 * x  # Gradient for f(x) = x^2
        dx = length / 2
        p1 = axes.c2p(x - dx, y - grad * dx)
        p2 = axes.c2p(x + dx, y + grad * dx)
        return Line(p1, p2, color=color)
