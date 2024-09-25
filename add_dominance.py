"""
This example shows how to filter and modify tags and write the results back.
It changes all tag values 'yes/no' to '1/0'.
"""

import osmium
import osmium.osm
import sys
import pandas as pd


class DominanceAdder(osmium.SimpleHandler):

    def __init__(self, writer):
        super(DominanceAdder, self).__init__()
        self.writer = writer
        self.dominance_data = pd.read_csv(
            "https://geo.dianacht.de/topo/topographic_isolation_viefinderpanoramas.txt",
            skiprows=15,
            names=["id", "lon", "lat", "dominance"],
            sep=";",
        )

    def add_dominance(self, peak: osmium.osm.Node) -> osmium.osm.Node:
        # if there are no tags we are done
        if not peak.id in self.dominance_data.index:
            return peak
        newtags = [
            osmium.osm.Tag(
                "dominance", str(self.dominance_data.loc[peak.id, "dominance"])
            )
        ]
        newtags.extend(peak.tags)
        return peak.replace(tags=newtags)

    def node(self, o):
        self.writer.add_node(self.add_dominance(o))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_dominance.py <infile> <outfile>")
        sys.exit(-1)

    writer = osmium.SimpleWriter(sys.argv[2])
    DominanceAdder(writer).apply_file(sys.argv[1])

    writer.close()
