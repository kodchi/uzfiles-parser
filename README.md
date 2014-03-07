uzfiles-parser
==============

Extract music links (by artist) from uzfiles.com

How to install
---
> pip install -r requirements.txt

How to use
---
- Visit http://uzfiles.com/mp3.php?letter=A&lang=Uzbek&op
- Click on any arist. For example, click on 'Y' and then 'Yulduz Usmanova'
- Copy the URL: http://uzfiles.com/mp3.php?artist=Yulduz%20Usmanova&lang=Uzbek&letter=Y
- Make note of the number of pages, which is 22
- run the script by passing the ulr and number of pages:
> parser http://uzfiles.com/mp3.php?artist=Yulduz%20Usmanova&lang=Uzbek&letter=Y 22
- Once done, the script will create an html file in the same dir as the script file. Open that file to see direct links to Yulduz Usmanova's songs.
