# Python Environment Setup Guide

This guide documents the Python backend development environment setup for this workspace. This is a generic setup suitable for various Python API projects using FastAPI.

## Prerequisites
- **Python**: Version 3.12 is installed.
- **Git**: Installed and configured.

## Virtual Environment
A project-specific virtual environment is located at `.venv` in the root of the workspace. This isolates project dependencies from the global Python installation.

### Activating the Environment
Before working on the project, always activate the virtual environment in your terminal.

**Windows (PowerShell)**:
```powershell
.\.venv\Scripts\Activate.ps1
```
> [!NOTE]
> If you encounter an "Execution Policies" error when activating the environment, you may need to allow local scripts to run by executing `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` in an Administrator PowerShell.

### Deactivating the Environment
To exit the virtual environment and return to the global Python environment, simply run:
```powershell
deactivate
```

## Dependencies
The environment comes pre-installed with the basic tools for backend development:
- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **Uvicorn**: An ASGI web server implementation for Python.

### Installing New Dependencies
To install additional dependencies, ensure the virtual environment is activated and use `pip`:
```powershell
pip install <package-name>
```

## Verification
To verify the environment is correctly set up, ensure your virtual environment is activated and run:

1. **Verify Python and pip**:
   ```powershell
   python --version
   pip --version
   ```

2. **Verify FastAPI and Uvicorn**:
   ```powershell
   python -c "import fastapi; print(fastapi.__version__)"
   uvicorn --version
   ```

## IDE Configuration
The workspace is configured to automatically use the Python interpreter from the virtual environment in VS Code/Antigravity IDE via `.vscode/settings.json`.

## Git Setup
Git is installed and configured. Basic configuration (username and email) is already set. You can verify it by running:
```powershell
git config user.name
git config user.email
```
