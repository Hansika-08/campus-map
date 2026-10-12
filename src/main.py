"""
Main Application & Input Validation

Tie all modules together to run the campus navigator:
1. Get the list of locations and print them.
2. Ask the user for a source and destination.
3. Validate user input (e.g. check if locations exist, source is not destination).
4. Call find_shortest_route() from navigator.
5. Call display_route() to show the result.
"""

import os
import sys

# Ensure src directory is in sys.path when executed directly or from parent directory
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from locations import get_locations
from routes import ROUTES
from navigator import find_shortest_route
from display import display_route


def main():
    print("========================================")
    print("       SVECW CAMPUS NAVIGATOR")
    print("========================================")

    # 1. Get locations from get_locations()
    locations = get_locations()

    # 2. Print available locations
    print("\nAvailable Locations:")
    for loc in locations:
        print(f"- {loc}")
    print()

    # 3. Ask the user for 'source' and 'destination'
    try:
        source_input = input("Enter source: ").strip()
        destination_input = input("Enter destination: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n\nOperation cancelled.")
        return

    # 4. Add Input Validation
    if not source_input or not destination_input:
        print("\nError: Source and destination cannot be empty.")
        return

    # Case-insensitive lookup mapping user input to canonical location name
    location_map = {loc.lower(): loc for loc in locations}
    source = location_map.get(source_input.lower())
    destination = location_map.get(destination_input.lower())

    if not source:
        print(f"\nError: Location '{source_input}' is not a valid campus location.")
        return

    if not destination:
        print(f"\nError: Location '{destination_input}' is not a valid campus location.")
        return

    if source == destination:
        print(f"\nSource and destination are the same ({source}).")
        print("Total distance: 0 m")
        return

    # 5. Call find_shortest_route(ROUTES, source, destination)
    route, distance = find_shortest_route(ROUTES, source, destination)

    # 6. Call display_route(route, distance)
    display_route(route, distance)


if __name__ == "__main__":
    main()


