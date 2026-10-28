# Análisis de temas — parciales y talleres viejos (Parcial 2)

## Tabla de fuentes

| ID corto | Archivo real | Tipo | Fecha/semestre | Notas |
|---|---|---|---|---|
| `P-2025-01` | `Talleres_Parciales/Parcial 2. - 2025-01.pdf` | Parcial (abierto, 4 preguntas; la #4 tiene 7 literales a-g) | 2025-01 | Foto de un examen; sin solución legible. |
| `P-2025-2S` | `Talleres_Parciales/Parcial 2 (2025-2S) - Estado Sólido.pdf` | Parcial (abierto, 4 preguntas; la #4 tiene literales a-f) | 2025-2S | 2 páginas, **con solución manuscrita calificada** (nota 3.3 de 5). Bandas casi libres en #4b-f. |
| `P-2026-1S` | `Talleres_Parciales/Parcial 2026_1S/Foto1-4.jpeg` | Parcial II (20 preguntas de selección múltiple, 5 opciones) | 2026-1S | **19 de vibraciones de red/fonones + 1 de metales (#11, definición de $E_F$)**. Estudiante: 11/20 = 2.7. Transcripción completa (enunciados y opciones) en `guia_teoria_por_examen.md`; clave deducida por física. Distinto de `Parcial_1/…/Parcial_1-2026-1S.pdf` (18 preguntas, "Parcial 1"). |
| `T-2025-II` | `Talleres_Parciales/Estado Solido (Taller II  2025 SII).pdf` | Taller (abierto, 8 problemas) | 2025-II | Texto limpio. |
| `T-SS2020` | `Talleres_Parciales/Estado Solido(tallerII) SS2020.pdf` | Taller (abierto, 6 problemas) | Semestre especial 2020 | Texto limpio. |

**Fuente de contenido:** `Diapositivas/Metales 2021.pdf` (109 págs), ya condensado en `notas/00-05`. El material de bandas que piden los parciales de 2025 **no está en esas diapositivas**: se cubrió en `notas/06_temas_de_examen_fuera_del_pdf.md` (`extra.1-3`).

## Ranking de subtemas "calientes" (frecuencia en el material viejo)

1. **fermi3d.1 ($k_F$, $E_F$, $T_F$, $v_F$ desde $n$)** — aparece en los 4 exámenes de metales: `P-2025-01 #1, #2, #3b`, `P-2025-2S #2, #3`, `T-2025-II #3, #5, #6`, `T-SS2020 #2, #3, #4, #6`. Es lo más preguntado con diferencia.
2. **cal.2 (FD, $T/T_F$, $C_e$)** — `P-2025-2S #3`, `P-2025-01 #3, #4b`, `T-2025-II #1, #8`, `T-SS2020 #4`.
3. **interac.1 / gas de Fermi vs. gas ordinario** — `P-2025-01 #4c` y `P-2025-2S #4a` (pregunta casi idéntica en dos parciales).
4. **extra.1 (bandas casi libres, aislante/semiconductor/metal)** — `P-2025-2S #4b-f` (5 literales) y `P-2025-01 #4g`.
5. **trans.2 (Wiedemann-Franz)** — `P-2025-01 #4d`.
6. **trans.4 (Hall / magnetorresistencia)** — `P-2025-01 #4a`.
7. **term.1 (termoiónica)** — `P-2025-01 #4e`.
8. **drude.1-3 (Drude, camino libre, $v_d$, $\rho\propto T^{3/2}$)** — `P-2025-2S #1`, `P-2025-01 #4f`, `T-2025-II #2, #4, #6`, `T-SS2020 #5`.
9. **extra.3 (astrofísica/relativista)** — `P-2025-2S #2`, `T-2025-II #3`.

## Observaciones de corrección (P-2025-2S, solución manuscrita)

- **#1 (camino libre Cu):** la solución usó $v$ térmico de equipartición ($\tfrac12mv^2=\tfrac32k_BT$) y recibió ~0.2 puntos. En el modelo de Fermi se usa $v_F$: con $n=4/a^3=8.5\times10^{28}$ m⁻³, $v_F=1.57\times10^6$ m/s y $\ell=v_F\tau=1.6$ mm.
- **#2 (enana blanca):** $E_F=32$ eV con $N=M/m_p$ (20 eV si $N=M/2m_p$), $T_F=3.7\times10^5$ K, $\langle v\rangle=\tfrac34v_F=2.5\times10^6$ m/s.
- **#3 (fracción excitada $T/T_F$):** Cu $\approx0.0037$ ($E_F=7$ eV; la solución usó 1.23 eV y obtuvo 0.0035), Na $\approx0.008$.
- **#4f:** la respuesta correcta es $\mathbf k_3=(\pi,\pi/3,0)$ (sobre el plano de Bragg $k_x=\pi/a$); la solución eligió $\mathbf k_1$ y perdió el punto.
- **#4b, #4d, #4e:** respondidas parcialmente, ver `notas/06` (`extra.1`).

## Vacíos que tenía el material y quedaron cerrados

| Vacío detectado | Motivado por | Cerrado en |
|---|---|---|
| Electrones casi libres, gaps, aislante/semiconductor/metal, paridad de e⁻ y solapamiento, grafito vs. diamante | `P-2025-2S #4b-f` | `notas/06_temas_de_examen_fuera_del_pdf.md` — `extra.1` |
| Condición análoga al efecto Zener con $B$ | `T-SS2020 #1` | `notas/06...` — `extra.2` |
| Escalas relativistas/astrofísicas ($E_F\approx\hbar c\,n^{1/3}$) | `T-2025-II #3`, `P-2025-2S #2` | `notas/06...` — `extra.3` |
| Presión, módulo de rigidez y $E_0=\tfrac35NE_F$ del gas de Fermi | `T-2025-II #5, #7`, `P-2025-01 #3` | `notas/03_gas_de_fermi_3D.md` — `fermi3d.2` |
| Anchura de la distribución FD (90 %→10 %) y $C_e$ vs. $C_{red}$ | `T-2025-II #1, #8` | `notas/02_estadistica_fermi_calor_especifico.md` — `cal.2` |

## Nota de alcance

`P-2026-1S` (las 4 fotos) es el **Parcial II de 2026-1S** y trata sobre todo vibraciones de red y fonones (cadena monoatómica/diatómica, Umklapp, conductividad térmica de fonones), con una pregunta de metales (#11). Por eso este parcial cubre los bloques 0-5 (metales) **y** el bloque 7 (`vib.1-6`, resumen en `notas/07_vibraciones_para_parcial_2026_1S.md`, teoría completa en `Parcial_1/notas/`). Orden de frecuencia: vib.4 (cadena diatómica, 6 preguntas) > vib.5 (Umklapp/κ, 5) > vib.2 y vib.3 (3 cada una) > vib.1 (2) > vib.6 (1).
