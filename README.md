# project_gateway

A simple Flask API gateway.

## Requirements

- Python 3.8+
- make (macOS/Linux) or PowerShell (Windows)
- Docker + Docker Compose (for containerized setup)

## Setup

**macOS/Linux**

Create a virtual environment and install dependencies:

```bash
make setup
```

**Windows (PowerShell)**

```powershell
python -m venv venv
pip install -r requirements.txt
```

## Running Locally

**macOS/Linux**

Activate the virtual environment:

```bash
source venv/bin/activate
```

Start the development server:

```bash
make run
```

**Windows (PowerShell)**

Activate the virtual environment:

```powershell
.\venv\Scripts\Activate.ps1
```

> If you get an execution policy error, run:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

Start the development server:

```powershell
$env:FLASK_APP = "base.py"
python -m flask run
```

The server will be available at `http://127.0.0.1:5000`.

## Running with Docker

This is the recommended approach for local development. The current directory is mounted into the container, so any code changes take effect immediately without rebuilding.

1. Build the image:

**macOS/Linux**
```bash
make docker-build
```

**Windows (PowerShell)**
```powershell
docker compose build
```

2. Start the container:

**macOS/Linux**
```bash
make docker-up
```

**Windows (PowerShell)**
```powershell
docker compose up -d
```

The server will be available at `http://127.0.0.1:5001`.

## Endpoints

| Method | Path | Response |
|--------|------|----------|
| GET | `/` | `{}` |
| GET | `/hello` | `{"message": "Hello World"}` |
| GET | `/hello/<id>` | `{"message": "Hello World", "id": "MyId-<id>"}` |

`<id>` accepts alphanumeric characters and hyphens (`-`).

### Restarting the container

**macOS/Linux**

```bash
make docker-restart
```

**Windows (PowerShell)**

```powershell
docker compose restart app
```

### Stopping the container

**macOS/Linux**

```bash
make docker-down
```

**Windows (PowerShell)**

```powershell
docker compose down
```

## Cleanup

**macOS/Linux**

Deactivate the virtual environment:

```bash
deactivate
```

Remove the virtual environment and cache:

```bash
make clean
```

**Windows (PowerShell)**

Deactivate the virtual environment:

```powershell
deactivate
```

Remove the virtual environment and cache:

```powershell
Remove-Item -Recurse -Force venv, __pycache__
```
