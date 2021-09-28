import folium
import pandas
import os

unem_data = pandas.read_csv('us_unemployment.txt')
state_data = os.path.join('us-states.json')

#creating the map object, setting the location latitude and longitude as the 1st param
#zoom_start determines how close to the ground we want the map to be once opened
map = folium.Map(location = [48,-102], zoom_start=3) 

#Now we create a choropleth Map
map.choropleth(
    geo_data = state_data, #the polygon/geographical data that separates states according to their boundaries
    name = 'choropleth', #a map that uses color to show diffs in unemployment rate for each state 
    data = unem_data, #the unemployment data 
    columns = ['State','Unemployment'], #what columns we need from the unemployment data 
    key_on = 'feature.id', #the id that uniquely identifies one state from another 
    fill_color = 'YlGn', #diff colors for diff unemployment rates 
    fill_opacity = 0.7,
    line_opacity = 0.2,
    legend_name = 'Unemployment Rate %' #the name of the legend 
)

folium.LayerControl().add_to(map) #allows us to add the unemployment rate layer 

#lastly, we save the map 
map.save('Map1.html') 
