# actions-project

Using Github Actions, when an `XML` file carrying a key-value pair is edited so that the key is changed, `main.txt` is edited so that it reflects the new key. This was done using YAML and Python.


# How it works
The Python code is in the `.github/workflows/` folder along with the `main.yml` file.

When a push to the repo happens, it is possible that the `data.xml` file has been edited. YAML sends a call to Python, and that Python file (`app.py`) checks if the XML file has been changed. Then, the current XML file with the current commit's SHA hash is uploaded to `history.json` as a key-value pair. This is what is used to compare the latest version with the current version of the XML.

# Usage
Clone the repository (`git clone https://github.com/adithraghavs/actions-project.git`), open the folder in your favourite text editor, change the XML file, stage, commit, and push.

You can also just change the XML file and then run `python3 .github/workflows/app.py` to see it happen on your local.
