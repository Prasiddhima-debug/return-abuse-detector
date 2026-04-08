import gradio as gr
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from tasks.easy import get_easy_task

def run_simulation():
    customers = get_easy_task()
    result = ""
    for c in customers:
        result += str(c) + "\n"
    return result

gr.Interface(
    fn=run_simulation,
    inputs=None,
    outputs="text",
    title="Return Abuse Detector",
    description="RL environment simulating e-commerce return abuse detection"
).launch()