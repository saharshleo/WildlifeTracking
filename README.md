# WildlifeTracking
_A geo-informatics project to keep track of different animal species and visualize factors related to them_
## Dependencies
* QGIS 3.10.3
* MapLibrary plugin
* TimeManager plugin
#### Open the wildlifeTracks.qgz in QGIS

## Layers
![image of all layers](https://github.com/saharshleo/WildlifeTracking/blob/master/DemoPlots/layers.png)<br />
**For viewing the plot of the layer click the checkbox of respective layers**
* **TIN interpolation** - Viewing the plots of black flying fox in the unknown reason by using TIN Interpolation
![image of all layers](https://github.com/saharshleo/WildlifeTracking/blob/master/DemoPlots/interpolationResult.png)
* **Path Northern Pintail** - Path view of Northern Pintail for each individual animal of that species __
* **Mixed_Animals** - categorised view on the basis of taxon canonical name 
* **Animals**
  * **Unclustered Categorized** - Initial plot of data with categorised view on the basis of sex
  * **Clustered** - Clustered view of data
* **nearestPopulated place** - Line connecting each plot of animal data to its nearest populated place 
* **nearestRiversLakes** - Line connecting each plot of animal data to its nearest rivers/lakes
* **AreaCoveredbyZebraElephant** - Polygon layer for visualizing area covered by Zebra and Elephant 
* **Buffer Analysis** - Buffer analysis for visualizing flying fox flying within 15km of populated places
![image of all layers](https://github.com/saharshleo/WildlifeTracking/blob/master/DemoPlots/bufferResult.png)
For visualizing this layer change the project CRS to EPSG:25386 and zoom to layer flyingFoxWithin15kms
* **ne_10m_populated_place_simple** - plot of populated places
* **ne_10m_rivers_lake_centerline** - Line plot of rivers and lakes centerline 
* **Google Satellite** - Base Map
## Time Series Heat Map
![image of all layers](https://github.com/saharshleo/WildlifeTracking/blob/master/DemoPlots/timeSeriesHeatmap.gif)
## Grapics Plot
* [flyingFox3d](https://github.com/saharshleo/WildlifeTracking/blob/master/GraphicsPlot/flyingFox3D.html)
  * x-axis - Latitude 
  * Y-axis - Longitude
  * Z-axis - Number of hrs
* [ibisScatterPlot](https://github.com/saharshleo/WildlifeTracking/blob/master/GraphicsPlot/ibisScatterPlot.html)
  * x-axis - Latitude 
  * Y-axis - Longitude
* [nearestPopSavannahSparrowPlot](https://github.com/saharshleo/WildlifeTracking/blob/master/GraphicsPlot/nearestPopSavannahSparrowPlot.html)
  * x-axis - Nearest river/lake name 
  * Y-axis - Distance of Savannah Sparrow from that river/lake
* [nearestPopWhalePLot](https://github.com/saharshleo/WildlifeTracking/blob/master/GraphicsPlot/nearestPopWhalePLot.html)
  * x-axis - HubName(populated place) 
  * Y-axis - HubDist(distance from populated place)
* [nearestRiverIbis](https://github.com/saharshleo/WildlifeTracking/blob/master/GraphicsPlot/nearestRiverIbis.html)
  * x-axis - Nearest river/lake name 
  * Y-axis - Distance of American Ibis from that river/lake
## Sample Plot
* [QGISCloud](https://qgiscloud.com/ganadhish/final_wildlife_tracking/?bl=&l=black%20vulture%2Cbald%20eagle%2Cblue%20whale%2Cmallard%2CGoogle%20Satellite&t=final_wildlife_tracking&e=-22205597%2C-2573073%2C3697111%2C9822656)
* [HERE-STUDIO_1](https://studio.here.com/viewer/?project_id=82c0ea42-1daa-44bd-b988-cc04e790a83b)
* [HERE-STUDIO_2](https://studio.here.com/viewer/?project_id=55d3a441-7195-44ae-a7ac-911da0fd916b)
#### [Drive link for Project Report, Demo and Ppt](https://drive.google.com/drive/folders/1zjDtE4VGgUj8hzTBJxO8vZtHaCWSXOyo?usp=drive_open)
