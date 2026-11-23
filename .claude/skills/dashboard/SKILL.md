---
name: dashboard
description: Publica o actualiza un tablero visual (Artifact HTML) del progreso de estudio de Estado Sólido de un perfil (Isa o Juan) en un parcial (Parcial 1 o Parcial 2), leyendo Parcial_N/progreso/<persona>.md como única fuente de verdad para ese perfil y parcial.
---

# /dashboard — tablero visual de progreso

Argumentos opcionales: el perfil y el parcial (`/dashboard juan p2`,
`/dashboard isa p1`). Si no se dan y no se saben ya en la sesión, pregunta
"¿Isa o Juan?" y "¿Parcial 1 o Parcial 2?" antes de seguir. Define
`BASE=Parcial_N/` y úsalo como prefijo de las rutas (`BASE/progreso/`,
`BASE/notas/`). Hay un dashboard (y una URL) por cada pareja (parcial, persona).

## Pasos

1. Lee `BASE/progreso/<persona>.md` completo (nunca
   `Parcial_1/progreso/progreso.legacy.md`, que está deprecado, ni el archivo de
   la otra persona ni el del otro parcial).
2. Antes de escribir el HTML, invoca el skill `artifact-design` para
   calibrar el nivel de diseño, y `dataviz` si vas a incluir gráficos de
   avance (ej. barra de % dominado) — este es un tablero simple, no hace
   falta sobre-diseñarlo.
3. Construye una página con:
   - Checklist de subtemas agrupados por archivo de `BASE/notas/` (mismo orden
     que `BASE/progreso/<persona>.md`), cada uno con su estado (color: gris=no
     visto, amarillo=en progreso, verde=dominado).
   - % global de avance (dominados / total subtemas).
   - Lista de debilidades vigentes (de subtemas `en progreso` o recién
     evaluados), agrupadas por subtema.
   - Fecha de la última evaluación de cada subtema dominado.
   - Tabla de "Parciales y talleres" (de la sección del mismo nombre en
     `BASE/progreso/<persona>.md`): estado/nota/fecha por examen viejo intentado.
   - El nombre del perfil y del parcial ("Progreso P1 de Juan", "Progreso P2
     de Isa", …) visible en el título del tablero.
4. Publica con la herramienta Artifact:
   - Si `BASE/progreso/<persona>.md` ya tiene una URL de dashboard guardada,
     primero **léela** (`action: "read"`) y luego publica sobre esa misma
     `url` para actualizarla (no crear una nueva).
   - Si no existe URL guardada, publícala como nueva y guarda la URL
     resultante en `BASE/progreso/<persona>.md`.
5. Entrega al usuario el enlace del artifact publicado.

## No hacer

- No inventes datos de progreso que no estén en `BASE/progreso/<persona>.md`.
- No crees un artifact nuevo si ya existe uno — actualízalo (evita
  fragmentar el progreso en varios links).
- No publiques ni modifiques el dashboard de la otra persona ni el del otro
  parcial sin que se pida explícitamente — cada (parcial, perfil) tiene su
  propio artifact y su propia URL, y no se tocan entre sí.

## Alcance Parcial 2

En `Parcial_2/` el % global = dominados / subtemas **en alcance** (12). Los `fuera de alcance` se muestran aparte, en gris atenuado con etiqueta "fuera del parcial (p. >70)", y no cuentan en el %. Indica en el título/subtítulo "Alcance: diapositivas 1-70".


## Parcial 2: tablero interactivo (desde 2026-11-22)

El tablero de `Parcial_2/` contiene TODO el contenido (teoría con imágenes, práctica, examen con cajas de respuesta, exámenes viejos) y guarda el avance en la `db` del propio artifact (colecciones `items`, `answers`, `grades`; `grades` solo la escribe un Editor/owner, o sea Claude vía ArtifactData).

1. `python3 .claude/skills/dashboard/build_site.py <dir_scratchpad>/site` genera `dash_juan.html`, `dash_isa.html`, copia los `.md`/imágenes y `_files.txt`.
2. Publica cada HTML con Artifact sobre la URL guardada (`root` = el dir, `files` = rutas de `_files.txt`, `capabilities: {db:{rules:[{path:"grades",read:"view",write:"admin"}]}}`). Título estable "Progreso P2 de <Nombre>".
3. Calificar: leer `answers` (doc id = ID con `.`→`_`, campo `text`) y escribir en `grades` `{id, score, fb, ts}`; `score` ≤ puntos del literal (puntos de la pregunta / nº de literales).
4. La pestaña **Pendientes** sale de la sección `PENDIENTES:START/END` de `Parcial_2/progreso/<persona>.md` (la lee `build_site.py` al generar): tras cambiarla hay que regenerar y republicar. El avance sale de la `db` (no de `progreso/*.md`); para dejarlo en el repo, listar `items` y volcarlo al md si el usuario lo pide.

## Marcar avance desde el comando (`/dashboard <persona> ...`)

Además del clic en el tablero, el avance se puede mover con el comando. Formas (el perfil es obligatorio; si falta, preguntar "¿Isa o Juan?"):

- `/dashboard juan marcar T.drude.1.1 hecho`: un ítem.
- `/dashboard juan marcar T.drude hecho`: todo ítem cuyo ID empiece por ese prefijo (`T.` teoría, `P.` práctica, `V.` exámenes viejos; ej. `T.cal`, `P.fermi3d.1`, `V.P2501`).
- `/dashboard juan marcar teoria en progreso`: toda la sección (`teoria`, `practica`, `viejos`).
- `/dashboard juan reiniciar practica`: vuelve a `pendiente`.
- `/dashboard juan calificar examen`: lee `answers`, califica y escribe `grades` (ver abajo).

Cómo se ejecuta: (1) listar los IDs con `grep -hoE '^- \[ \] \S+' Parcial_2/{teoria,practica,examenes_resueltos}/*.md`, filtrando por prefijo; (2) con `ArtifactData` `batch` (máx. 50 por llamada) escribir en la colección `items` un doc por ID: `doc_id` = ID con `.`→`_`, `data` = `{"id": "<ID>", "s": "<pendiente|en progreso|hecho>", "ts": <ms>}` (`set`; si existe, `update` con `if_version`); (3) confirmar al usuario cuántos ítems cambió. Nunca tocar el artifact de la otra persona.

### Calificar el examen
Opción múltiple (50 preguntas, 0.1 c/u, total 5.0): leer `answers` (campo `text` = letra) y la clave en el tablero **de Juan** (`key/mc`, cadena `n:letra,...`, solo admin; nunca se guarda en el tablero de Isa porque, al estar compartido, un Editor podría leerla); escribir en `grades` (doc_id `EX_M_n`) `{"id":"EX.M.n","score":0.1 o 0,"fb":"clave: c — por qué"}`. Al final, resumir la nota por parte.
