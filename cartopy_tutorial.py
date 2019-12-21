# -*- encoding: utf-8 -*-
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

# 投影
# ax = plt.axes(projection=ccrs.PlateCarree())
ax = plt.axes(projection=ccrs.Mollweide())

# 绘地图
# ax.coastlines()   # 海岸线
ax.stock_img()      # 底图

# 添加数据
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='blue', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),
         )

plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),
         )

plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',
         transform=ccrs.Geodetic())

plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',
         transform=ccrs.Geodetic())


# Save the plot by calling plt.savefig() BEFORE plt.show()
plt.savefig('./map_output/output_map.svg')

plt.show()
