# Bank Data DevOps Lab

Proyecto práctico de extremo a extremo para un rol DevOps Developer con:

- GitHub y GitHub Actions
- Python y pruebas unitarias
- Azure Data Factory
- Azure Databricks y PySpark
- Arquitectura Bronze, Silver y Gold
- CI/CD, configuración y buenas prácticas

## Primera ejecución local

### 1. Crear entorno virtual

```bash
python -m venv .venv
```

### 2. Activar entorno

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 4. Ejecutar validaciones

```bash
ruff check .
pytest -q
```

## Flujo Git

```text
main
  └── feature/inicializar-proyecto
```

Crear rama:

```bash
git checkout -b feature/inicializar-proyecto
```

## Próximos pasos

1. Subir el repositorio a GitHub.
2. Proteger la rama `main`.
3. Abrir un pull request.
4. Confirmar que GitHub Actions ejecuta lint y pruebas.
5. Crear los recursos mínimos en Azure.
