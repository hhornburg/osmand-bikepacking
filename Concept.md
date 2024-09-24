# Concept

The goal is to transmit as much information as possible while still being easy to read and clear.

## Highways

Following information is needed by the user to make informed choices on the route to take:

- Surface Conditions
- Estimated Traffic
- Access Restrictions
- How clearly the path/track exist
- Bridge/Tunnel/Avalanche Protection
- Hiking/Biking Difficulty

This data is available from OSM.

### High Zoom Design Style (`minzoom=11`)

#### Line Vertical Colouring & Width

A line can have up to 3 vertical line colors, depending on line width.
While both width and color are used to indicate the estimated traffic, solely the color is used to indicate the surface conditions.
Since the outline color should be darker than the fill color, the meaning of the outline and the fill has to be adjusted respectively.

| Highway Type | Fill Width | Fill Color | Outline Color | Additional center stripe |
|--------------|------------|------------|---------------|--------------------------|
| Path, Footway, Steps etc. | 1 | Surface Conditions | None | None |
| Track, Cycleway, Residential etc. | 1 | Surface Conditions | Bike designation (if existing), else Surface Conditions | None |
| Unclassified roads | 2 | Surface Conditions | Bike designation (if existing), else Surface Conditions | None |
| Tertiary roads | 2 | Light yellow | Surface Conditions | None |
| Secondary roads | 2 | Yellow | Surface Conditions | None |
| Primary roads | 2 | Orange | Surface Conditions | None |
| Trunk roads | 2 | Red | Surface Conditions | None |
| Motorways | 2 | Red | Surface Conditions | Yellow |

The width of the line is not further increased by the road size, since these roads are not the ones that are of much interest and thus don't need to be found quickly.
A too big width also can impair the readability of the map for other roads close-by.

##### Surface Conditions

The surface conditions are divided into two categories: Paved and Unpaved.
For paved roads, the fill is white while the outline is black.
For unpaved roads, the fill is light brown while the outline is brown.
The surface conditions can be derived from the `surface` tag and as a fallback from the default for the respective highway type and the `tracktype` tag.

##### Bike Designation

For bike designated roads, the outline color is blue.

#### Line Horizontal Colouring

Horizontal stripes are used to indicate the access restrictions and hiking/biking restrictions.

#### Line Pattern

The line pattern is used to indicate the strength of the existence of the path/track.
For paths the `visibility` tag is used, for tracks the `tracktype` tag.
