# OsmAnd Bikepacking Profile

For the moment it is only a map style strongly inspired by the [Elevate theme](https://www.openandromaps.org/en/legend/elevate-mountain-hike-theme) for Mapsforge maps. It is designed for bikepacking and touring.

## Things I learned writing the Rendering Style

- You can't just have your own renderingProperty. The UI does not adapt to the options you give.

### Shadows

You have to activate the rendering of line shadows using the snippet below (it is important to use ˋcaseˋ and not ˋapplyˋ, because otherwise it silently fails):

ˋˋˋxml
<renderingAttribute name="shadowRendering">
    <!-- 0 - no shadow, 1 - one step, 2 - blur shadow, 3 - solid shadow -->
    <case attrIntValue="3" />
</renderingAttribute>
ˋˋˋ

The shadows for lines seem to be rendered after the area objects with order 10, but before area objects with order 11.

### Relevance of the order of statements

The order of the statements in the rendering style is important and might not be intuitive.
The first example does not do what I would expect, while the second one does, i.e. the value set in the apply statement is not overwritten by the value set in the switch statement.

```xml
<apply>
    <!--Default case if tag is not set-->
    <apply pathEffect_0="$pathEffect_unknown" pathEffect="$pathEffect_unknown"/>
    <switch>
        <case additional="tracktype=grade1" pathEffect_0="" pathEffect=""/>
        <case additional="tracktype=grade2" pathEffect_0="$pathEffect_good" pathEffect="$pathEffect_good"/>
        <case additional="tracktype=grade3" pathEffect_0="$pathEffect_intermediate" pathEffect="$pathEffect_intermediate"/>
        <case additional="tracktype=grade4" pathEffect_0="$pathEffect_bad" pathEffect="$pathEffect_bad"/>
        <case additional="tracktype=grade5" pathEffect_0="$pathEffect_horrible" pathEffect="$pathEffect_horrible"/>
    </switch>
</apply>
```

```xml
<apply>
    <switch>
        <case additional="tracktype=grade1" pathEffect_0="" pathEffect=""/>
        <case additional="tracktype=grade2" pathEffect_0="$pathEffect_good" pathEffect="$pathEffect_good"/>
        <case additional="tracktype=grade3" pathEffect_0="$pathEffect_intermediate" pathEffect="$pathEffect_intermediate"/>
        <case additional="tracktype=grade4" pathEffect_0="$pathEffect_bad" pathEffect="$pathEffect_bad"/>
        <case additional="tracktype=grade5" pathEffect_0="$pathEffect_horrible" pathEffect="$pathEffect_horrible"/>
        <!--Default case if tag is not set-->
        <case pathEffect_0="$pathEffect_unknown" pathEffect="$pathEffect_unknown"/>
    </switch>
</apply>
```
