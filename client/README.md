# Client

This is the Client Side folder. Inside contains:

-  index.html
-  vue.css
-  Makefile
-  Dockerfile

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

## Usage

This folder and its contents should be used for Cypress testing according to the Freecycle API spec.

## Authors and acknowledgment

Forked from the [Caladees Frameworks and Languages module Repo](https://github.com/calaldees/frameworks_and_languages_module).

## License
[MIT](https://choosealicense.com/licenses/mit/)