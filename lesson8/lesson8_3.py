from tools import get_youbikes
import streamlit as st

youbikes_data: list[dict] = get_youbikes()

# Create a list of unique areas (sarea)
areas = sorted(list(set(station['sarea'] for station in youbikes_data)))

# Create two columns
left_column, right_column = st.columns(2)

# Left column - Dropdown for areas
with left_column:
    selected_area = st.selectbox(
        '選擇行政區域',
        areas
    )

# Right column - Display stations for selected area
with right_column:
    st.write(f'## {selected_area}的站點')
    area_stations = [station for station in youbikes_data if station['sarea'] == selected_area]
    for station in area_stations:
        st.write(f" {station['sna']}")
        st.write(f"地址: {station['ar']}")
        st.write("---")

# Map display at the bottom
st.write('## 站點地圖')
stations_for_map = [
    {
        "lat": float(station['lat']),
        "lon": float(station['lng']),
        "name": station['sna']
    }
    for station in area_stations
]

# Display map with station markers
st.map(stations_for_map)














