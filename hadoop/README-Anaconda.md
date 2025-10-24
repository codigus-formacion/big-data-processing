# Hadoop

Para trabajar con los ejemplos de esta carpeta, es necesario instalar la librería `mrjob`, que permite ejecutar trabajos de MapReduce en Hadoop y en local desde Python. Para poder utilizar dicha librería, es necesario utilizar la versión de **Python 3.12**.

## Instalación del entorno

Para trabajar con los ejemplos, primero debes crear un entorno virtual usando **Anaconda**.

1. Abre una terminal de **Anaconda Prompt**.  
2. Ejecuta el siguiente comando para crear un entorno con Python 3.12:


```bash
conda create -n mrjob-env python=3.12
```

3. Conecta Positron al entorno recién creado llamado mrjob-env.
4. La primera vez que abras el proyecto, instala las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

## Ejecución de los ejemplos

Los ejemplos pueden ejecutarse en local o en un clúster Hadoop. Para ejecutar en local, simplemente se puede usar los siguientes comandos:

### Ejemplos WordCount

```bash
cd WordCount
python MRWordCount.py data.txt
```

```bash
cd WordCount
python MRWordFrequencyCount.py data.txt
```

```bash
cd WordCount
python MRMostUsedWord.py data.txt
``` 

### Ejemplos Football

```bash
cd Football
python MRMostEfficientPlayers.py players.csv
```

```bash
cd Football
python MRTeamStatistics.py players.csv
```