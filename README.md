# lpfgaz

A python package for working with data in the Linked Places Format (LPF)

# install and config

- For functions involving the Geonames API, the environment variable `GEONAMES_USER` must be set to a string that is a valid GeoNames username. In the absence of this environment variable, the "demo" username is used, which almost always results in a "denied" response from the API.

## Roadmap

- [ ] Support all LPF complex objects with corresponding python classes, each with intuitive properties for accessing data.
    - [ ] LPFFeatureCollection (in progress)
        - [ ] Read an LPF JSON file
        - [ ] Write an LPF JSON file
        - [ ] Read an [LP-TSV file](https://github.com/LinkedPasts/linked-places-format/blob/main/tsv_0.5.md)
    - [ ] LPFFeature (in progress)
        - [x] get properties:title
        - [x] get properties:@id
        - [x] get properties:ccodes
            - [x] lookup countries from ccodes (implemented with issue #1)
            - [x] validate ccodes (implemented with issue #1)
        - [x] get properties:fclasses
            - [ ] lookup feature class names from fclasses (in work in issue #2)
            - [ ] validate fclasses (in work in issue #2)
        - [ ] are there other properties in the spec not represented in the example JSON?
        - [ ] LPFWhen
            - [ ] LPFTimeSpan
            - [ ] LPFTimePeriod
        - [ ] LPFName
        - [ ] LPFType
        - [ ] LPFGeometry
        - [ ] LPFLink
        - [ ] LPFRelation
        - [ ] LPFDescription
        - [ ] LPFDepiction


