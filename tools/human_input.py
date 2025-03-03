"""
Human input tools for Hello World Agent
"""

def get_human_input(prompt="Please provide your input:"):
    """Get input from a human user"""
    print(f"\n{prompt}")
    return input("> ")

def validate_human_input(input_text, validation_func=None):
    """Validate human input"""
    if validation_func:
        return validation_func(input_text)
    return True