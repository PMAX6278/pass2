# pass2.py - Launcher for compiled module
import sys

try:
    import phyo_bypass as bypass
except ImportError as e:
    print(f"Error: Could not load module - {e}")
    print("Make sure phyo_bypass.so is in the same directory")
    sys.exit(1)

if __name__ == "__main__":
    bypass.start()
