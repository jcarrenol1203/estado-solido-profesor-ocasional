# Estado Sólido — Parcial 2: profesor ocasional

Sistema de auto-estudio para el segundo bloque del curso (metales y electrón libre), con los mismos tres comandos que `Parcial_1/`:

- `/duda <pregunta>` — responde una duda puntual desde `notas/`, cita la diapositiva `[p. N]` y marca el subtema como "en progreso".
- `/evaluar <tema>` — checklist de ~5 preguntas (numéricas, deducción, conceptuales, adaptadas del banco de exámenes viejos), corrige y actualiza el progreso.
- `/dashboard [isa|juan]` — publica un tablero visual con el avance del perfil.

Los skills viven en `.claude/skills/` de la raíz del repo y detectan el parcial (`Parcial_1/` o `Parcial_2/`).

## Estructura

```
Parcial_2/
  CLAUDE.md                      reglas del profesor ocasional
  README.md
  Diapositivas/Metales 2021.pdf  fuente (109 págs; ignorada por git)
  Talleres_Parciales/            talleres y parciales viejos (crudos)
  notas/00-05_*.md               contenido del PDF, con [p. N]
  notas/06-07_*.md               temas de examen fuera del PDF (bandas, astrofísica, vibraciones del parcial 2026-1S)
  examenes/                      banco de preguntas, análisis y guía por examen
  progreso/progreso.template.md  plantilla; copiar a isa.md / juan.md
```

## Uso

```bash
cp progreso/progreso.template.md progreso/juan.md   # o isa.md
```

## Adaptarlo a otro bloque

Extraer el PDF una sola vez a `notas/*.md` con citas de página, volcar los exámenes viejos a `examenes/`, regenerar la tabla del template con IDs nuevos y ajustar `CLAUDE.md`.
