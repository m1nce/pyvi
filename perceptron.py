from manim import *

class PerceptronNeuralNetworkDemo(Scene):
    def construct(self):
        input_layer = [Circle(radius=0.3, color=BLUE) for _ in range(2)]
        hidden_layer = [Circle(radius=0.3, color=GREEN) for _ in range(3)]
        output_layer = [Circle(radius=0.3, color=RED) for _ in range(1)]

        input_positions = [UP * i for i in range(-1, 2)]
        hidden_positions = [RIGHT * 2 + UP * i for i in range(-2, 3, 2)]
        output_positions = [RIGHT * 4]

        input_layer_group = VGroup(*[circle.move_to(pos) for circle, pos in zip(input_layer, input_positions)])
        hidden_layer_group = VGroup(*[circle.move_to(pos) for circle, pos in zip(hidden_layer, hidden_positions)])
        output_layer_group = VGroup(*[circle.move_to(pos) for circle, pos in zip(output_layer, output_positions)])

        self.play(Create(input_layer_group), Create(hidden_layer_group), Create(output_layer_group))

        edges = VGroup()
        for input_neuron in input_layer:
            for hidden_neuron in hidden_layer:
                edges.add(Line(input_neuron.get_center(), hidden_neuron.get_center(), color=WHITE))
        for hidden_neuron in hidden_layer:
            for output_neuron in output_layer:
                edges.add(Line(hidden_neuron.get_center(), output_neuron.get_center(), color=WHITE))

        self.play(Create(edges))

        input_labels = VGroup(*[Text(f"x{i+1}", font_size=24).next_to(neuron, LEFT) for i, neuron in enumerate(input_layer)])
        hidden_labels = VGroup(*[Text(f"h{i+1}", font_size=24).next_to(neuron, UP) for i, neuron in enumerate(hidden_layer)])
        output_labels = VGroup(Text("y", font_size=24).next_to(output_layer[0], RIGHT))

        self.play(Write(input_labels), Write(hidden_labels), Write(output_labels))

        weights_text = Text("Weights: W", font_size=24).to_corner(UL)
        self.play(Write(weights_text))

        def forward_propagation():
            for input_neuron in input_layer:
                for hidden_neuron in hidden_layer:
                    edge = Line(input_neuron.get_center(), hidden_neuron.get_center(), color=YELLOW)
                    self.play(Create(edge), run_time=0.2)

            for hidden_neuron in hidden_layer:
                for output_neuron in output_layer:
                    edge = Line(hidden_neuron.get_center(), output_neuron.get_center(), color=YELLOW)
                    self.play(Create(edge), run_time=0.2)

        forward_propagation()

        def activate_layer(layer_group, layer_name):
            activations = VGroup()
            activation_text = Text(f"{layer_name} activated", font_size=24).to_edge(DOWN)
            self.play(Write(activation_text))
            for neuron in layer_group:
                activation = Circle(radius=0.35, color=YELLOW).move_to(neuron.get_center())
                activations.add(activation)
                self.play(Create(activation), run_time=0.3)
                self.play(FadeOut(activation), run_time=0.3)
            self.play(FadeOut(activation_text))

        activate_layer(input_layer, "Input Layer")
        activate_layer(hidden_layer, "Hidden Layer")
        activate_layer(output_layer, "Output Layer")

        final_text = Text("Forward Propagation Complete", font_size=36).to_edge(UP)
        self.play(Write(final_text))
        self.wait(2)
