import functools
import http.server
from pathlib import Path
import threading
import unittest
import urllib.request

ROOT = Path(__file__).resolve().parents[1]

class SmokeTest(unittest.TestCase):
    def test_static_http_routes(self):
        self.assertTrue((ROOT / 'site' / 'index.html').is_file(), 'static homepage missing')
        handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / 'site'))
        server = http.server.ThreadingHTTPServer(('127.0.0.1', 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            for path, marker in [('/', 'RBDEZIGNZ staging smoke test'), ('/health', 'ok')]:
                with urllib.request.urlopen(f'http://127.0.0.1:{server.server_port}{path}', timeout=5) as response:
                    self.assertEqual(response.status, 200)
                    self.assertIn(marker, response.read().decode())
        finally:
            server.shutdown()
            server.server_close()
            thread.join()

if __name__ == '__main__':
    unittest.main()
