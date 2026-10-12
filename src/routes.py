"""
Campus Connections (Routes)

Represent the connections between different locations and the distance between them.
Use a dictionary where the keys are locations, and the values are also dictionaries 
representing connected locations and the distance in meters.

Make sure the graph is bidirectional:
if Main Gate connects to CSE Block, CSE Block must also connect to Main Gate with the same distance.

Example format:
ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        # Add more connections...
    },
    # Add more locations...
}
"""

# Define the full ROUTES dictionary
ROUTES = {
    "Main Gate": {
        "CSE Block": 120,
        "Canteen": 180,
        "Admin Block": 100,
    },
    "CSE Block": {
        "Main Gate": 120,
        "Library": 80,
        "ECE Block": 90,
        "Canteen": 150,
    },
    "ECE Block": {
        "CSE Block": 90,
        "Library": 70,
        "Mechanical Block": 100,
    },
    "Mechanical Block": {
        "ECE Block": 100,
        "Civil Block": 80,
        "Sports Complex": 160,
    },
    "Civil Block": {
        "Mechanical Block": 80,
        "Admin Block": 150,
    },
    "Library": {
        "CSE Block": 80,
        "ECE Block": 70,
        "Auditorium": 110,
        "Admin Block": 130,
    },
    "Auditorium": {
        "Library": 110,
        "Admin Block": 90,
        "Hostel Block": 160,
    },
    "Canteen": {
        "Main Gate": 180,
        "CSE Block": 150,
        "Hostel Block": 140,
        "Sports Complex": 200,
    },
    "Hostel Block": {
        "Canteen": 140,
        "Auditorium": 160,
        "Sports Complex": 120,
    },
    "Sports Complex": {
        "Canteen": 200,
        "Hostel Block": 120,
        "Mechanical Block": 160,
    },
    "Admin Block": {
        "Main Gate": 100,
        "Library": 130,
        "Civil Block": 150,
        "Auditorium": 90,
    },
}


