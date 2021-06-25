# 3D_houses: a _geodata_ visualization project :houses:

### The team
This project was a teamwork by [Arnaud D.](
https://github.com/Pablousse), [Lyes](
https://github.com/lyesds) and [Shilpa S.](https://github.com/ssg-hub).
### The project
This is a _learning_ project about **data visualization** using Python tools.
The objective is to generate a **3D rendering** of any building located in the Flanders region of Belgium using open data.

***Input :*** an address given by user or selected by user from a pre-determined list.
Example : Schoenmarkt 35, 2000 Antwerpen

***Output :*** a 3D image rendered for the building structure at the above address.
Example :
![Schoenmarkt35](assets/Schoenmarkt%2035,%202000%20Antwerpen%20DSM%20minus%20DTM.png)

### The timeline
This work was done during working hours in 2 weeks in June 2021 as required by the project timeline.
It means there's room for improvements in the future if more time could be allowed to it ;)

### "Maturity" and progression of the project
Please note that this project was done at the beginning of a training in AI where the teammates were enrolled. The primary objective was to **consolidate** our learnings in:
- Python (specifically in pandas, numpy and matplotlib libraries),
- Git and GitHub,
- IDEs and notebooks,
- Teamwork

This is why there is room for improvements, both for the 3D rendering itself (eg, using other plotting libraries)
and for adding other features like living area of the house in m², number of floors, if there is a pool, the vegetation in the neighborhood, etc...
Therefore, any contribution (comments, feedback, feature suggestion) or help is welcome!

### How it works (in a nutshell)
From the address of a house or building given by the final user or selected from a pre-determined list, our application retrieves:
- its location within Flanders (using an API),
- the cadastral data associated to it,
- the elevation data (please see resources.md for more info) of the location and its surroundings

Then, our python programming will ensure the 3D rendering!

### Open data used
[DSM - Digital Surface Model](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dsm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DSM,%20raster,%201m) 
[DTM - Digital Terrain Model](http://www.geopunt.be/download?container=dhm-vlaanderen-ii-dtm-raster-1m&title=Digitaal%20Hoogtemodel%20Vlaanderen%20II,%20DTM,%20raster,%201m)  
Above links contain the required _.tif_ files for DSM and DTM respectively. _.tif_ is for the elevation of a structure.

[Cadastral Data](https://eservices.minfin.fgov.be/myminfin-rest/cadastral-plan/cadastralPlan/2020/Belgium/72)  
Above link contains the required files for Belgium specific Lambert72 coordinates. They are for the location, and the shape of the building on ground.

### Installation Guide
1. Clone the project with this command in your terminal :
> git clone https://github.com/lyesds/3D_houses.git
2. Download at least one couple of DSM/DTM related files (for example DHMVIIDSMRAS1m_k15.zip _and_ DHMVIIDTMRAS1m_k15.zip). The more files you have, the larger the area of Flanders will be covered by the application.
3. Extract the content of the GeoTIFF folder inside the downloaded zip files into folders `assets/data/DSM` and `assets/data/DTM` respectively.
4. Download the cadastral data (see link above) and extract its content into `assets/data/cadastral`.
5. Lastly, go to the root of the project folder with your terminal and run the line below :
> pip install -r requirements.txt

### How to use
Click [here](link to jupyter nb) to open the interface and enjoy!


### Learning objectives
- :heavy_check_mark: consolidate the knowledge in Python :snake:, specifically in numpy, pandas and matplotlib.
- :heavy_check_mark: search and implement new libraries: **geopandas, osgeo, gdal, rasterio, shapely.**
- :heavy_check_mark: read and use the **shapefile** format
- :heavy_check_mark: read and use **.tif files** (GeoTIFF)
- :heavy_check_mark: render a **3D plot**
- :heavy_check_mark: present a **final product**

### The Client and mission behind the project
- The client is LIDAR PLANES, a company active in the Geospatial industry.  
- The goal is to  launch a new branch in the insurance business using a 3D model of houses with only their addresses as input.

**Must-have features:** 3D lookup of houses:heavy_check_mark:

**Nice-to-have features:** quick rendering:heavy_check_mark:, additional features (living area of the house in m², number of floors, if there is a pool, the vegetation in the neighborhood, etc...), better visualizations.

