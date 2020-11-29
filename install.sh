wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1-C8AfjQVJIS5xMgzo4tx0miFfof8PPVa' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1-C8AfjQVJIS5xMgzo4tx0miFfof8PPVa" -O models.zip && rm -rf /tmp/cookies.txt
unzip models.zip
pip install gpt-2-simple
pip install Pillow==2.2.1
pip install asciimatics 
pip install pyfiglet
pip install colorama