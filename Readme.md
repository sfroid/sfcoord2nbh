<h2>Convert coordinates to SF Neighborhood names.</h2>

Python script to convert (lon, lat) to a neighborhood name in San Francisco.

example:
```
>>> from getSFNeighName import getSFNeighNames
>>> locs = [(-122.424612993055, 37.8014488257836), (-122.420120319211, 37.7877570602182)]
>>> print getSFNeighNames(locs)
[u'Marina', u'Lower Nob Hill']
```

Input to getSFNeighNames is a list of (lon, lat) tuples and
it returns a list of strings containing the neighborhood names.


<h2>Installation instructions</h2>

You will need a few dependencies, that can be easily installed on
Ubuntu.

These instructions assume that you are going to use this script
in a virtualenv. If you are not using a virtualenv, simply use `sudo
pip install xyz` instead of `pip install xyz` in the commands below.


```
# start new bash shell
# and create a new virtual environment
sudo apt-get install python-software-properties
sudo add-apt-repository ppa:ubuntugis/ppa
sudo apt-get update
sudo apt-get install libgdal-dev

# use sudo in pip installs if not in a virtualenv
pip install fiona
pip install pyproj
pip install shapely
```

Now, you can simply clone this repository and run the
example code given above to test the script.

<h2>More info</h2>

The neighborhoods that the script (or shapedata) knows about:

```
'Alamo Square',
'Anza Vista',
'Apparel City',
'Aquatic Park / Ft. Mason',
'Ashbury Heights',
'Balboa Terrace',
'Bayview',
'Bernal Heights',
'Bret Harte',
'Buena Vista',
'Candlestick Point SRA',
'Castro',
'Cathedral Hill',
'Cayuga',
'Central Waterfront',
'Chinatown',
'Civic Center',
'Clarendon Heights',
'Cole Valley',
'Corona Heights',
'Cow Hollow',
'Crocker Amazon',
'Diamond Heights',
'Dogpatch',
'Dolores Heights',
'Downtown / Union Square',
'Duboce Triangle',
'Eureka Valley',
'Excelsior',
'Fairmount',
'Financial District',
'Fishermans Wharf',
'Forest Hill',
'Forest Knolls',
'Glen Park',
'Golden Gate Heights',
'Golden Gate Park',
'Haight Ashbury',
'Hayes Valley',
'Holly Park',
'Hunters Point',
'India Basin',
'Ingleside',
'Ingleside Terraces',
'Inner Richmond',
'Inner Sunset',
'Japantown',
'Laguna Honda',
'Lake Street',
'Lakeshore',
'Laurel Heights / Jordan Park',
'Lincoln Park / Ft. Miley',
'Little Hollywood',
'Lone Mountain',
'Lower Haight',
'Lower Nob Hill',
'Lower Pacific Heights',
'Marina',
'McLaren Park',
'Merced Heights',
'Merced Manor',
'Midtown Terrace',
'Mint Hill',
'Miraloma Park',
'Mission',
'Mission Bay',
'Mission Dolores',
'Mission Terrace',
'Monterey Heights',
'Mt. Davidson Manor',
'Nob Hill',
'Noe Valley',
'North Beach',
'Northern Waterfront',
'Oceanview',
'Outer Mission',
'Outer Richmond',
'Outer Sunset',
'Pacific Heights',
'Panhandle',
'Parkmerced',
'Parkside',
'Parnassus Heights',
'Peralta Heights',
'Polk Gulch',
'Portola',
'Potrero Hill',
'Presidio Heights',
'Presidio National Park',
'Presidio Terrace',
'Produce Market',
'Rincon Hill',
'Russian Hill',
'Seacliff',
'Sherwood Forest',
'Showplace Square',
'Silver Terrace',
'South Beach',
'South of Market',
'St. Francis Wood',
'St. Marys Park',
'Stonestown',
'Sunnydale',
'Sunnyside',
'Sutro Heights',
'Telegraph Hill',
'Tenderloin',
'Treasure Island',
'Union Street',
'University Mound',
'Upper Market',
'Visitacion Valley',
'West Portal',
'Western Addition',
'Westwood Highlands',
'Westwood Park',
'Yerba Buena Island'
```

The free shape data used by the script is courtesy of sfgov.

https://data.sfgov.org/Service-Requests-311-/Neighborhoods/ejmn-jyk6?

You can also modify the script easily to use the planning and
realtor shape data files

https://data.sfgov.org/Geography/SF-Realtor-Neighborhoods/wwis-y924
https://data.sfgov.org/Geography/Neighborhood-Groups-Map/qc6m-r4ih
