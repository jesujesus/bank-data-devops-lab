# Arquitectura inicial

```text
CSV ficticio
   |
   v
Azure Data Factory
   |
   v
Azure Data Lake Storage
   |
   v
Azure Databricks
   |
   +--> Bronze: dato original
   +--> Silver: dato limpio y validado
   +--> Gold: métricas agregadas
```

## Principios

- Nada de credenciales dentro del código.
- Configuración separada por ambiente.
- Código reusable fuera de los notebooks.
- Pruebas automáticas antes de fusionar a `main`.
- Datos completamente ficticios.
