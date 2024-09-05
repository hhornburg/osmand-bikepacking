# OsmAnd Bikepacking Profile

For the moment it is only a map style strongly inspired by the [Elevate theme](https://www.openandromaps.org/en/legend/elevate-mountain-hike-theme) for Mapsforge maps. It is designed for bikepacking and touring.

## Things I learned writing the Rendering Style

- You can't just have your own renderingProperty. The UI does not adapt to the options you give.

### Shadows

You have to activate the rendering of line shadows using the snippet below (it is important to use ˋcaseˋ and not ˋapplyˋ, because otherwise it silently fails):

ˋˋˋˋ
    <renderingAttribute name="shadowRendering">
        <!-- 0 - no shadow, 1 - one step, 2 - blur shadow, 3 - solid shadow -->
        <case attrIntValue="3" />
    </renderingAttribute>
ˋˋˋ

The shadows for lines seem to be rendered after the area objects with order 10, but before area objects with order 11.