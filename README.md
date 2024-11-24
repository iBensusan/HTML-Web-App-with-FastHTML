# FastHTML Code Snippet Web App

A simple Python web app that displays a code snippet using the **FastHTML** framework. This project is ideal for creating lightweight, fast web pages without relying on extensive configurations.

## Features

- Display Python code snippets with proper formatting and styling.
- Built with the minimalistic **FastHTML** Python framework.
- Simple structure for showcasing or sharing code snippets online.

## Prerequisites

- **Python 3.7 or later**
- **FastHTML**: Install with `pip install python-fasthtml`

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/fasthtml-code-snippet-web-app.git
    cd fasthtml-code-snippet-web-app
    ```

2. Create a virtual environment (optional but recommended):
    ```bash
    python -m venv env
    source env/bin/activate  # On macOS/Linux
    env\Scripts\activate     # On Windows
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the app:
    ```bash
    python app.py
    ```

2. Open your browser and go to:
    ```
    http://127.0.0.1:5000/
    ```

3. The page will display the Python code snippet as shown in the example below.

## Example Output

The app displays a formatted Python code snippet like this:

```python
import folium
import pandas as pd

def load_data():
    return pd.read_csv("europe.csv")

data = load_data()
# Create a Folium map
m = folium.Map(location=[data["Latitude"].mean(), data["Longitude"].mean()], zoom_start=5)

for _, row in data.iterrows():
    folium.Marker(location=[row["Latitude"], row["Longitude"]],
                  popup=row["Country"],
                  tooltip=row["Country"]).add_to(m)

m.save("map.html")
```
## Learning Benefits

This project demonstrates how to:

1. Use FastHTML for building minimal web applications.
2. Display code snippets dynamically using Python.
3. Create simple HTML pages directly from Python scripts.

## License
This project is licensed under the MIT License.
