#!/usr/bin/env python3
"""
gen simulated IOT observations from a bricks schema
"""
import argparse

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='Generate from bricks')
    parser.add_argument('--iterations', type=int, default=3,
                        help='Number of iterations to report')
    parser.add_argument('--interval-dur', type=int, default=1,
                        help='Minutes between iterations and reports')
    parser.add_argument('--hours-ago', type=int, default=12,
                        help='Initial timestamp for each generated observations is HOURS_AGO hours')
    parser.add_argument('--compact-json', action='store_true', help='Generate Compact JSON')
    args = parser.parse_args()


if __name__ == "__main__":
    main()
