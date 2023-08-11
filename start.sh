cd veb # Legitimately I have never wrote a bash script in my life until now
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
