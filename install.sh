#!/bin/sh
sudo cp icat.py /usr/local/bin/ 
sudo cp icat /usr/local/bin/

FILE=/usr/local/bin/icat.py
if test -f "$FILE"; then
    echo "✅\t$FILE installed."
else
    echo "❌\t$FILE could not be installed."
fi
FILE=/usr/local/bin/icat
if test -f "$FILE"; then
    echo "✅\t$FILE installed."
else
    echo "❌\t$FILE could not be installed."
fi

echo "ℹ️\tMake sure the required Python packages are installed. They are listed in README.md"

export PATH=$PATH:/usr/local/bin/icat