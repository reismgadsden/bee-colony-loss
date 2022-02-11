import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import shapefile as shp
import seaborn as sns


def read_shapefile(sf) -> pd.DataFrame:
    fields = [x[0] for x in sf.fields][1:]

    records = [list(i) for i in sf.records()]
    shps = [s.points for s in sf.shapes()]

    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df


def plot_shape(id, sf, s=None):
    plt.figure()
    ax = plt.axes()
    ax.set_aspect('equal')

    shape_ex = sf.shape(id)

    x_lon = np.zeros((len(shape_ex.points), 1))

    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]

    plt.plot(x_lon, y_lat)
    x0 = np.mean(x_lon)
    y0 = np.mean(y_lat)
    plt.text(x0, y0, s, fontsize=10)

    plt.xlim(shape_ex.bbox[0], shape_ex.bbox[2])
    return x0, y0


def plot_map(sf, x_lim=None, y_lim=None, figsize=(11,9)):
    plt.figure(figsize=figsize)
    id = 0
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        plt.plot(x, y, 'k')

        if x_lim is None and y_lim is None:
            x0 = np.mean(x)
            y0 = np.mean(y)
            plt.text(x0, y0, id, fontsize=10)
        id = id + 1

    if x_lim is not None and y_lim is not None:
        plt.xlim(x_lim)
        plt.ylim(y_lim)


def plot_map_fill(id, sf, x_lim=None, y_lim=None, figsize=(11,9), color='r'):
    plt.figure(figsize=figsize)
    fig, ax = plt.subplots(figsize=figsize)
    for shape in sf.shapeRecords():
        x = [i[0] for i in shape.shape.points[:]]
        y = [i[1] for i in shape.shape.points[:]]
        ax.plot(x, y, 'k')

    shape_ex = sf.shape(id)
    x_lon = np.zeros((len(shape_ex.points), 1))
    y_lat = np.zeros((len(shape_ex.points), 1))
    for ip in range(len(shape_ex.points)):
        x_lon[ip] = shape_ex.points[ip][0]
        y_lat[ip] = shape_ex.points[ip][1]
    ax.fill(x_lon, y_lat, color)

    if x_lim is not None and y_lat is not None:
        plt.xlim(x_lim)
        plt.ylim(y_lim)


def main():
    sns.set(style="whitegrid", palette="pastel", color_codes=True)
    sns.mpl.rc("figure", figsize=(10, 6))

    shp_path = "..\\usshapefiles\\s_11au16.shp"

    sf = shp.Reader(shp_path)
    df = read_shapefile(sf)

    #STATE_NAME = "NC"
    #com_id = df[df.STATE == "NC"].index.array[0]
    #plot_shape(com_id, sf, STATE_NAME)
    #sf.shape(com_id)

    contiguous_x = (-125, -65)
    contiguous_y = (24, 50)

    #plot_map(sf, x_lim=contiguous_x, y_lim=contiguous_y)
    plot_map_fill(13, sf, x_lim=contiguous_x, y_lim=contiguous_y, color='y')
    plt.show()


if __name__ == "__main__":
    main()
