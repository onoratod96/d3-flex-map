import http.server
import socketserver
import sys, os, random, string, signal, subprocess
import time, random, string
import asyncio
import argparse
import json
from pyppeteer import launch


def parseArguments():

	parser = argparse.ArgumentParser()


	# Program options
	csv_group = parser.add_argument_group("Map maker", "Inputs to the map maker python script.")
	csv_group.add_argument('-df', "--dataFile", required = True, help="Path to the CSV file containing the data to be mapped")
	csv_group.add_argument("-gf", "--geoJsonFile", required=True, help="Path to the geoJSON file containing map geo data.")
	csv_group.add_argument("-gv", "--geoVariable", help="The name of the column with the geographic identifier.", required=True)
	csv_group.add_argument("-fv", "--fillVariable", help="The name of the csv column to plot.", required=True)
	csv_group.add_argument("-gjv", "--geoJsonGeoVariable", help="The name of the geographic identifier in the geoJSON file.", required=True)
	csv_group.add_argument("-sd", "--saveDirectory", help="The directory where the image should be saved.", required=True)

	args = parser.parse_args()

	return args

# Use the arguments passed in the command line to populate the map_settings.json
def populateSettings(args):
	with open('settings/default_settings.json') as json_file:
		settings = json.load(json_file)


	# Loop over the arguments and overwrite 
	for key in args:
		# if argument is not null or space
		if (args[key] and not str(args[key]).isspace()):
			settings[key] = args[key]

	# write the settings to map_settings.json
	with open('settings/map_settings.json', 'w') as json_file:
		json.dump(settings, json_file)

# Asynchronous function to take a screenshot using pyppeteer
async def screenshot(url, path):
    browser = await launch(headless=True)
    page = await browser.newPage()

    print("Processing HTML and D3...")
    await page.goto(url, {'waitUntil': 'networkidle2'})
    await page.screenshot({'path': path, 'fullPage': True})
    #await page.pdf({'path': 'screenshot.pdf', 'landscape' : True,  'format': 'A4'});
    await browser.close()
    print("Done!")


args = vars(parseArguments())
populateSettings(args)

# Open local host over port 8888
print("Creating local host over port 8888...")
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags = subprocess.STARTF_USESHOWWINDOW
p = subprocess.Popen("python -m http.server 8888".split(" "), startupinfo=startupinfo)
# Wait for the server to get up and running
time.sleep(0.5)
print("Saving file: " + args["saveDirectory"])
asyncio.get_event_loop().run_until_complete(screenshot("http://localhost:8888/map.html", args["saveDirectory"]))

p.terminate()

os.system("start " + args["saveDirectory"])
