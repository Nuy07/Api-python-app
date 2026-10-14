# App FakeStore API

Monorepo de la aplicación móvil Expo y su API FastAPI:

- `mi-app/`: cliente móvil y web.
- `api-python/`: API de catálogo, usuarios, carritos y autenticación.

## Requisitos

- Node.js y npm.
- Python 3.10 o posterior.

## Ejecutar la API

Desde la raíz del repositorio, en PowerShell:

```powershell
cd api-python
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

La documentación interactiva de la API estará disponible en
<http://localhost:8000/docs>.

## Ejecutar la app

Abre otra terminal en la raíz del repositorio:

```powershell
cd mi-app
npm install
npm run start
```

La app detecta la dirección del servidor Expo y usa el puerto `8000` para
conectarse a la API. Si necesitas indicar otra dirección, configura
`EXPO_PUBLIC_API_URL` antes de iniciar Expo, por ejemplo:

```powershell
$env:EXPO_PUBLIC_API_URL = "http://192.168.1.25:8000"
npm run start
```

En un teléfono físico, usa la dirección IP local de la computadora que ejecuta
la API; `localhost` en el teléfono se refiere al propio teléfono. Ambos equipos
deben estar en la misma red.

## Datos de demostración

La API guarda productos, usuarios y carritos en memoria; los cambios hechos
mediante el CRUD de productos se pierden al reiniciar el servidor. Las cuentas
incluidas en `api-python/main.py` son solo para desarrollo y demostración. No
uses esas credenciales ni esta autenticación de ejemplo en producción.
