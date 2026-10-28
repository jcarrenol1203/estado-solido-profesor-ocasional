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
