# See https://docs.osmcode.org/pyosmium/latest/cookbooks/Enhance-Tags/

import osmium
import osmium.filter
import osmium.osm
import sys
import pandas as pd


dominance_data = pd.read_csv(
    "https://geo.dianacht.de/topo/topographic_isolation_viefinderpanoramas.txt",
    skiprows=15,
    names=["id", "lon", "lat", "dominance"],
    sep=";",
)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python add_dominance.py <infile> <outfile>")
        sys.exit(-1)

    with osmium.SimpleWriter(sys.argv[2], overwrite=True) as writer:
        fp = (
            osmium.FileProcessor(sys.argv[1])
            .with_filter(osmium.filter.EntityFilter(osmium.osm.osm_entity_bits.NODE))
            .with_filter(osmium.filter.IdFilter(dominance_data.index))
            .handler_for_filtered(writer)
        )

        for obj in fp:
            newtags = [
                osmium.osm.Tag(
                    "dominance", str(dominance_data.loc[obj.id, "dominance"])
                )
            ]
            newtags.extend(obj.tags)
            writer.add(obj.replace(tags=newtags))
