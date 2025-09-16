# Hadoop

Para trabajar con los ejemplos de esta carpeta, es necesario instalar la librería `mrjob`, que permite ejecutar trabajos de MapReduce en Hadoop y en local desde Python.

Se recomienda utilizar un entorno virtual para instalar la librería:

```bash
python -m venv mrjob-env
source mrjob-env/bin/activate
pip install -r requirements.txt
```

Los ejemplos pueden ejecutarse en local o en un clúster Hadoop. Para ejecutar en local, simplemente se puede usar:

```bash
cd WordCount
python MRWordCount.py -r inline data.txt
```

```bash
cd WordCount
python MRWordFrequencyCount.py -r inline data.txt
```

```bash
cd WordCount
python MRMostUsedWord.py -r inline data.txt
``` 



