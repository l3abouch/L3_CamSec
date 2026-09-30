#!/usr/bin/env python3

import argparse
import signal
import sys
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime
import json


PROJECT_DIR = Path(__file__).resolve().parent.parent
WEB_DIR = PROJECT_DIR / "web"
CAMERA_DIR = PROJECT_DIR / "logs" / "camera"

MAX_UPLOAD_SIZE = 100 * 1024 * 1024  # 100 MB


class CamSecHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print(f"[REQUEST] GET {self.path}")

        if self.path == "/" or self.path == "/index.html":
            self.serve_page(WEB_DIR / "index.html")
            return

        if self.path == "/continue.html":
            self.serve_page(WEB_DIR / "continue.html")
            return

        if self.path == "/favicon.ico":
            self.send_response(204)
            self.end_headers()
            return

        self.send_error(404, "Not Found")


    def do_POST(self):

        print(f"[REQUEST] POST {self.path}")

        if self.path != "/upload-image":
            self.send_error(404, "Not Found")
            return

        self.save_image()


    def serve_page(self, file_path):

        try:
            body = file_path.read_bytes()

        except OSError as exc:

            self.send_error(
                500,
                f"Could not read page: {exc}"
            )

            return

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "text/html; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(body))
        )

        self.send_header(
            "X-Content-Type-Options",
            "nosniff"
        )

        self.send_header(
            "X-Frame-Options",
            "DENY"
        )

        self.send_header(
            "Referrer-Policy",
            "no-referrer"
        )

        self.end_headers()

        self.wfile.write(body)


    def save_image(self):

        content_length = self.headers.get("Content-Length")

        if not content_length:

            self.send_json(
                400,
                {
                    "success": False,
                    "message": "Missing Content-Length."
                }
            )

            return


        try:

            content_length = int(content_length)

        except ValueError:

            self.send_json(
                400,
                {
                    "success": False,
                    "message": "Invalid Content-Length."
                }
            )

            return


        if content_length <= 0:

            self.send_json(
                400,
                {
                    "success": False,
                    "message": "Empty image."
                }
            )

            return


        if content_length > MAX_UPLOAD_SIZE:

            self.send_json(
                413,
                {
                    "success": False,
                    "message": "Image is too large."
                }
            )

            return


        try:

            image_data = self.rfile.read(
                content_length
            )

        except Exception as exc:

            print(
                f"[ERROR] Could not read image: {exc}"
            )

            self.send_json(
                500,
                {
                    "success": False,
                    "message": "Could not read image."
                }
            )

            return


        if not image_data:

            self.send_json(
                400,
                {
                    "success": False,
                    "message": "Received empty image."
                }
            )

            return


        CAMERA_DIR.mkdir(
            parents=True,
            exist_ok=True
        )


        timestamp = datetime.now().strftime(
            "%Y-%m-%d_%H-%M-%S"
        )


        filename = (
            f"photo_{timestamp}.jpg"
        )


        output_file = CAMERA_DIR / filename


        try:

            output_file.write_bytes(
                image_data
            )

        except OSError as exc:

            print(
                f"[ERROR] Could not save image: {exc}"
            )

            self.send_json(
                500,
                {
                    "success": False,
                    "message": "Could not save image."
                }
            )

            return


        size_kb = (
            len(image_data)
            / 1024
        )


        print()
        print("[+] Camera image received")
        print(f"[+] File: {output_file}")
        print(f"[+] Size: {size_kb:.2f} KB")
        print()


        self.send_json(
            200,
            {
                "success": True,
                "message": "Image saved successfully.",
                "filename": filename,
                "path": str(output_file),
                "size_kb": round(size_kb, 2)
            }
        )


    def send_json(self, status_code, data):

        body = json.dumps(data).encode(
            "utf-8"
        )


        self.send_response(status_code)

        self.send_header(
            "Content-Type",
            "application/json; charset=utf-8"
        )

        self.send_header(
            "Content-Length",
            str(len(body))
        )

        self.send_header(
            "Cache-Control",
            "no-store"
        )

        self.end_headers()

        self.wfile.write(body)


    def log_message(self, format, *args):
        return


def main():

    parser = argparse.ArgumentParser(
        description="L3_CamSec local security laboratory server"
    )


    parser.add_argument(
        "--host",
        default="127.0.0.1"
    )


    parser.add_argument(
        "--port",
        type=int,
        default=8080
    )


    args = parser.parse_args()


    WEB_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    CAMERA_DIR.mkdir(
        parents=True,
        exist_ok=True
    )


    index_file = WEB_DIR / "index.html"


    if not index_file.is_file():

        print(
            f"[!] Web interface not found: {index_file}",
            file=sys.stderr
        )

        return 1


    server = HTTPServer(
        (args.host, args.port),
        CamSecHandler
    )


    def shutdown_handler(signum, frame):

        print(
            "\n[+] Shutting down L3_CamSec server..."
        )

        server.server_close()

        sys.exit(0)


    signal.signal(
        signal.SIGINT,
        shutdown_handler
    )

    signal.signal(
        signal.SIGTERM,
        shutdown_handler
    )


    print()
    print("[+] L3_CamSec server started")
    print(f"[+] Address: http://{args.host}:{args.port}")
    print(f"[+] Web interface: {WEB_DIR}")
    print(f"[+] Camera images: {CAMERA_DIR}")
    print("[+] Press Ctrl+C to stop")
    print()


    try:

        server.serve_forever()

    finally:

        server.server_close()


if __name__ == "__main__":

    sys.exit(main())
