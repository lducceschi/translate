# Esercizi

Su [questo repository Github](https://github.com/UniversalDependencies/UD_Italian-ParTUT) è possibile trovare vari files derivanti dal processamento di un corpus dell'italiano. A noi interessa utilizzare un file di tipo *conllu*, che rappresenta per ogni riga una parola, ovvero un token per riga. Nonostante l'estensione del file poco comune, si tratta di un banale file di tipo *.csv*, cioè un file leggibile sia con un editor di testo qualsiasi (come Notepad++ o TextMate), sia con Excel.

## Esercizio 1

  - Utilizzare `requests` per ottenere dal repository la stringa (ovvero il testo) corrispondente a [questa url](https://raw.githubusercontent.com/UniversalDependencies/UD_Italian-ParTUT/master/it_partut-ud-train.conllu)
  - Definire una funzione che prenderà tale stringa in input e restituirà in output un dizionario in cui le chiavi saranno un indice numerico intero a partire da 1 (1,2,3,4,etc.) e i valori le frasi che compaiono nel testo e che iniziano per #text. Per intenderci, la prima di queste è:
    - `# text = La distribuzione di questo modello di contratto di licenza non instaura un rapporto avvocato-cliente.`

