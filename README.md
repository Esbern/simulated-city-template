# Simulated City Workshop - Template

A template repository for creating urban simulations and digital twins using Python. This template provides a starting point for the **Simulated City Workshop**, where participants learn to model urban phenomena through programming.

## Overview

This workshop introduces Python programming through the creation of simple **urban digital twins**. The focus is on **writing simulations** that model urban phenomena such as:
- Population movement and pedestrian flows
- Disease spread in urban environments
- Traffic patterns and transportation
- Environmental factors (rain, solar radiation, etc.)
- Urban planning scenarios

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Basic understanding of programming concepts (helpful but not required)
- A code editor or IDE (VS Code, PyCharm, or Jupyter Notebook)

### Installation

1. **Clone this repository** (or use as a template):
   ```bash
   git clone https://github.com/Esbern/simulated-city-template.git
   cd simulated-city-template
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Launch Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

## Project Structure

```
simulated-city-template/
├── notebooks/              # Jupyter notebooks for simulations
│   └── 01_getting_started.ipynb
├── data/                   # Data files (GeoJSON, CSV, etc.)
│   └── README.md
├── src/                    # Python source code modules
│   └── __init__.py
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── LICENSE                # License file
└── README.md              # This file
```

## Workshop Topics

This template supports the following learning objectives:

1. **Python Basics**: Variables, loops, functions, and data structures
2. **Data Handling**: Working with pandas, GeoPandas, and GeoJSON
3. **Visualization**: Creating maps and charts with matplotlib and folium
4. **Simulation**: Building agent-based models and system dynamics
5. **Urban Analysis**: Spatial analysis and urban digital twin concepts

## Example Simulations

The `notebooks/` directory contains starter examples:
- **Getting Started**: A simple random walk simulation
- **Urban Movement**: Modeling pedestrian movement in a city
- **Disease Spread**: SIR model for contagious diseases

## Learning Resources

For comprehensive learning materials, see the main course repository:
- [Python for Planners Course](https://github.com/Esbern/Python-for-Planners)

**Additional Resources**:
- Introduction to Python for Geographic Data Analysis: [python-gis-book](https://python-gis-book.readthedocs.io/)
- Modeling and Simulation in Python: [ModSimPy](https://allendowney.github.io/ModSimPy/)
- Mesa Agent-based Modeling: [Mesa Docs](https://mesa.readthedocs.io/)

## Contributing

This is a template repository. Feel free to:
- Fork and customize for your own workshop
- Submit improvements via pull requests
- Share your simulations and examples

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

Based on the "Python for Planners" course materials by Esbern Holmes.
Inspired by urban digital twin concepts and geodesign principles.