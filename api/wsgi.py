import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from api import app


if __name__ == "__main__":
    app.run(debug=True)
