#!/usr/bin/env python3
import sys
import argparse
def main():
    parser.add_argument('--command', required=True, help="Command to run")
    args = parser.parse_args()
    output =args.command
    print(output)
    
if __name__ == "__main__":
    main()
