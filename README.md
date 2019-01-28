# matrix_to_image.py
Lo script **matrix_to_image.py** contiene la funzione **converter()** che trasforma matrici da file di testo ad immagini `.png`.

La funzione prende in input:
* **path:** che contiene il percorso della cartella che contiene il file da convertire;
* **file_name:** nome del file di testo da convertire;
* **extension:** estensione del file da convertire;
* **log:** se impostato su `'ON'` la funzione stamperà un messaggio con il path dove è stata salvata l'immagine e le sue dimensioni.

```
Immagine salvata alla posizione: /matrix_to_image_converter/test.png
L'immagine ha dimensione [h,w] = [1000, 48].
```

Il file **simple.py** contiene un esempio sull'utilizzo dello script

