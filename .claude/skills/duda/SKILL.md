---
name: duda
description: Responde una duda puntual de Estado Sólido usando las notas ya extraídas del PDF (nunca relee el PDF completo), cita la página fuente y actualiza el progreso del subtema tocado.
---

# /duda — resolver una duda puntual

Argumento: la pregunta del usuario (texto libre), ej. `/duda por qué la rama
óptica tiene ω finita en q=0`.

## Pasos

1. **No leas el PDF.** Busca primero en `notas/*.md` (usa Grep/búsqueda por
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
   confirma, actualiza el archivo de `notas/` correspondiente con lo
   encontrado para que quede disponible en el futuro sin volver a leer el
   PDF.
6. Actualiza `progreso/progreso.md`: si el subtema tocado está marcado
   `no visto`, cámbialo a `en progreso` (no toques el estado si ya está
   `en progreso` o `dominado` — una duda puntual no rebaja un tema
   dominado).

## No hacer

- No generes un resumen completo del tema si no te lo piden — responde la
  pregunta puntual.
- No marques un tema como `dominado` desde `/duda` — eso solo lo hace
  `/evaluar`.
- No regeneres el dashboard automáticamente desde aquí.
