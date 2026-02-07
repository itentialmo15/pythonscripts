#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python echo.py <text>")
        sys.exit(1)

    text = " ".join(sys.argv[1:])
    print(text)

