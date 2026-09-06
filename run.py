import sys
import os

# Set working directory and path to cyberarenasecurity package
base_dir = os.path.dirname(os.path.abspath(__file__))
pkg_dir = os.path.join(base_dir, "cyberarenasecurity")
if os.path.exists(pkg_dir):
    sys.path.insert(0, pkg_dir)
    os.chdir(pkg_dir)

from main import main

if __name__ == "__main__":
    main()
