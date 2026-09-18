---
name: dashboard
description: Publica o actualiza un tablero visual (Artifact HTML) del progreso de estudio de Estado Sólido, leyendo progreso/progreso.md como única fuente de verdad.
---

# /dashboard — tablero visual de progreso

## Pasos

1. Lee `progreso/progreso.md` completo.
2. Antes de escribir el HTML, invoca el skill `artifact-design` para
   calibrar el nivel de diseño, y `dataviz` si vas a incluir gráficos de
   avance (ej. barra de % dominado) — este es un tablero simple, no hace
   falta sobre-diseñarlo.
3. Construye una página con:
   - Checklist de subtemas agrupados por archivo de `notas/` (mismo orden
     que `progreso.md`), cada uno con su estado (color: gris=no visto,
     amarillo=en progreso, verde=dominado).
   - % global de avance (dominados / total subtemas).
   - Lista de debilidades vigentes (de subtemas `en progreso` o recién
     evaluados), agrupadas por subtema.
   - Fecha de la última evaluación de cada subtema dominado.
4. Publica con la herramienta Artifact:
   - Si `progreso.md` ya tiene una URL de dashboard guardada, primero
     **léela** (`action: "read"`) y luego publica sobre esa misma `url`
     para actualizarla (no crear una nueva).
   - Si no existe URL guardada, publícala como nueva y guarda la URL
     resultante en `progreso/progreso.md`.
5. Entrega al usuario el enlace del artifact publicado.

## No hacer

- No inventes datos de progreso que no estén en `progreso.md`.
- No crees un artifact nuevo si ya existe uno — actualízalo (evita
  fragmentar el progreso en varios links).
