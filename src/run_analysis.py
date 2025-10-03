#!/usr/bin/env python3
"""
Script to run rainfall analysis for different years.
Usage: python run_analysis.py [YEAR]
Example: python run_analysis.py 2025
"""

import sys
import os
from . import main

def run_for_year(year):
    """Run analysis for a specific year."""
    print(f"🌧️ Running rainfall analysis for {year}...")
    
    # Update the year in main.py by modifying the global variable
    from . import main
    main.YEAR = year
    main.BASE_CSV = f"Rainfall_Garden_{year}.csv"
    main.HOLIDAYS_CSV = f"holidays_{year}.csv"
    
    # Run the analysis
    main.main()
    
    print(f"✅ Analysis complete! Check output/{year}/ for results.")

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
