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

## Alcance (diapositivas 1-70) y mapa a Pavlov

El parcial llega hasta la **p. 70** de `Metales 2021.pdf`. Mapa diapositivas → subtema:

| Págs. | Subtema | En alcance |
|---|---|---|
| 1-13 | metal.1 | sí |
| 13-18 | gas1d.1 | sí |
| 19-23 | interac.1 | sí |
| 24-50 | drude.1-3 (24-30, 31-37, 38-50) | sí |
| 51-61 | cal.1 (51-53), cal.2 (53-61) | sí |
| 62-67 | fermi3d.1 | sí |
| 68-70 | fermi3d.2 | sí |
| 70-71, 106-109 | cal.3 | no |
| 72-73 | fermi3d.3 | no |
| 74-91 | trans.1-4 | no |
| 92-105 | term.1, falla.1 | no |

Pavlov (recomendado): `Diapositivas/pdf-fisica-del-estado-solido-p-v-pavplovpdf_compress.pdf`. Mapa completo en `notas/08_mapa_pavlov.md`. Resumen: gas de Fermi, FD, $E_F$, $D(E)$ y $C_e$ → **§6.1** (pp. 200-206); modelos de Drude/Sommerfeld e interacciones → **§7.1** (pp. 235-236); $\sigma(T)$ de metales → **§7.13** (pp. 286-287). El libro no cubre 1D, la deducción de Drude ni el §2.6 (falta en la copia).


## Material de estudio (teoría, práctica, examen, exámenes viejos)

| Carpeta | Contenido |
|---|---|
| `teoria/` | Teoría por bloque con las diapositivas 1-70 y el Pavlov correspondiente (imágenes con capítulo/página) |
| `practica/` | Ejercicios resueltos paso a paso, teóricos y numéricos |
| `examen/` | Examen propuesto sin ayuda (teoría y ejercicios), para calificar con Claude |
| `examenes_resueltos/` | Exámenes viejos resueltos paso a paso. `T-2026-II.md` (taller nuevo) va completo: primero los 12 enunciados y después cada solución en un botón plegable, con página de diapositiva y de Pavlov |

Dashboard: `python3 ../.claude/skills/dashboard/tools.py sync <persona>` y luego `/dashboard`.
