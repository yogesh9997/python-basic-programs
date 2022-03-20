import gmaps
import gmaps.datasets

gmaps.configure(api_key=api_key)
eartquake_df=gmaps.datasets.load_datasets_as_df('earthquakes')
loaction=earthquake_df[['latitude','longitude']]
weight=earthquake_df['magnitude']
fig=gmaps.figure()
fid.add_layer(gmaps.heatmap_layer(location,weights=weights))
fig
