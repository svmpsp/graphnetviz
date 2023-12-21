"""Graphics and visualization."""
from pathlib import Path

import networkx as nx
import numpy as np
import pyvis

from .adt import NetworkGraph


def print_adjacency_matrix(graph: NetworkGraph):
    """Prints the adjacency matrix or the input graph
    to stdout.

    :param graph: input graph
    :type graph: NetworkGraph
    """
    adjacency_matrix = np.array(nx.adjacency_matrix(graph).todense())
    print(adjacency_matrix)


def to_html(graph: NetworkGraph):
    """Generates an HTML file containing a visualization of
    the input graph.

    :param graph: input graph
    :type graph: NetworkGraph
    """
    net = pyvis.network.Network(notebook=False)

    net.from_nx(graph)
    net.toggle_physics(False)
    # net.show_buttons(filter_=['physics'])
    Path("./output").mkdir(parents=True, exist_ok=True)
    net.show("./output/example_net.html", notebook=False)
