wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1QeSXSE88AaMta7V123qVpO6H43DNywaX' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1QeSXSE88AaMta7V123qVpO6H43DNywaX" -O checkpoint.zip && rm -rf /tmp/cookies.txt
pip install gpt-2-simple
pip install Pillow==2.2.1
pip install asciimatics 
pip install pyfiglet
pip install colorama
pip install fitz
pip install PyMuPDF
pip install ebooklib
pip install BeautifulSoup4
pip install flask_ngrok