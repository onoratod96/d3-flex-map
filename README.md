# d3-flex-map
D3 Code to produce flexible choropleth maps

## Viewing the maps

To view the map:
1. Open Command prompt (Windows) or Terminal (Mac) (**Note:** You will need `python` installed on your machine). 
2. Navigate to the directory where the code is located.
3. Enter the following command:

```
python -m http.server 8888 &
```

This will create a local server on your machine over port 8888. Open your preferred browser, enter `http://localhost:8888`, and click on the `.html` file you want to view. 

## Folder Structure

Files are organized into a few main folders:

- **data** stores the raw data used in creating various maps. This is also where `d3Choropleth` outputs the relevant data to map in `temp_data.csv` 
- **examples** stores `.html` files that create example maps for testing `flex_map.js`
- **geoJSON** stores the geoJSON files used for the map examples
- **js** stores the `flex_map.js` code and other Javascript files used in examples or `flex_map.js` 
- **screenshots** is where we saving maps created by `d3Choropleth` 
- **settings** is where we store `json` settings files that are used by `map.html` to load in the arguments for the `flex_map.js` function

## Project Idea

The idea is to write a Stata ado program that takes a geographic variable and a display variable and creates a choropleth map in D3. 

The basic structure for how this will work is that the Stata program will call a Python program. The Python program will create a local server on the user's machine and serve the D3 code to this local server. Then we will use a "headless browser" to access the HTML and take a screenshot of the map.

There are a few key components to get this to work. 

### Stata ado 

The first component is the Stata `.ado` program. This program will take user specified options for the map and the data to display and create the necessary files for the downstream programs. This program will call the Python program with command line arguments that contain information on where important files are stored and how we should draw the map.

### Python Program

The Python program has several key tasks. 

1. First it will read in the command line arguments which contain settings for the map and information about files that contain the relevant data. Then it will write these settings into a JSON file so that the HTML code can read them in when its time to make the map. 
2. Then it will create a local server on the user's machine. 
3. Lastly, it will serve the HTML to the local server and take a screenshot of the map through a headless browser using `pyppeteer` a Python port of Google's Puppeteer library. 

### HTML Code

There will be a HTML file that will act as a skeleton to create the map. It will call a D3/Javascript function in the `<script>` section. The arguments to this function will be read in via the JSON file that the Python program creates. This is the file that will be served over the local server and processed by the headless browser. 

### D3 Code

Lastly, we need a flexible Javascript function that draws the map using D3. 

## Main Files

### `d3Choropleth.ado` 

This is the Stata ado program that turns Stata data into D3 Choropleth maps. Its main functions are to:

- Save the relevant data in `data`
- Call `map_maker.py` with the relevant arguments

### `test_d3Choropleth.do`

This do file tests the functionality of `d3Choropleth.ado`

### `map.html`

This is the HTML code that is served to the local server. Its main functions are to:

- Read in the map settings from `settings/map_settings`
- Call the `flex_map` function with the appropriate arguments

### `map_maker.py`

This is the Python script called by `d3Choropleth.ado`. Its main functions are to:

- Read in the command line arguments.
- Write the appropriate arguments to `settings/map_settings.json`
- Open a local server on the users machine
- Open `map.html` via a headless browser
- Take a screenshot of the contents of the web page created by `map.html`
- Save this screenshot to the appropriate location
- Kill the local server
- Display the screenshot