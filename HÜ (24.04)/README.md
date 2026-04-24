Zeichenketten werden in 2 verschieden Apostrophe gestellt
'abc'
"abc"
beides ist gleich


Soll die Zeichenkette über mehrere Zeilen reichen, müssen dreifache Apostrophe verwendet werden
'''
"""
z.b. """abc
            abc 
                abc"""

Lehrzeichen können bei der Zk vermieden werden, sollte man aber nicht weil die ganze optische Struktur grauenhaft aussieht
if True:
    S = """Das ist eine lange Zeichenkette."""
    print(s)


## Zeichenkette aufeinanderfügen oder vervielfältigen

ZK aufeinanderfügen = Operator+


## Sonderzeichen
s.82
\a
\f
\n
\n
\unnnn
\'
\"
\\

## Raw Zeichenkette

Eine Raw-Zeichenkette in Python sorgt dafür, dass Sonderzeichen wie \n oder \t nicht als Escape-Sequenzen(spezielle Zeichenkombinationen mit einem Backslash)(\) 
interpretiert, sondern genau so als Text übernommen werden.

zb: r'\'

## chr
diese Funktion liefert ein Zeichen, das dem übergebebnden ASCII-Code bzq Unicode entspricht

zb:     chr(67)     # 'A'

## ord
EIne Umkehrfunktion liefert den ASCII/UNICODE einzelne Zeichen

ord('A')    # 65


## Zusätzliche Funktionen/ Zeichen

