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
   (b) actualizar el avance y/o anotar un pendiente (paso 7 y sección Pendientes), (c) escribir como
   último mensaje, sin herramientas después, la explicación completa de los
   pasos 3-4. Nunca escribas la explicación antes de una herramienta.
7. **Avance automático (solo Parcial 2, solo hacia adelante).** El avance de checklists vive en la `db` del tablero de la persona (URL en `BASE/progreso/<persona>.md`, línea `Dashboard URL`). Si no sabes el perfil, no lo adivines: termina la explicación con "¿Isa o Juan?" y aplica el cambio en el turno siguiente. Pasos:
   a. Identifica los ítems de **teoría** (`T.<subtema>.<n>`, en `Parcial_2/teoria/*.md`) que la duda toca de verdad; no todo el subtema. Si ninguno encaja claramente, no cambies nada.
   b. Lee la colección `items` con `ArtifactData` (`list`); doc id = ID con `.`→`_`; campo `s` ∈ `pendiente | en progreso | hecho`.
   c. Regla: si el ítem está `pendiente` (o no existe) pásalo a `en progreso`; si ya está `en progreso` o `hecho`, **déjalo igual** (nunca bajes un estado). Escribe `{"id":"<ID>","s":"en progreso","ts":<ms>}` con `set` (si existe, pasa `if_version` del doc leído para no pisar un clic simultáneo; si falla por versión, relee y reevalúa).
   d. El usuario puede seguir cambiando el estado a mano en el tablero o con `/dashboard <persona> marcar ...`; ambas vías escriben en la misma base y se ven al instante. `/duda` nunca marca `hecho`.
8. El mensaje final termina con una línea: qué ítems pasó a `en progreso` (o "sin cambios en el progreso").

## Pendientes (Parcial 2)

Si la duda deja algo abierto (el usuario sigue sin entender, hay que repasar un prerrequisito, o detectas un error/vacío en las notas o la teoría), añade una fila en la sección "Pendientes y por mejorar" de `BASE/progreso/<persona>.md` (entre `PENDIENTES:START` y `PENDIENTES:END`): `| n | AAAA-MM-DD | subtema | duda/repasar/error-material/mejora | descripción concreta | abierto |`. Si una duda anterior queda resuelta, cambia su estado a `resuelto`. No anotes dudas ya resueltas del todo. Si el error está en el material, corrígelo también en `teoria/`, `practica/` o `notas/`.

## No hacer

- No escribas la explicación antes de una llamada a herramienta ni la
  sustituyas por un resumen de una línea o por el aviso de que actualizas el
  progreso.
- No generes un resumen completo del tema si no te lo piden — responde la
  pregunta puntual.
- No marques `hecho` ni bajes un estado desde `/duda`: solo `pendiente`→`en progreso`.
- No regeneres el dashboard automáticamente desde aquí.
- No toques `BASE/progreso/<otra-persona>.md` — solo el perfil activo de la
  sesión, ni el progreso del otro parcial.

## Alcance Parcial 2

En `Parcial_2/` el parcial llega solo hasta la p. 70. Si la duda es de un subtema `fuera de alcance` (ver `progreso/<persona>.md`), respóndela pero avisa que no entra en el parcial y no cambies su estado.

En `Parcial_2`, además de `[p. N]` de las diapositivas, cita la sección del Pavlov (`notas/08_mapa_pavlov.md`) cuando el subtema aparezca en el libro; no releas el libro.
