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


sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10, 6))

shp_path = "..\\usshapefiles\\s_11au16.shp"

sf = shp.Reader(shp_path)
df = read_shapefile(sf)
