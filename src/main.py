"""Main function to run."""
import autodynatrace
import sys
import uvicorn
from app import app
def main() -> int:
    """Entry function.

    :return: zero on sucecssful exit.
    """
    uvicorn.run(app=app, host="0.0.0.0", port=20080)
    return 0


if __name__ == "__main__":
    sys.exit(main())
