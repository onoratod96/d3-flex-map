cap : program drop d3Choropleth
program define d3Choropleth
version 16
	
syntax varname(numeric) using/, geovar(varname) geofile(string) geojsonvar(string) [directory(string)]


if "`directory'" == "" {
	loc directory "${github}/d3-flex-map"
}


noi di "`using'"
* Export the data to the data section
* XX Get this to work without filepath
export delimited using "`directory'/data/temp_data.csv", quote replace

* Create the options
local options	 -df "/data/temp_data.csv" ///
				 -gf "/geoJSON/`geofile'" ///
				 -gv "`geovar'" ///
				 -fv "`varlist'" ///
				 -gjv "`geojsonvar'" ///
				 -sd "`using'"

* Call the python script from the shell
python script "`directory'/map_maker.py", args(`options')
end