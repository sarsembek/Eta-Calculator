# η Calculator with GUI using Python

This Python code provides a graphical user interface (GUI) for calculating the efficiency (η) based on user-provided data files. It also allows users to visualize the data using matplotlib. The code is structured as a Python class-based application using tkinter for the GUI, pandas for data manipulation, and numpy for calculations.

## Features

- Load data from Excel files.
- Calculate η using provided data and user inputs.
- Visualize data using matplotlib.

## Requirements

Before running this code, make sure you have the following libraries installed:

- **tkinter**: For creating the graphical user interface.
- **pandas**: For data manipulation.
- **numpy**: For numerical calculations.
- **matplotlib**: For data visualization.

You can install these libraries using pip:

```bash
pip install tkinter pandas numpy matplotlib
```

## How to Use

1. Clone or download this repository to your local machine.
2. Run the Python script `main.py`.
3. The GUI window will open, allowing you to interact with the application.
4. Follow these steps in the GUI:
  * Click the "Выбрать I(ti) файл" button to select an Excel data file containing time and current values (I(ti)).
  * Click the "Выбрать I0(ti) файл" button to select another Excel data file containing time and current values (I0(ti)).
  * Enter the values for Δt0 and Δt in the corresponding entry fields.
  * Click the "Рассчитать η" button to calculate η based on the provided data and parameters.
  * The calculated efficiency (η) will be displayed on the GUI.
  * Click the "График" button to visualize the I(ti) and I0(ti) data on a graph.

## Author 

[Arman Sarsembek](https://github.com/sarsembek)
