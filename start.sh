source venv/bin/activate

# Make tmp/
tmppath="tmp/"

if [ ! -d "$tmppath" ]; then
    mkdir -p "$tmppath"
    echo "Folder created: $tmppath"
else
    echo "Folder already exists: $tmppath"
fi

export FLASK_APP="server.py"

flask run -p 8738