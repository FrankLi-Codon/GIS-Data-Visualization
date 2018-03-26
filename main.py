def truncate_colormap(cmap, minval=0.0, maxval=1.0, n=-1):
    import matplotlib.colors as mcolors
    import numpy as np
    if n == -1:
        n = cmap.N
    new_cmap = mcolors.LinearSegmentedColormap.from_list(
         'trunc({name},{a:.2f},{b:.2f})'.format(name=cmap.name, a=minval, b=maxval),
         cmap(np.linspace(minval, maxval, n)))
    return new_cmap


def overlay_map(base_gdf, overlay_gdf, bc, oc, **graph_param):
#bc_name: base column name, oc_name = overlay_column_name, bc = base colormap
    import geopandas as gpd
    import matplotlib.pyplot as plt
    bc_name = graph_param['bc_name']
    oc_name = graph_param['oc_name']
    title = graph_param['title']
    bl_name = graph_param['bl_name']
    ol_name = graph_param['ol_name']


    fig, ax = plt.subplots(1, figsize = (25,12))
    ax.axis('off')
    base_map =  base_gdf.plot(ax = ax, column= bc_name,
                             scheme='fisher_jenks', cmap= bc,
                             legend=True, k =6)
    base_map.get_legend().set_title(bl_name, prop={'size':12})
    base_leg = base_map.get_legend()
    overlay_gdf.plot(ax = base_map, column= oc_name,
                          scheme='fisher_jenks', cmap= oc,
                          markersize = 10, legend=True, k =8)
    ax.set_title(title,fontsize=20)
    ax.get_legend().set_title(ol_name, prop ={'size': 12})
    ax.add_artist(base_leg)
    base_leg.set_bbox_to_anchor((1, 0.4))
    ax.get_legend().set_bbox_to_anchor((1, 0.2))
    ax.set_xlim([-130, -60])
    ax.set_ylim([23, 52])

    return fig