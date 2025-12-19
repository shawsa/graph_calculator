from graph_calculator.graph import Graph
from graph_calculator.animals import (
    AnimalsCSV,
    DogsColumn,
    DogAverage,
    DogMedian,
    DogStat,
    EnoughDogs,
)

animals_csv = AnimalsCSV.from_file("animals.csv")

graph = Graph()

# add inputs
graph.add_node(animals_csv)

# add desired fields
# graph.add_node(DogAverage())
graph.add_node(DogMedian())
graph.add_node(EnoughDogs())

graph.calculate_node(EnoughDogs)

print(f"{graph[DogStat].name}: {graph[DogStat].value}")
print(f"Enough dogs: {graph[EnoughDogs].value}")
print()

graph = Graph()

# add inputs
graph.add_node(animals_csv)

# add desired fields
graph.add_node(DogAverage())
graph.add_node(EnoughDogs())
graph.calculate_node(EnoughDogs)
print(f"{graph[DogStat].name}: {graph[DogStat].value}")
print(f"Enough dogs: {graph[EnoughDogs].value}")
print()
