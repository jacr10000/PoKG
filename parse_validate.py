from rdflib import Graph
from pyshacl import validate

graph = Graph()
graph.namespace_manager.bind('xsd', 'http://www.w3.org/2001/XMLSchema#')
graph.parse('p_kg.ttl', format='turtle')

shacl = Graph()
shacl.namespace_manager.bind('xsd', 'http://www.w3.org/2001/XMLSchema#')
shacl.parse('p_shacl.shacl')

r = validate(graph, shacl_graph=shacl, inference='rdfs')
conforms, results_graph, results_text = r