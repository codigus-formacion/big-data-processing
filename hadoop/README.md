# Hadoop

Para trabajar con los ejemplos de esta carpeta, es necesario instalar la librería `mrjob`, que permite ejecutar trabajos de MapReduce en Hadoop y en local desde Python.

Se recomienda utilizar un entorno virtual para instalar la librería:

``` bash
python -m venv mrjob-env
source mrjob-env/bin/activate
pip install -r requirements.txt
```

Si no tenemos `venv` instalado, debemos ejecutar antes el siguiente comando:

```         
pip install virtualenv
```

Los ejemplos pueden ejecutarse en local o en un clúster Hadoop. Para ejecutar en local, simplemente se puede usar los siguientes comandos:

# Ejemplos WordCount

``` bash
cd WordCount
python MRWordCount.py data.txt
```

``` bash
cd WordCount
python MRWordFrequencyCount.py data.txt
```

``` bash
cd WordCount
python MRMostUsedWord.py data.txt
```

## Ejemplos Football

``` bash
cd Football
python MRMostEfficientPlayers.py players.csv
```

``` bash
cd Football
python MRTeamStatistics.py players.csv
```