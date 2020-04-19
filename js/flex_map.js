/***
  Here are the program parameters
  geoJsonFile : This is you geoJSON data file
  dataFile : This is your data file in .csv format
  fillVariable : Variable name for the fill variable
  geoVariable : The name of the variable in dataFile that has the geoid
  geoJsonGeoVariable : The name of the variable in geJsonFile that has the geoid

  Note that geoVariable and geJsonGeoVariable have to be the same (the names can be different)
  but if you are doing tracts they would both have to contain 11 digit FIPS for instance.
***/

function flex_map(geoJsonFile, dataFile, fillVariable, geoVariable, geoJsonGeoVariable, legend_title) {
    // Canvas size
    var width = 1000,
    height = 800;

    // JS Object to hold data
    var data = {};

    // Coloring function
    var color = d3.scaleQuantile(d3.schemeRdPu[9]); 

    // Set the projection
    var projection = d3.geoAlbersUsa()
        .translate( [width/2,height/2] );

    // Create SVG
    var svg = d3.select("body").append("svg")
        .attr("width", width)
        .attr("height", height);

    // Array of files that need to be loaded in
    var files = [geoJsonFile, dataFile];
    var promises = [];

    // Try to get the files
    promises.push(d3.json(geoJsonFile));
    promises.push(d3.csv(dataFile, function(d) {
        data[d[geoVariable]] = +d[fillVariable];
        color.domain(Object.values(data));
    }));

    // Upon successful completion run the map making code
    Promise.all(promises)
    .then(function(values) {
        make_map(values[0]);
    })
    .catch(function(err) {
        console.log(err.message);
    });

    // Code to make map
    function make_map(us_states) {

      // Center the projection, should dynamically zoom
      projection.fitSize([width, height], us_states);
      // D3 path using our projection
      var path = d3.geoPath()
          .projection(projection);



      // Add a legend using Mike Bostock's legend code in legend.js
      svg.append("g")
          .attr("transform", "translate(600,100)")
          .append(() => legend({color, title: legend_title, ticks : 9, tickFormat : ".0s", width: 300}));

      // Draw the map and add the fill
      svg.append("g")
          .selectAll("path")
          .data(us_states.features)
          .enter()
          .append("path")
          .attr("d", path)
          .attr("class", "geo")
          .attr("fill", function(d) {
            var value = data[d.properties[geoJsonGeoVariable]];
            if (value) {
              return color(value);
            } else {
              return "#ccc";
            }
          });             
    }
}