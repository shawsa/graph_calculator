from graph_calculator.graph import Graph
from graph_calculator.animals import (
    AnimalsCSV,
    CatsColumn,
    DogsColumn,
    MamalsColumn,
    CoolnessConfig,
    CoolnessPerCatColumn,
    DogAverage,
    DogMedian,
    EnoughDogs,
)

animals_csv = AnimalsCSV.from_file("animals.csv")
coolness_config = CoolnessConfig.from_file("coolness.yaml")


graph = Graph()

# add inputs
graph.add_node(animals_csv)
graph.add_node(coolness_config)


# add desired fields
graph.add_node(MamalsColumn())
graph.add_node(CoolnessPerCatColumn())
# graph.add_node(DogAverage())
graph.add_node(DogMedian())
graph.add_node(EnoughDogs())

print("before calculation")
print(graph)
for node in graph.nodes:
    print(node.name)
    print(node.value)
    print()


print("\n\n")
print("Calculate Mamals")
graph.calculate_node(MamalsColumn, verbose=True)
print(graph)
for node in graph.nodes:
    print(node.name)
    print(node.value)
    print()


print("\n\n")
print("Calculate coolness")
graph.calculate_node(CoolnessPerCatColumn, verbose=True)
print(graph)
for node in graph.nodes:
    print(node.name)
    print(node.value)
    print()

print("\n\n")
print("Calculate enough dogs")
graph.calculate_node(EnoughDogs, verbose=True)
print(graph)
for node in graph.nodes:
    print(node.name)
    print(node.value)
    print()
