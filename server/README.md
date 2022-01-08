# Server

This is the Server Side folder. Inside contains:

-  __init__.py
-  datastore.py
-  sample.py
-  Makefile
-  Dockerfile

The main file is sample.py, containing the API routes and server side coding. The server runs on port 8000 when using Gitpod to view and edit the files.

## Configuration

In order to host the server on port 8000 via Gitpod, run:

```bash
cd server
make build
make run
```

In order to run the server locally, run:

```bash
cd server
run_local
```

## Testing

In order to run the server tests against the server files:

-  Split two terminals to run side-by-side (for ease of use)

-  In terminal one, run:

```bash
cd server
make build
make run
```
-  In terminal two, run:

```bash
pip install pytest
pytest test_api.py
```

When the tests have run and the results returned to the terminal, Ctrl+C in the first terminal to stop hosting the server. Running tests in the same session after the first means that you will not have to install Pytest for every test.

## Falcon Installation

Falcon is already set to install in the process of make build, make run.
However, you can manually install Falcon as shown below.

```bash
$ pip install falcon gunicorn
```

## Usage

This folder and its contents should be used for server testing according to the Freecycle API spec.

## Authors and acknowledgment

Forked from the [Caladees Frameworks and Languages Repo](https://github.com/calaldees/frameworks_and_languages_module).

## License
[MIT](https://choosealicense.com/licenses/mit/)


