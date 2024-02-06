# Calculator Project

This is a simple calculator application built with Python and PySide6.

![Calculator screenshot](https://github.com/danielzanelli/Portfolio/assets/83187517/153d3417-d1af-4176-ad26-d193a8df62b8)


## Features

- Basic arithmetic operations: addition, subtraction, multiplication, and division.
- Advanced mathematical operations: power, square root, sine, cosine, tangent, and natural logarithm.
- Keyboard shortcuts for all buttons.

## Windows Executable

1. Download the `Calculator.exe` file on this folder.
2. Run the executable.

## Linux Executable

1. Download the `Calculator` file on this folder.
2. Open a terminal where the file is located.
3. Use `sudo chmod +x Calculator` to make the file executable.
4. Run it by using `./Calculator` on the terminal or by double clicking on the file.

## Execute from Source Code

1. Clone this repository.
2. Install the requirements with `pip install pyside6`.
3. Go into the `src` folder.
4. Run `python calculator.py` to start the application.

## Compile Source Code into Executable

1. Ceate a new virtual environment in the src folder with `python -m venv myenv`.
2. Activate the environment with `myenv\Scripts\activate.bat` for Windows or `source myenv/bin/activate` for MacOS/Linux.
3. Install the required packages with `pip install pyside6 pyinstaller`
4. Compile into an executable using `pyinstaller calculator.spec`
    
The spec file in this project contains the build configuration. The final executable will be in the resulting `dist` folder. Note that the executable will be made only for the operating system on which it is compiled.


## Usage

Use the buttons on the calculator or the corresponding keyboard shortcuts to perform calculations. Press "Enter" or "Return" to calculate the result.


## License

[MIT](https://choosealicense.com/licenses/mit/)
