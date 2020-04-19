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

This will create a local server on your machine over port 8888. Open your preferred browser, enter `http//:localhost:8888`, and click on the `.html` file you want to view. 

## Folder Structure

Files are organized into a few main folders:

- **data** stores the raw data used in creating various maps
- **examples** stores `.html` files that create example maps for testing `flex_map.js`
- **geoJSON** stores the geoJSON files used for the map examples
- **js** stores the `flex_map.js` code and other Javascript files used in examples or `flex_map.js` 

