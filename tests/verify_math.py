import sys
import os

# Adjust path to include the project root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
sys.path.insert(0, project_root)

try:
    from src.utils.math_ops import factorial
except ImportError:
    # Fallback if src is not a package (though with sys.path hack it should work as namespace package)
    # Or maybe user runs it from root?
    sys.path.insert(0, os.path.join(project_root, 'src'))
    from utils.math_ops import factorial

if __name__ == "__main__":
    n = 5
    print(f"Calculating factorial of {n}...")
    result = factorial(n)
    print(f"Factorial of {n} is: {result}")
