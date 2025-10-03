#!/usr/bin/env python3
"""
Entry point for Boston Rainfall Analysis.
This script runs the analysis from the project root directory.
"""

import sys
import os

# Import and run the analysis
from src.run_analysis import run_for_year

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            year = int(sys.argv[1])
            run_for_year(year)
        except ValueError:
            print("❌ Error: Year must be a number (e.g., 2025)")
            sys.exit(1)
    else:
        # Default to 2025
        run_for_year(2025)
