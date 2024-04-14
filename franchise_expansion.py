import streamlit as st
import streamlit_highcharts as hct
import requests

# Fetch the world topology JSON for Highcharts map
topology_response = requests.get('https://code.highcharts.com/mapdata/custom/world.topo.json')
world_topology = topology_response.json()

# Data for the map with updated city and country information
data = [
    ['UAE', 'United Arab Emirates', '2022', 24.00, 54.00, 5, 2, 1, 2],
    ['Australia', 'Australia', '2022', -33.87, 151.20, 6, 3, 2, 1],
    ['Miami', 'USA', '2022', 25.76, -80.19, 4, 1, 1, 2],
    ['Charlotte', 'USA', '2022', 35.22, -80.84, 3, 1, 0, 2],
    ['Santa Barbara', 'USA', '2022', 34.42, -119.70, 2, 0, 1, 1],
    ['Los Angeles', 'USA', '2022', 34.05, -118.24, 5, 2, 2, 1]
]

# Configuration for the Highcharts map
chart_def = {
    "chart": {
        "map": world_topology
    },
    "title": {
        "text": "Medals in Various Cities (2022)",
        "align": "left"
    },
    "subtitle": {
        "text": "Source: Fictional Data"
    },
    "mapNavigation": {
        "enabled": True,
        "buttonOptions": {
            "verticalAlign": "bottom"
        }
    },
    "tooltip": {
        "headerFormat": "",
        "pointFormat": "{point.city} ({point.country}, {point.year})<br/>" +
                       "Total medals: {point.z}<br/>" +
                       '<span style="color: #ffd700;">●</span> {point.gold}<br/>' +
                       '<span style="color: #c0c0c0;">●</span> {point.silver}<br/>' +
                       '<span style="color: #cd7f32;">●</span> {point.bronze}<br/>'
    },
    "series": [{
        "name": "Medals data",
        "type": "mapbubble",
        "color": "#FF5733",
        "keys": ["city", "country", "year", "lat", "lon", "z", "gold", "silver", "bronze"],
        "data": data,
        "minSize": "5%",
        "maxSize": "12.5%"
    }]
}

# Display the map using streamlit_highcharts
st.title("Olympic Medals Distribution")
hct.streamlit_highcharts(chart_def, height=640)  # 600 is the chart height



