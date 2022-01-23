import pandas as pd
import folium

from src.markup_class import MarkUp

mk = MarkUp()

def load_data():
    file_path = "data/static_mock_data.csv"

    df = pd.read_csv(file_path)

    # group data by locations and count
    df_group = df.groupby(by=mk.groupby).agg({mk.location_name: "count"}).rename(columns={mk.location_name: mk.count}).reset_index()

    return df_group


def update_map(df, order_by=mk.count, ascending=False):

    df.sort_values(by=order_by, ascending=ascending)

    start_location = df.iloc[0]

    
    my_map = folium.Map(
        location = [start_location[mk.location_lat], start_location[mk.location_long]],
        zoom_start=2
        )

    # add markers on map
    
    for _, location in df.iterrows():
        folium.Marker(
            location = [location[mk.location_lat], location[mk.location_long]],
            popup=location[mk.location_name],
            tooltip=location[mk.location_name]
            ).add_to(my_map)

    my_map.fit_bounds(my_map.get_bounds(), padding=(30, 30))
    
    
    # size of markers proportional to counts

    return my_map


def load_map():

    data = load_data()

    my_map = update_map(data)

    return my_map

