# Análisis de temas — parciales, talleres y question sets viejos

## Tabla de fuentes

| ID corto | Archivo real | Tipo | Fecha/semestre | Notas |
|---|---|---|---|---|
| `P-2026-1S` | `Parcial_1-2026-1S.pdf` | Parcial (opción múltiple, 18 preguntas) | 2026-1S | Cambio de formato: 100% conceptual salvo 1 numérica (#11). Sin solución manuscrita. |
| `P-2025-01` | `Parcial 1 - 2025-01.jpg` + `Parcial 1(2) - 2025-01.jpg` | Parcial (abierto, 2 imágenes) | 2025-01 | Img. 1 = mismo enunciado que `T-SS2020`/`P-SS2020` Q2 (cadena con 2dos vecinos). Img. 2 = mismo enunciado que `T-SS2020` Q4 (jellium). |
| `P-SS2020` | `Parcial I (SS2020).pdf` | Parcial (abierto, 4 preguntas) | Semestre especial 2020 | Solución manuscrita: `Parcial I (SS2020) - Mi solucion.pdf`. |
| `T-SS2020` | `Taller Vibraciones de red(SS2020).pdf` | Taller (abierto, 8 preguntas) | Semestre especial 2020 | Solución manuscrita en `Talleres Parcial 1 - Mi Solucion.pdf` (cuaderno combinado). |
| `T-2025-II` | `Taller I (2025 II).pdf` / `Taller I(2025 II).doc` | Taller (abierto, 7 preguntas) | 2025-II | Mismo taller en 2 formatos (idénticos). Solución parcial (Q1-4, Q7) también en `Talleres Parcial 1 - Mi Solucion.pdf`. |
| `T-2025-01` | `Taller 1 - 01-2025(Solucion).pdf` | Taller (abierto, 4 preguntas, con solución) | 2025-01 | Es la solución manuscrita completa de su propio enunciado (no hay PDF de enunciado limpio por separado). |
| `QS1`–`QS6` | `Ejercicios Conceptuales de Practica/Question_Set____Solid_State__1_.pdf` … `_6_.pdf` | Question set de práctica (opción múltiple con justificación por opción, inglés) | Sin fecha (curso "3006843") | Cubren todo el temario 1:1 con `notas/`: QS1=cristalografía, QS2=enlaces+ondas elásticas, QS3=calor específico clásico/Einstein/Debye, QS4=fonones/anarmonicidad/cadena monoatómica, QS5=cadena diatómica+3D, QS6=conductividad térmica+aplicaciones. |

**Fuera de este banco:** `Apuntes P1-Vibraciones de la Red- E.pdf` (49 páginas) — es la fuente de clase ya condensada en `notas/*.md`, no contiene preguntas de examen. `Talleres Parcial 1 - Mi Solucion.pdf` no tiene ID propio: es el cuaderno de soluciones manuscritas de `T-SS2020` + `T-2025-II`, más una síntesis comparativa "Einstein vs. Debye" ya escrita por el usuario (ver nota abajo).

## Síntesis manuscrita ya existente del usuario

`Talleres Parcial 1 - Mi Solucion.pdf` incluye una sección "Resumen de los modelos" donde el usuario ya comparó cualitativamente Einstein vs. Debye (supuestos, dominio de validez, por qué Debye reproduce T³ y Einstein no). Si en una evaluación futura sale un vacío o una duda sobre esta comparación, vale la pena preguntarle al usuario si quiere recuperar esa síntesis antes de reexplicarla desde cero.

## Ranking de subtemas "calientes" (frecuencia de aparición en el material viejo)

Contando apariciones en parciales/talleres clásicos + question sets (ver `banco_preguntas.md` para el detalle):

1. **calor.4 (Debye)** y **calor.3 (Einstein)** — los más preguntados con diferencia; aparecen en los 3 parciales, 2 talleres y 2 question sets completos (QS3 dedicado enteramente a esto).
2. **monoat.1 (cadena monoatómica discreta)** — aparece en 4 de las 6 fuentes clásicas y en QS4 completo.
3. **calor.6/calor.7 (fonón y su estadística)** — presente en 2 parciales, 1 taller, QS4.
4. **diatom.1 (cadena diatómica numérica)** — en 2 parciales/talleres y QS5 completo.
5. **extra.2/extra.3 (K∝1/T, Umklapp)** — se repite en `P-SS2020`, y es el tema completo de QS6.
6. **enlace.8 (Madelung/estabilidad del NaCl)** — recurrente en preguntas de selección múltiple (`P-2026-1S`, QS2).
7. **crist.8/crist.9 (red recíproca, zonas de Brillouin)** — cubierto a fondo solo por QS1 (no aparece en los parciales/talleres clásicos, que se concentran más en calor específico y dinámica de red).

## Vacíos que tenía `notas/` y quedaron cerrados

| Vacío detectado | Motivado por | Cerrado en |
|---|---|---|
| Cadena monoatómica con acoplamiento a 2dos vecinos | `Parcial SS2020 #2`, imagen `P-2025-01` | `notas/01b_cadena_monoatomica_discreta.md` — nuevo subtema `monoat.2` |
| Modelo de Debye en dimensión general D (1D/2D explícitos) | `Taller SS2020 #1, #6`, `Taller 2025-II #5` | `notas/03_densidad_estados_calor_especifico.md` — nuevo subtema `calor.8` |
| Energía de punto cero en Debye (`⟨u²⟩`, `E₀=9/8 Nk_BΘ_D`) | `Taller 01-2025 #2, #3` | `notas/03_densidad_estados_calor_especifico.md` — nuevo subtema `calor.9` |
| Dispersión inelástica de fotones/neutrones por fonones | `Taller SS2020 #5`, `Taller 2025-II #6` | `notas/03_densidad_estados_calor_especifico.md` — nuevo subtema `calor.10` |
| Momento total real del cristal vs. momento cristalino ℏq | `Taller 2025-II #1`, `Taller SS2020 #8`, `QS4 #1` | `notas/03_densidad_estados_calor_especifico.md` — nuevo subtema `calor.11` |
| Modelo de jellium (ion en mar de electrones, enlace metálico cuantitativo) | `Taller SS2020 #4`, imagen `P-2025-01(2)` | `notas/00b_enlaces_fuerzas_interatomicas.md` — nuevo subtema `enlace.9` |
| Grafeno como contraejemplo de "toda red periódica es Bravais" | `QS1 #3` | `notas/00_cristalografia_basica.md` — bullet agregado a `crist.3` (sin ID nuevo) |

Todos los demás temas de los question sets (QS1–QS6) ya estaban cubiertos de fondo por `notas/*.md`; sus preguntas se incorporaron directamente a `banco_preguntas.md` sin requerir contenido nuevo.
