# Prueba técnica PyE — módulos

Este repo es tu espacio de trabajo durante la prueba.

```
pye_sale_extras/    módulo existente del cliente (Parte A)
```

La Parte B la desarrollas como un módulo nuevo dentro de este mismo repo.

## Cómo empezar

Con el entorno Docker de PyE:

```bash
git clone <esta-url> addons/prueba
docker compose restart odoo
docker compose run --rm odoo odoo -d prueba -i pye_sale_extras --stop-after-init --no-http
docker compose restart odoo
```

Con tu propio entorno: clona este repo donde prefieras, agrega esa carpeta a tu `addons_path`
e instala `pye_sale_extras`.

## Cómo entregar

Haz un commit por ticket y uno por nivel, en este repo, con un mensaje que explique qué cambiaste
y por qué. No hace falta hacer push: revisamos el repo en tu laptop al terminar.
