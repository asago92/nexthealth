import streamlit as st
import streamlit_highcharts as hg
import requests

# Fetch the world topology JSON for Highcharts map
topology = requests.get('https://code.highcharts.com/mapdata/custom/world.topo.json')

# Data for the map with updated city and country information
data = [
    ["UAE", "United Arab Emirates", "2022", 24.00, 54.00, 5, 2, 1, 2],
    ["Australia", "Australia", "2022", -33.87, 151.20, 6, 3, 2, 1],
    ["Miami", "USA", "2022", 25.76, -80.19, 4, 1, 1, 2],
    ["Charlotte", "USA", "2022", 35.22, -80.84, 3, 1, 0, 2],
    ["Santa Barbara", "USA", "2022", 34.42, -119.70, 2, 0, 1, 1],
    ["Los Angeles", "USA", "2022", 34.05, -118.24, 5, 2, 2, 1]
]


chartDef={ 'title': {
        'text': 'Medals in Various Cities (2022)',
        'align': 'left'
    },
    'subtitle': {
        'text': 'Source: Fictional Data'
    },
    'mapNavigation': {
        'enabled': True,
        'buttonOptions': {
            'verticalAlign': 'bottom'
        }
    },
    'mapView"': {
        'fitToGeometry': {
            'type': 'MultiPoint',
            'coordinates': [
                [-164, 54],  # Alaska west
                [-35, 84],   # Greenland north
                [179, -38],  # New Zealand east
                [-68, -55]   # Chile south
            ]
        }
    },
    'tooltip': {
        'headerFormat': "",
        'pointFormat': '{point.city} ({point.country}, {point.year})<br/>' +
                       'Total medals: {point.z}<br/>' +
                       '<span style="color: #ffd700;">●</span> {point.gold}<br/>' +
                       '<span style="color: #c0c0c0;">●</span> {point.silver}<br/>' +
                       '<span style="color: #cd7f32;">●</span> {point.bronze}<br/>'
    },
  'chart': {'map': 'topology'},
  'series': [{
        'name': 'Medals data',
        'type': 'mapbubble',
        'color': '#FF5733',
        'keys': ['city', 'country', 'year', 'lat', 'lon', 'z', 'gold', 'silver', 'bronze'],
        'data': data,
        'minSize': '5%',
        'maxSize': '12.5%'
    }]
}

# Display the map using streamlit_highcharts
st.title("Olympic Medals Distribution")
hg.streamlit_highcharts(chart_def, height=640)  # Specify height in pixels


