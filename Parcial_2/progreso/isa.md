# Progreso — Parcial 2 (metales y electrón libre)

Fuente de verdad del avance del usuario en este bloque del curso. La leen y actualizan los skills `/duda`, `/evaluar` y `/dashboard` (con `BASE=Parcial_2/`). Nunca se llena "a mano" desde el PDF — todo sale de `notas/*.md`.

Estados posibles: `no visto` | `en progreso` | `dominado`.

**Dashboard URL:** https://claude.ai/artifact/LLC4kbKYAmUL7bLB8DeWyt

---

## Resumen rápido (27 subtemas)

| ID | Subtema | Archivo | Estado | Última evaluación |
|---|---|---|---|---|
| metal.1 | Metales, cristal metálico y concentración de e⁻ ($N=Z_vN_A\rho/M$) | 00_metales_y_gas_de_electrones.md | no visto | — |
| gas1d.1 | Gas de Fermi 1D: niveles, Pauli y $E_F$ | 00_metales_y_gas_de_electrones.md | no visto | — |
| interac.1 | Interacciones e⁻-ion y e⁻-e⁻; gas de e⁻ vs. gas ordinario | 00_metales_y_gas_de_electrones.md | no visto | — |
| drude.1 | Ley de Ohm y ecuación de Drude: $\sigma=Ne^2\tau/m^*$ | 01_modelo_de_drude.md | no visto | — |
| drude.2 | Tiempo de relajación, camino libre, movilidad, Joule | 01_modelo_de_drude.md | no visto | — |
| drude.3 | Origen de $\tau$: ondas de materia, Matthiessen, $\rho(T)$ | 01_modelo_de_drude.md | no visto | — |
| cal.1 | Calor específico electrónico: fracaso clásico | 02_estadistica_fermi_calor_especifico.md | no visto | — |
| cal.2 | Fermi-Dirac, potencial químico, $T_F$ y $C_e\propto T$ | 02_estadistica_fermi_calor_especifico.md | no visto | — |
| cal.3 | Energía interna del gas de Fermi, $U(T)$ | 02_estadistica_fermi_calor_especifico.md | no visto | — |
| fermi3d.1 | Gas 3D: ondas planas, $k_F$, $E_F$, $v_F$ | 03_gas_de_fermi_3D.md | no visto | — |
| fermi3d.2 | Densidad de estados $D(\varepsilon)$, $E_0$, presión y módulo de rigidez | 03_gas_de_fermi_3D.md | no visto | — |
| fermi3d.3 | Superficie de Fermi | 03_gas_de_fermi_3D.md | no visto | — |
| trans.1 | Conductividad eléctrica cuántica (esfera desplazada) | 04_transporte.md | no visto | — |
| trans.2 | Conductividad térmica y Wiedemann-Franz | 04_transporte.md | no visto | — |
| trans.3 | Resonancia ciclotrónica | 04_transporte.md | no visto | — |
| trans.4 | Efecto Hall | 04_transporte.md | no visto | — |
| term.1 | Emisión termoiónica y Richardson-Dushman | 05_emision_termoionica_y_fallas.md | no visto | — |
| falla.1 | Fallas del modelo del e⁻ libre | 05_emision_termoionica_y_fallas.md | no visto | — |
| extra.1 | Electrones casi libres: bandas, gaps, aislante/semiconductor/metal | 06_temas_de_examen_fuera_del_pdf.md | no visto | — |
| extra.2 | Zener magnético | 06_temas_de_examen_fuera_del_pdf.md | no visto | — |
| extra.3 | Escalas relativistas y astrofísicas del gas de Fermi | 06_temas_de_examen_fuera_del_pdf.md | no visto | — |
| vib.1 | Velocidad de fase/grupo y medios dispersivos | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |
| vib.2 | Cadena monoatómica: aliasing, $\lambda=2a$, $g(\omega)$ en $\pi/a$ | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |
| vib.3 | Modos normales, Bragg y ramas acústicas ($\omega_L>\omega_T$) | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |
| vib.4 | Cadena diatómica: ramas, gap, $M\to m$, borde de zona | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |
| vib.5 | Umklapp y conductividad térmica de fonones | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |
| vib.6 | Definición de $E_F$ a $T=0$ (pregunta de metales del parcial) | 07_vibraciones_para_parcial_2026_1S.md | no visto | — |

*(Nota de orden: el orden de estudio recomendado es el de la sección "Checklist detallado" más abajo, que sigue el temario de las diapositivas. `extra.1-3` no vienen del PDF — salen de vacíos detectados en `Talleres_Parciales/`, ver `examenes/analisis_temas.md`.)*

**Debilidades vigentes:** ninguna todavía (no se ha hecho ninguna evaluación).

## Parciales y talleres (banco de examenes viejos)

| ID | Tipo | Estado | Nota | Fecha |
|---|---|---|---|---|
| P-2025-2S | Parcial (abierto, 4 preguntas, con solución manuscrita) | no intentado | — | — |
| P-2025-01 | Parcial (abierto, 4 preguntas, #4 con 7 literales) | no intentado | — | — |
| P-2026-1S | Parcial II (20 selección múltiple: 19 vibraciones de red + 1 metales) | no intentado | — | — |
| T-2025-II | Taller (abierto, 8 problemas) | no intentado | — | — |
| T-SS2020 | Taller (abierto, 6 problemas) | no intentado | — | — |

## Log de evaluaciones

*(vacío — se llenará cada vez que se use `/evaluar`)*

---

## Checklist detallado — qué debes saber, tema por tema

Orden de estudio recomendado (sigue el orden de las diapositivas). Cada subtema tiene su rango de páginas de `Metales 2021.pdf`.

### Bloque 0 — Metales y gas de e⁻ [p. 1-23]

**metal.1 — Metales, cristal metálico y $N$** [p. 1-13]
- Describir pozos $U$ + gas de e⁻ libres; e⁻ de valencia → conducción (Na 3s, ~15 % del volumen son iones).
- Calcular $N=Z_vN_A\rho/M$; monovalentes vs. divalentes.
- Éxitos (Ohm, W-F) y fracasos (calor específico, $\ell$ largo) de la teoría clásica; las dos razones de la "transparencia".

**gas1d.1 — Gas de Fermi 1D** [p. 13-19]
- $\varepsilon_n=\hbar^2\pi^2n^2/2mL^2$ desde $\psi(0)=\psi(L)=0$; estado exacto vs. aproximado.
- Pauli: 2 e⁻ por nivel; $2n_F=N$; $\varepsilon_F$ en 1D.

**interac.1 — Interacciones** [p. 19-23]
- Por qué e⁻-ion (seudopotencial, apantallamiento) y e⁻-e⁻ (Pauli, energía mínima, hueco de Fermi) son débiles.
- Gas de e⁻ vs. gas ordinario: FD vs. MB, densidad, plasma.

### Bloque 1 — Drude [p. 24-50]

**drude.1 — Ohm y Drude** [p. 24-30]
- $m^*\dot v=-eE-m^*v/\tau$, $v_d=-e\tau E/m^*$, $J=-Nev_d$, $\sigma=Ne^2\tau/m^*$; $v_r\gg v_d$.

**drude.2 — $\tau$, $\ell$, $\mu$** [p. 31-37]
- $e^{-t/\tau}$, $\ell=v\tau$, $\mu=e\tau/m^*$, $\sigma=Ne\mu$; órdenes de magnitud; $\sigma_m/\sigma_i\sim10^{23}$; Joule $=I^2R$.

**drude.3 — Origen de $\tau$** [p. 38-50]
- e⁻-e⁻ conservan $J$; red perfecta no dispersa; fonones e impurezas; Matthiessen; $\rho_{ph}\propto T$ ($T\gg\theta$) y $T^5$ ($T\ll\theta$); Kondo.

### Bloque 2 — Estadística de Fermi y calor específico [p. 51-61, 106-109]

**cal.1 — Fracaso clásico** [p. 51-53]
- $C_e=\tfrac32R$, $C_{total}=4.5R$ vs. experimento $\approx3R$.

**cal.2 — FD y $C_e$** [p. 53-61]
- $f(E)$, $f(\mu)=\tfrac12$, $\mu(0)=E_F$, cola MB; $C_e\approx2R\,T/T_F$ ($\tfrac{\pi^2}{2}R\,T/T_F$); $C=\gamma T+\beta T^3$; anchura 90→10 % $=4.4k_BT$.

**cal.3 — $U(T)$** [p. 70-71, 106-109]
- Truco de sumar la identidad de $N$; integrales de e⁻ excitados y huecos.

### Bloque 3 — Gas de Fermi 3D [p. 62-73]

**fermi3d.1 — $k_F$, $E_F$, $v_F$** [p. 62-67]
- Condiciones periódicas → $e^{i\mathbf k\cdot\mathbf r}$, $k_i=2\pi n_i/L$; derivar $k_F=(3\pi^2n)^{1/3}$; $E_F$, $T_F$, $v_F$; $\langle v\rangle=\tfrac34v_F$.

**fermi3d.2 — $D(\varepsilon)$** [p. 68-71]
- $N(\varepsilon)\propto\varepsilon^{3/2}$, $D(E_F)=3N/2E_F$, $E_0=\tfrac35NE_F$, $P=\tfrac25nE_F$, $B=\tfrac23nE_F$.

**fermi3d.3 — Superficie de Fermi** [p. 72-73]
- Esfera en $\mathbf k$/$\mathbf v$; casi independiente de $T$; propiedad característica del metal.

### Bloque 4 — Transporte [p. 74-91]

**trans.1 — $\sigma$ cuántica** [p. 74-79]
- Esfera desplazada $\delta k=-eE\tau/\hbar$; solo e⁻ de la SF; $\sigma=Ne^2\tau_F/m^*$.

**trans.2 — W-F** [p. 80-83]
- $K=\tfrac13C_Vv_F\ell_F$, $K/\sigma=LT$, $L=\tfrac{\pi^2}{3}(k_B/e)^2$; por qué falla en aislantes.

**trans.3 — Ciclotrón** [p. 84-87]
- $\omega_c=eB/m^*$; absorción resonante; $\omega_c\tau\gg1$; medir $m^*$.

**trans.4 — Hall** [p. 88-91]
- $R_H=-1/Ne$; $R_H>0$ ⇒ huecos; qué cambia al invertir $B$.

### Bloque 5 — Termoiónica y fallas [p. 92-105]

**term.1 — Termoiónica** [p. 92-104]
- $\phi=E_{vac}-E_F$; $J=AT^2e^{-\phi/k_BT}$, $A=120$ A/cm²K²; Schottky; gráfica de Richardson.

**falla.1 — Fallas del modelo** [p. 105]
- $\sigma\propto N$ falla, $R_H>0$, SF no esférica, sin aislantes → bandas.

### Bloque 6 — Temas de examen fuera del PDF (sin páginas)

**extra.1 — Bandas casi libres**
- Gaps en fronteras de zona; electrón más afectado; metal/semiconductor/aislante con paridad y solapamiento; grafito vs. diamante; alcalinos.

**extra.2 — Zener magnético**
- Condición $\hbar\omega_cE_F\gtrsim E_g^2$.

**extra.3 — Astrofísica/relativista**
- $N\approx M/m_p$; $E_F$ no relativista y relativista $\hbar c(3\pi^2n)^{1/3}$; $T_F$, $\langle v\rangle$.

### Bloque 7 — Vibraciones de red del Parcial II 2026-1S (sin páginas de este PDF; teoría completa en `Parcial_1/notas/`)

**vib.1 — Fase y grupo** (`P-2026-1S #1, #8`)
- $v_f=\omega/q$, $v_g=d\omega/dq$; medio dispersivo ⇔ $v_f\ne v_g$; $v_g$ periódica como $\omega(q)$; $v_g\to v_s$ a $q\to0$.

**vib.2 — Cadena monoatómica** (`#2, #3, #7`)
- Aliasing $q\equiv q+G$ ($6a$ y $6a/7$ iguales); $\lambda=2a$ ⇒ contrafase; $v_g(\pi/a)=0$ ⇒ $g(\omega)\to\infty$.

**vib.3 — Modos normales y ramas** (`#6, #9, #10`)
- Conteo de modos con condiciones de frontera (cuerda vibrante); Bragg = onda + periodicidad; $\omega_L>\omega_T$ por fuerzas restauradoras (Newton).

**vib.4 — Cadena diatómica** (`#4, #5, #12, #13, #14, #15`)
- Acústica: centro de masa se mueve; óptica: fijo. Borde: $\omega_A=\sqrt{2C/M}$, $\omega_O=\sqrt{2C/m}$, $v_g=0$ en ambas; $M\to m$ cierra el gap; masas↑ ⇒ $\omega\downarrow$; en la óptica del borde solo se mueven los átomos ligeros; gap ⇒ $q$ complejo.

**vib.5 — Umklapp y $\kappa$ de fonones** (`#16-#20`)
- N conserva $\hbar q$, U lo cambia en $\hbar G$; U requiere $|q|\gtrsim|G|/2$ y da la resistencia a $T$ alta ($\kappa\propto1/T$); $\kappa\propto T^3$ a $T\to0$ en cristal finito; ópticos aportan poco ($v_g\approx0$).

**vib.6 — $E_F$ a $T=0$** (`#11`)
- Nivel ocupado más alto; no confundir con $\mu(T)$, energía media $\tfrac35E_F$ o función trabajo.
