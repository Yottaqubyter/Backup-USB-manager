# USB Backup

Este es un microprograma que hace copias de seguridad de los USB que hayas configurados. Las copias de seguridad se encuentran en `%HOMEDRIVE%%HOMEPATH%\USB-backup`. (`USB-backup` en el directorio del usuario)

---



## Como hacer la copia

### USBackup.txt

Debes crear un archivo de texto en el USB llamado `USBackup.txt`. Debes escribir dentro el nombre de la carpeta de la copia de seguridad (si el nombre es incorrecto, al intentar hacer la copia de seguridad, el programa te lo dirá).

### .USBignore

También debes crear un archivo de nombre `.USBignore`. En el archivo incluirás una lista de archivos o directorios que ignorar. Aquí incluyo como ejemplo un `.USBignore` que se ignora a si mismo, a USBackup.txt y a una carpeta de la versión portable de codeblocks:

```
\codeblocks-16.01mingw-nosetup\
\USBack.txt
\.USBignore
```

Cabe notar que para ignorar una carpeta es recomendable (Aunque no necesario) colocar otra `\` al final.

Esta parte del programa no comprueba si hay errores, así que hay que tener cuidado con lo escrito o la copia de seguridad no se hará bien (No será muy problemático por lo simple que es, pero mejor prevenir que curar).

---



## Inicio del programa

Al iniciar el programa, este se instalara en tu ordenador para iniciarse al encender el ordenador. Habrá una ventana abierta que te informa de los USB que ha detectado para hacer una copia de seguridad.

<img src="BACK_SUCCESSFUL.PNG" alt="a" style="zoom:60%;" />

