# Client

This is the Client Side folder. Inside contains:

-  index.html
-  vue.css
-  Makefile
-  Dockerfile
-  package.json

The main index file has been built with HTML and JavaScript, using the Vue framework.

## Configuration

In order to run the client files locally for HTML viewing, run:

```bash
python3 -m http.server 8001
```

## Testing

In order to run the Cypress tests, run the following command:

```bash
make client_test
```

## Vue Installation

The Vue JavaScript is already included in the HTML file.

```bash
<script src="https://unpkg.com/vue@next"></script>
```

## Bootstrap Installation

The Bootstrap references are already included in the HTML file.

```bash
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
```

## Usage

This folder and its contents should be used for Cypress testing according to the Freecycle API spec.

## Authors and acknowledgment

Forked from the [Caladees Frameworks and Languages module Repo](https://github.com/calaldees/frameworks_and_languages_module).

## License
[MIT](https://choosealicense.com/licenses/mit/)