# PythonDevContainer

This repository demonstrates how to run Python in a development container using Visual Studio Code.

## Prerequisites

Before you begin, ensure you have the following installed:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Docker](https://www.docker.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for Visual Studio Code

## Getting Started

1. Clone this repository:

   ```bash
   git clone https://github.com/mdelgert/PythonDevContainer.git
   cd PythonDevContainer
   ```

2. Open the repository in Visual Studio Code.

3. Reopen the folder in a development container:
   - Press `F1` to open the Command Palette.
   - Search for and select `Dev Containers: Reopen in Container`.

4. Once the container is ready, open a terminal in Visual Studio Code and run Python scripts as needed:
   ```bash
   python example.py
   ```

5. To install additional Python packages, use `pip`:
   ```bash
   pip install package_name
   ```