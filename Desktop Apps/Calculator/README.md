# Calculator Project

This is a simple calculator application built with Python and PySide6.

## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Advanced mathematical operations: power, square root, sine, cosine, tangent, and natural logarithm.
- Keyboard shortcuts for all buttons.

## Installation

1. Clone this repository.
2. Install the requirements with `pip install pyside6`.
3. Go into the src folder.
4. Run `python calculator.py` to start the application.

## Executable Compilation

1. Ceate a new virtual environment in the src folder with 'python -m venv myenv'.
2. Activate the environment with 'myenv\Scripts\activate.bat' for Windows or 'source myenv/bin/activate' for MacOS/Linux.
3. Install the required packages with 'pip install pyside6 pyinstaller'
4. Compile into an executable using 'pyinstaller calculator.spec'
    
The spec file in this project contains the build configuration. The final executable will be in the resulting 'dist' folder.


## Usage

Use the buttons on the calculator or the corresponding keyboard shortcuts to perform calculations. Press "Enter" or "Return" to calculate the result.


## License

[MIT](https://choosealicense.com/licenses/mit/)