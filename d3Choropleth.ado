cap : program drop d3Choropleth
program define d3Choropleth
version 16
	
syntax varname(numeric), geovar(varname) geofile(string) geojsonvar(string)

* Export the data to the data section
* XX Get this to work without filepath
export delimited using "A:/Github/d3-flex-map/data/temp_data.csv", quote replace

* Create the options
local options	 -df "/data/temp_data.csv" ///
				 -gf "/geoJSON/`geofile'" ///
				 -gv "`geovar'" ///
				 -fv "`varlist'" ///
				 -gjv "`geojsonvar'"

* Call the python script from the shell
python script map_maker.py, args(`options')
end