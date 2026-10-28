---
name: duda
description: Responde una duda puntual de Estado Sólido (Parcial 1 o Parcial 2) usando las notas ya extraídas del PDF (nunca relee el PDF completo), cita la página fuente y actualiza el progreso del subtema tocado en el perfil activo (Isa o Juan).
---

# /duda — resolver una duda puntual

Argumento: la pregunta del usuario (texto libre), ej. `/duda por qué la rama
óptica tiene ω finita en q=0`.

## Pasos

0. **Parcial activo.** Hay dos bloques: `Parcial_1/` (vibraciones de red) y
   `Parcial_2/` (metales y electrón libre). Deduce el parcial por el tema de la
   pregunta o de la sesión; si es ambiguo, pregunta "¿Parcial 1 o Parcial 2?".
   Define `BASE=Parcial_N/` y úsalo como prefijo de **todas** las rutas de
   abajo (`BASE/notas/`, `BASE/progreso/`, `BASE/examenes/`). Cada parcial tiene
   su propio `CLAUDE.md` con sus reglas y fuentes.
1. **No leas el PDF.** Busca primero en `BASE/notas/*.md` (usa Grep/búsqueda por
   palabras clave del tema) el o los archivos relevantes a la pregunta.
2. Lee solo esos archivos (no todos los de `notas/`) para tener el contexto
   exacto: definiciones, ecuaciones, derivaciones y el `[p. N]` de respaldo.
3. Responde de forma **breve y concreta** — esto es una duda puntual, no una
   clase. Da la explicación mínima suficiente para resolver la confusión,
   con la ecuación relevante si aplica, y cita la página del PDF entre
   corchetes (`[p. N]`) para que el usuario pueda revisar la diapositiva
   original si quiere más detalle o el diagrama.
4. Si la pregunta involucra deducir algo, muestra los pasos clave pero sin
   relleno.
5. Si las notas **no cubren** la pregunta (vacío real, no solo falta de
   memoria del asistente): dilo explícitamente al usuario. Solo entonces,
   como excepción, ofrece leer esa sección puntual del PDF (pocas páginas,
   no el documento completo) para completar la nota — y si el usuario
   confirma, actualiza el archivo de `BASE/notas/` correspondiente con lo
   encontrado para que quede disponible en el futuro sin volver a leer el
   PDF.
6. **La explicación va en el MENSAJE FINAL, después de todas las
   herramientas.** La interfaz del usuario colapsa en una línea resumen el
   texto que se escribe antes de una llamada a herramienta, así que una
   explicación puesta ahí no se ve. Orden obligatorio: (a) leer notas,
   (b) actualizar el progreso si corresponde (paso 7), (c) escribir como
   último mensaje, sin herramientas después, la explicación completa de los
   pasos 3-4. Nunca escribas la explicación antes de una herramienta.
7. Actualiza el progreso **antes** del mensaje final. Si no sabes ya en esta
   sesión qué perfil está activo (Isa o Juan), no lo adivines: termina el
   mensaje final con la explicación completa y la pregunta "¿Isa o Juan?", y
   actualiza el progreso en el turno siguiente. Actualiza
   `BASE/progreso/<persona>.md`: si el subtema tocado está marcado `no visto`,
   cámbialo a `en progreso` (no toques el estado si ya está `en progreso` o
   `dominado` — una duda puntual no rebaja un tema dominado).
8. El mensaje final termina con una sola línea que diga qué subtema se
   marcó (o que no hubo cambios). Esa línea va después de la explicación,
   nunca en su lugar.

## No hacer

- No escribas la explicación antes de una llamada a herramienta ni la
  sustituyas por un resumen de una línea o por el aviso de que actualizas el
  progreso.
- No generes un resumen completo del tema si no te lo piden — responde la
  pregunta puntual.
- No marques un tema como `dominado` desde `/duda` — eso solo lo hace
  `/evaluar`.
- No regeneres el dashboard automáticamente desde aquí.
- No toques `BASE/progreso/<otra-persona>.md` — solo el perfil activo de la
  sesión, ni el progreso del otro parcial.
