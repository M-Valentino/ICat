#!/bin/sh

while true; do
    read -p "Is your terminal font wide where this character, '▓' appears as a square? [y|n] " yn
    case $yn in
        [Yy]* ) echo "font_width: full" > icat_settings.cfg; break;;
        [Nn]* ) echo "terminal_width: half" > icat_settings.cfg; break;;
        * ) echo "Please enter 'y' or 'n'.";;
    esac
done

while true; do
    read -p "Is your terminal background light or dark? [l|d] " ld
    case $ld in
        [Ll]* ) echo "terminal_color: light" >> icat_settings.cfg; break;;
        [Dd]* ) echo "terminal_color: dark" >> icat_settings.cfg; break;;
        * ) echo "Please enter 'l' or 'd'.";;
    esac
done

sudo cp icat.py /usr/local/bin/ 
sudo cp icat /usr/local/bin/
sudo cp icat_settings.cfg /usr/local/bin/

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
FILE=/usr/local/bin/icat_settings.cfg
if test -f "$FILE"; then
    echo "✅\t$FILE installed."
else
    echo "❌\t$FILE could not be installed."
fi

echo "ℹ️\tMake sure the required Python packages are installed. They are listed in README.md"

export PATH=$PATH:/usr/local/bin/icat