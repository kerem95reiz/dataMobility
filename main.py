# Coordinates needed for the basemap start position
# Istanbul
# westlimit=28.5804; southlimit=40.879; 
# eastlimit=29.4537; northlimit=41.1743

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# import matplotlib.cm

# from matplotlib.patches import Polygon
# from matplotlib.collections import PatchCollection
# from matplotlib.colors import Normalize

if __name__ == '__main__':
    fig, ax = plt.subplots(figsize=(10, 20))
    m = Basemap(
        resolution='c',
        projection='merc',
        lat_0=40.9, lon_0=28.9,
        llcrnrlon=28.5, llcrnrlat=40.8, urcrnrlon=29.4, urcrnrlat=41.1
    )

    m.drawmapboundary(fill_color='#46bcec')
    m.fillcontinents(color='#f2f2f2', lake_color='#46bcec')
    m.drawmapboundary()
    # m.fillcontinents()
    # m.drawcoastlines()