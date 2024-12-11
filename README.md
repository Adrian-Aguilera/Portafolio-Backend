# Portafolio-Backend

## Ejecutar local
 
Clonar el repositorio 
```bash
  git clone https://github.com/Adrian-Aguilera/Portafolio-Backend.git
```
Go to the project directory 

```bash
  cd /Portafolio-Backend
```


## Instalacion

Para poder instalar el proyecto, crearemos un .venv para instalar las dependencias

```bash
  python3 -m venv .venv
```
```bash
.venv\Scripts\activate
```
una vez instalado y corriendo la terminal del .venv, instalar las dependencias corriendo

```bash
  pip install -r requirements.txt
```

Crear migraciones del proyecto
```bash
  python manage.py makemigrations
  python manage.py migrate
```

Crear usuario administrador
```bash
  python manage.py createsuperuser
```

## Deployment

Ejecutar servidor local

```bash
  python manage.py runserver
```

##Informacion extra
Crear una aplicacion con django

```bash
  python manage.py startapp {name_app}
```

<hr>


## Instalacion de los temas para el panel admin de django (Opcional)
luego de hacer las migraciones instalar los temas de para django:

##### [Django](https://www.djangoproject.com/) theme (default): Run 

```bash
python manage.py loaddata admin_interface_theme_django.json
```
##### [Bootstrap](http://getbootstrap.com/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_bootstrap.json
```

##### [Foundation](http://foundation.zurb.com/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_foundation.json
```

##### [U.S. Web Design Standards](https://standards.usa.gov/) theme: Run 
```bash
python manage.py loaddata admin_interface_theme_uswds.json
```
