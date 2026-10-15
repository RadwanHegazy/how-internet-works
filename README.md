# Building the internet

**Building the internet** is a small educational project that simulates part of
how the web works. A custom browser looks up a domain using a simple DNS server,
then connects to the web server associated with that domain and displays its
response.

This is a local simulation for educational purposes only. It does not connect
to or resolve real internet websites.

To Watch the video on youtube [click here](https://youtu.be/RUMT98RRLb8)

## Services

| Service | Purpose | Host port |
| --- | --- | --- |
| `dns` | Resolves the simulated domains over UDP | `5000/udp` |
| `google` | Serves the simulated Google page | `8000/tcp` |
| `facebook` | Serves the simulated Facebook page | `8001/tcp` |

The DNS records for `google.com` and `facebook.com` both resolve to
`127.0.0.1`. The browser uses the domain to choose the matching web-server
port.

## Requirements

- Docker with the Docker Compose plugin
- Python 3 to run `browser.py` on your host machine
- `PyQt5` and `PyQtWebEngine` to run the browser on your host machine

## Run

Install the dependencies needed to run the browser:

```sh
python -m pip install PyQt5 PyQtWebEngine
```

From the project directory, start the DNS and web servers:

```sh
docker compose up --build
```

Leave this running, then open a second terminal and start the custom browser:

```sh
python browser.py
```

Enter `google.com` or `facebook.com` in the browser's address field. You can
also try a page path, such as `google.com/test`.

Stop the containers with `Ctrl+C`, or run this from the project directory:

```sh
docker compose down
```

The host ports `5000/udp`, `8000/tcp`, and `8001/tcp` must be available while
the containers are running.
