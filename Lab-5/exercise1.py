def display_resources(resources):
    if len(resources) == 0:
        return(print("Empty List"))
    
    for x in resources:
        if x[3] < 0:
            print("Negative")
        else:
            print(x[0], x[1], x[2], x[3])

def search_by_category(resources, category):
    if len(resources) == 0:
        return(print("Empty List"))

    found = False

    for x in resources:
        if x[3] < 0:
            print("Negative Quantity")
        elif x[2] == category:
            print(x[0], x[1], x[2], x[3])
            found = True

    if found == False:
        print("No resources found in this category")

def find_unavailable(resources):
    if len(resources) == 0:
        return(print("Empty List"))

    found = False

    for x in resources:
        if x[3] < 0:
            print("Negative Quantity")
        elif x[3] == 0:
            print(x[0], x[1], x[2], x[3])
            found = True

    if found == False:
        print("No unavailable resources found")

resources = [
    [101, "Laptop", "Electronics", 8],
    [102, "Projector", "Electronics", 3],
    [103, "Whiteboard", "Classroom", 5],
    [104, "Microphone", "Audio", 3],
    [105, "Camera", "Electronics", 2]
]

display_resources(resources)
search_by_category(resources, "Electronics")
find_unavailable(resources)

empty = []
display_resources(empty)

negative = [[101, "Laptop", "Electronics", -3]]
display_resources(negative)