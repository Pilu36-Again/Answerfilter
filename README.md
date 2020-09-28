# Answerfilter
This script is a solution to search for strings among all responses after a questionnaire is filled/closed and the DB (a .csv file) is available. There is a simple, however yet not solved task: define those respondents who mentioned a specific string anywhere among their answers. So filter for these respondents and make a list about these. 

To be translated: 
"""Ez a script a kovetkezo celbol keszult: 
Amikor valaszok vannak egy tablaban, es azt szeretnénk tudni, hogy:
- egy bizonyos választ ki adott.
- A válaszokon belül is előfordulhatnak vesszők és az egyes kérdések válaszai is vesszővel elválasztottak. 
Tábla előkészítése: 
- Ez a srcipt Ubuntu-n így futtatható: $ python Respfilter_multiple_str_write.py
- Ez a script és az inputként használt file is ugyanabban a mappában legyen.
- A válaszadó neve az utolsó oszlopban legyen. 
Eredmények: 
- A Terminal-os is láthatók
- De különben egy hónap-nap-óra-perc-másodperc nevü .txt file-ba is kiexportálja, abba a könyvtárba, ahol futtatunk.
.csv-re és .txt-re is működik.

"""
