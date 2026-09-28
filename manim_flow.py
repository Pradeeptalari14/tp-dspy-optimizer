"""
3Blue1Brown Manim Animation: DSPy MIPROv2 Bayesian Prompt Search
Visualizes convergence curve over instruction candidate space.
"""
from manim import *

class DSPyOptimizerFlow(Scene):
    def construct(self):
        title = Text("DSPy MIPROv2: Algorithmic Prompt Optimizer", font_size=30, color=PURPLE)
        subtitle = Text("Replacing Manual Prompt Crafting with Bayesian Compilation", font_size=18, color=LIGHT_GRAY)
        title_group = VGroup(title, subtitle).arrange(DOWN, buff=0.2).to_edge(UP)
        self.play(Write(title_group))
        self.wait(1)

        sig = Text("Signature: (Telemetry) -> (RootCause, Action)", font_size=20, color=YELLOW).shift(UP * 0.5)
        curve = Text("MIPROv2 Search: +19.4% Task Accuracy", font_size=22, color=GREEN).shift(DOWN * 0.5)

        self.play(FadeIn(sig), FadeIn(curve))
        self.wait(2)
