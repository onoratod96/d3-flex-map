
global root "A:/Github/d3-flex-map"

adopath + "${root}"

import delimited using "${root}/data/covid_confirmed_cases_by_county.csv", clear

* CD to root for now, XX Need to implement this in the ado based on where the ado is stored
qui cd ${root}

d3Choropleth total_confirmed_cases,  ///
	geovar(county_fips) ///
	geofile("us_counties.json") ///
	geojsonvar("COUNTY_FIPS")