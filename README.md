# Debug-Visuals

A collection of functions that can be used inside the [Debug Visualizer](https://marketplace.visualstudio.com/items?itemName=hediet.debug-visualizer) VS Code extension.

## Features

Features are limited to python ready-to-use functions for visualizing variables in the Debug visualizer view.

Here ist a list of all supported types and visualizations

| Type                     | Visualization                             |
| ------------------------ | ----------------------------------------- |
| Shapely geometries       | Plotted with plotly                       |
| GeoPandas GeoDataFrame   | Plotted with plotly                       |
| GeoPandas GeoSeries      | Plotted with plotly                       |
| List[int \|float]        | Values plotted in graph                   |
| List[List[int \| float]] | Value sets plotted in multiple line graph |
| List[Any]                | List graph of nodes                       |
| dict                     | AST tree view                             |

## Installation
The python package is available on pypi:
```bash
pip install debug-visuals
```

## Usage
### Python
When debugging in python, just import the abstract Visualizer class:
```python
from debug_visuals import Visualizer
```
And use it inside the debug visualizer view:
```python
Visualizer.vis(your_variable)
```

`Visualizer.vis()` will automatically choose the type of visualization for the type stored in the given variable. You can also manually choose the type of visualization by using the underlying functions directly:

| Function name | Visualization          |
| ------------- | ---------------------- |
| shape()       | Plotly drawing         |
| vis_list()    | List graph of nodes    |
| value_graph() | Value graph(s)         |
| vis_dict()    | AST view of dictionary |

