import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_file
from bokeh.models import ColumnDataSource, HoverTool

# Malzemeler ve ısı iletkenlikleri (W/mK)
materials = ["Aluminum", "Copper", "Glass", "Stainless Steel", "Wood"]
thermal_conductivities = [205, 398, 0.8, 16, 0.12]

# Veri kaynağını oluşturun
source = ColumnDataSource(data=dict(materials=materials, thermal_conductivities=thermal_conductivities))

# Grafiği oluşturun
output_file("thermal_conductivity.html")
p = figure(x_range=materials, height=350, title="Thermal Conductivity of Materials")
p.vbar(x="materials", top="thermal_conductivities", width=0.8, source=source)

# Eksen ve başlık ayarları
p.xgrid.grid_line_color = None
p.y_range.start = 0
p.xaxis.axis_label = "Materials"
p.yaxis.axis_label = "Thermal Conductivity (W/mK)"

# Imleç üzerinde görünen araç ucu (Hover Tool) ekle
hover = HoverTool()
hover.tooltips = [("Material", "@materials"), ("Thermal Conductivity", "@thermal_conductivities W/mK")]
p.add_tools(hover)

# Grafiği gösterin
show(p)