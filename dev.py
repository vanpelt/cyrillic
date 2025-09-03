#!/usr/bin/env uv run
# /// script
# dependencies = []
# ///

import http.server
import socketserver
import os
import sys

def main():
    port = int(os.environ.get('PORT', 8000))
    
    class Handler(http.server.SimpleHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, directory='.', **kwargs)

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Server running at http://localhost:{port}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"Port {port} is already in use. Try a different port.")
            sys.exit(1)
        else:
            raise

if __name__ == "__main__":
    main()