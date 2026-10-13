# Trabajando con Spark

Si utilizamos Databricks, no es necesario instalar nada en local, ya que Databricks nos proporciona un entorno de trabajo con Spark preconfigurado. Sin embargo, si queremos trabajar con Spark en local, necesitaremos instalar algunas dependencias.

Para trabajar con Spark en local, lo mejor es que nos creemos un entorno virtual de Python.

```bash
$ python -m venv spark-env
```

Si no tenemos instalada la libreria de entornos virtuales, la instalamos con el siguiente comando.

```bash
$ pip install virtualenv
```

Activamos el entorno virtual

```bash
$ source spark-env/bin/activate
```

Instalamos las dependencias necesarias (puede tomar unos minutos)

```bash
$ pip install -r requirements.txt
```

Lanzamos Jupyter Lab

```bash
$ jupyter lab
```