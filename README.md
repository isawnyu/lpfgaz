# lpfgaz

A python package for working with data in the Linked Places Format (LPF)

## Roadmap

- [ ] Support all LPF complex objects with corresponding python classes, each with intuitive properties for accessing data.
    - [ ] LPFFeatureCollection (in progress)
    - [ ] LPFFeature (in progress)
        - [x] get properties:title
        - [x] get properties:@id
        - [x] get properties:ccodes
            - [ ] lookup countries from ccodes
            - [ ] validate ccodes
        - [x] get properties:fclasses
            - [ ] lookup feature class names from ccodes
            - [ ] validate fclasses
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

- [ ] Read an LPF JSON file

- [ ] Write an LPF JSON file

- [ ] TBD


