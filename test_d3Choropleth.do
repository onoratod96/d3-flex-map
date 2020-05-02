
global root "A:/Github/d3-flex-map"
adopath + "${root}"

import delimited using "${github}/d3-flex-map/data/covid_confirmed_cases_by_county.csv", clear

// COVID cases US
d3Choropleth total_confirmed_cases using "${root}/screenshots/covid_cases.png",  ///
	geovar(county_fips) ///
	geofile("us_counties.json") ///
	geojsonvar(COUNTY_FIPS)
	
import delimited using "${github}/d3-flex-map/data/3rd_grade_math_scores_nyc.csv", clear

// NYC Tract Math Scores
d3Choropleth raw_math_2015_3_all using "${root}/screenshots/nyc_math.png", ///
	geovar(geoid) ///
	geofile("nyc_census_tracts.json") ///
	geojsonvar(geoid)
