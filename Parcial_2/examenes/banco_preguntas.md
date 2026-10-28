# Banco de preguntas — parciales y talleres viejos (Parcial 2)

> Extracción única de `Parcial_2/Talleres_Parciales/` (regla dura: no releer esos archivos crudos — ver `analisis_temas.md` y `CLAUDE.md`). Cada pregunta cita su fuente corta entre corchetes y su tipo (numérica / deducción / conceptual). Usado por `/evaluar` para adaptar preguntas reales de examen.

## metal.1 — Metales, cristal metálico y $N$
- Concentración de e⁻ de conducción del Li a partir de $E_F=4.72$ eV y verificación con $\rho=0.534$ g/cm³ ($A=6.941$): $n=4.66\times10^{28}$ m⁻³ vs. $4.63\times10^{28}$ m⁻³. **[P-2025-01 #1]** — numérica.
- Plata, $n=5.86\times10^{28}$ m⁻³: $E_F=5.5$ eV, comparación con $k_BT$ a 300 K (25.9 meV; razón ≈ 213). **[P-2025-01 #2]** — numérica.
- Cobre fcc, $a=3.61$ Å (4 átomos/celda, 1 e⁻/átomo): $n=8.5\times10^{28}$ m⁻³ (dato implícito para `drude.2`). **[P-2025-2S #1]** — numérica.

## gas1d.1 — Gas de Fermi 1D
- Metales unidimensionales: ¿pueden existir aislantes, semiconductores y conductores usando e⁻ casi libres? ¿igual que en 3D? **[P-2025-2S #4b]** — conceptual.
- En el modelo cuántico del gas libre la cuantización de la energía no es una suposición: ¿de dónde viene? (condiciones de frontera / confinamiento, $\psi(0)=\psi(L)=0$). **[P-2025-01 #4g]** — conceptual.

## interac.1 — Gas de Fermi vs. gas ordinario
- Un gas familiar es el aire: explicar analogías y diferencias con el gas de e⁻ (FD vs. MB, energía a $T=0$, densidad, plasma). **[P-2025-01 #4c]**, **[P-2025-2S #4a]** — conceptual (misma pregunta dos veces).
- ¿Por qué la dispersión e⁻-e⁻ no explica el cambio de la velocidad de deriva? (conserva el momento total). **[P-2025-01 #4f]** — conceptual.

## drude.1 — Drude, ley de Ohm, deriva
- Alambre de Cu de 2 mm² con 20 A: $v_d/v_F$ ($v_d=I/neA\approx7\times10^{-4}$ m/s; $v_d/v_F\approx5\times10^{-10}$). **[T-2025-II #6]** — numérica. (Fórmula $v_d=I/(neA)$ anotada en `P-2025-01`.)
- Modelo cinético de Drude: la energía no se conserva en colisiones; demostrar que la pérdida de potencia en un hilo ($L$, $A$) es $I^2R$. **[T-SS2020 #5]** — deducción.

## drude.2 — Tiempo de relajación y camino libre
- Camino libre medio en Cu con $\tau=10^{-9}$ s, fcc $a=3.61$ Å (con $v_F$: ≈ 1.6 mm). **[P-2025-2S #1]** — numérica (la solución usó $v$ térmico: error).
- Muestra a 4 K con $\tau=3\times10^{-10}$ s: ¿qué $B$ hace que el e⁻ complete al menos una órbita ciclotrónica? ($\omega_c\tau\ge1$: $B\gtrsim0.019$ T; con $2\pi$: 0.12 T). **[T-2025-II #4]** — numérica.

## drude.3 — Origen de $\tau$, Matthiessen, $\rho(T)$
- Con velocidad térmica de gas clásico, mostrar que $\rho\propto T^{3/2}$. **[T-2025-II #2]** — deducción.

## cal.1 — Calor específico electrónico: fracaso clásico
- Sin pregunta real propia; aparece implícita en `P-2025-01 #4b` y `T-2025-II #8` (valor clásico $\tfrac32R$ vs. experimento). Para `/evaluar`, basarse en los puntos clave de la nota.

## cal.3 — Energía interna del gas de Fermi
- Sin pregunta real propia; el contenido (energía de e⁻ excitados y huecos) respalda `P-2025-01 #3a`. Para `/evaluar`, pedir la deducción de $U=\int(\varepsilon-E_F)Df+\int(E_F-\varepsilon)(1-f)D$.

## cal.2 — Fermi-Dirac, $T_F$ y calor específico
- Anchura de $f(E)$ entre 90 % y 10 %: $\Delta E=2\ln9\,k_BT\approx4.4k_BT$. **[T-2025-II #1]** — deducción/numérica.
- Fracción de e⁻ excitados sobre $E_F$ a 300 K para Cu y Na ($\sim T/T_F$: 0.0037 y 0.008). **[P-2025-2S #3]** — numérica.
- $T_F$ de Cu, Na, Ag y $T/T_F$ a 300 K con $m^*$(Cu)=$m_0$, $m^*$(Na)=1.2$m_0$. **[T-SS2020 #4]** — numérica.
- Comparar $C_{red}$ y $C_{el}$ a 300 K con $\theta_D\sim300$ K y hallar la $T$ en que son del mismo orden (≈ 3 K). **[T-2025-II #8]** — numérica.
- Energía interna promedio de un metal con $E_F=7.5$ eV a $T=100$ K: cuántica $\approx\tfrac35E_F=4.5$ eV (corrección térmica despreciable) vs. clásica $\tfrac32k_BT=0.013$ eV. **[P-2025-01 #3a]** — numérica/conceptual.
- Significado físico de $T_F\sim5\times10^4$ K y su consecuencia en el calor específico (solo $\sim T/T_F$ de los e⁻ participan; $C_e\propto T$, ~1 % del clásico). **[P-2025-01 #4b]** — conceptual.

## fermi3d.1 — $k_F$, $E_F$, $v_F$
- Estrella colapsada en enana blanca ($M=2\times10^{30}$ kg, $R=7\times10^8$ m): $E_F$ (32 eV), $T_F$ ($3.7\times10^5$ K), $\langle v\rangle=\tfrac34v_F$ ($2.5\times10^6$ m/s). **[P-2025-2S #2]** — numérica.
- Energía de Fermi del Cu con $n=8.45\times10^{28}$ m⁻³ (7.05 eV) y velocidad de un e⁻ con $E=E_F$ ($1.57\times10^6$ m/s). **[T-SS2020 #2]** — numérica.
- He³ líquido (espín ½, fermión), $\rho=0.081$ g/cm³: $E_F=4.2\times10^{-4}$ eV, $T_F=4.9$ K (usar la masa del átomo de He³). **[T-SS2020 #3]** — numérica.
- Metal con $4\times10^{28}$ m⁻³ estados, pozo finito: $E_F=4.27$ eV, $v_F=1.2\times10^6$ m/s. **[P-2025-01 #3b]** — numérica.
- Sodio con $\alpha=1.5\times10^{-6}$ K⁻¹ (0-300 K): $\Delta E_F/E_F=-2\alpha\Delta T=-0.09$ % ($E_F\propto V^{-2/3}\propto\ell^{-2}$). **[T-SS2020 #6]** — numérica/deducción.
- Gas de Fermi estelar: número de e⁻ del Sol ($M=2\times10^{33}$ g → $N=1.2\times10^{57}$) y $E_F$ en una enana blanca ($R=2\times10^9$ cm); límite relativista $E_F\approx\hbar c(N/V)^{1/3}$; pulsar $R=10$ km → $\sim10^8$ eV. **[T-2025-II #3]** — numérica/deducción.

## fermi3d.2 — $D(\varepsilon)$, presión, módulo de rigidez
- Módulo de rigidez $B=-V(\partial P/\partial V)_T$ del gas libre a $T=0$ con $P=-(\partial E/\partial V)_T$, $E_0=\tfrac35NE_F$, para Al, K, Cs, Cu (teóricos: 226, 3.2, 1.5, 64 GPa vs. exp. 76, 2.81, 1.43, 134 GPa). **[T-2025-II #5]** — deducción/numérica.
- Presión del gas de e⁻ a 0 K: $P=\tfrac25nE_F$. **[T-2025-II #7]** — deducción.
- Energía interna promedio $E=\tfrac35E_F$ a $T=0$ y por qué contradice el gas clásico. **[P-2025-01 #3a]** — conceptual.

## fermi3d.3 — Superficie de Fermi
- Sin pregunta real propia; relacionada con `P-2025-2S #4f` (el e⁻ más afectado por el potencial periódico es el más cercano a la frontera de zona). Para `/evaluar`, usar los puntos clave de la nota.

## trans.1 — Conductividad eléctrica cuántica
- Sin pregunta real propia; las conceptuales `P-2025-01 #4f` (e⁻-e⁻ no cambian $v_d$) y `T-2025-II #6` ($v_d/v_F$) la tocan.

## trans.2 — Wiedemann-Franz
- Por qué existen materiales (alúmina) con alta conductividad térmica y $\sigma\approx0$ vista desde W-F (la conducción térmica la llevan fonones, no e⁻). **[P-2025-01 #4d]** — conceptual.

## trans.3 — Resonancia ciclotrónica
- Ver `T-2025-II #4` bajo `drude.2` (órbita ciclotrónica completa).

## trans.4 — Efecto Hall
- Si en cobre se invierte el sentido de $B$: ¿cambia el signo del voltaje Hall? ¿el de la magnetorresistencia? Explicación física en ambos. **[P-2025-01 #4a]** — conceptual.

## term.1 — Termoiónica
- Mecanismo fundamental del efecto termoiónico. **[P-2025-01 #4e]** — conceptual.

## falla.1 — Fallas del modelo del e⁻ libre
- Sin pregunta real propia; `P-2025-2S #4b, #4d` y `P-2025-01 #4a` (Hall) evalúan su consecuencia (aislantes, $R_H>0$, alcalinos vs. Al/Bi).

## extra.3 — Astrofísica y límite relativista
- Preguntas reales ya listadas bajo `fermi3d.1`: **[P-2025-2S #2]** y **[T-2025-II #3]** (enana blanca, pulsar, $E_F\approx\hbar c(N/V)^{1/3}$).

## extra.1 — Electrones casi libres y bandas
- Grafito conduce y diamante no (ambos C, $1s^22s^22p^2$): interpretar desde bandas. **[P-2025-2S #4c]** — conceptual.
- Por qué los alcalinos se ajustan al e⁻ libre y Al, Bi no. **[P-2025-2S #4d]** — conceptual.
- ¿Un cristal con número par de e⁻ de valencia por celda primitiva siempre es aislante? **[P-2025-2S #4e]** — conceptual.
- Cúbico simple $a=1$ Å, $\mathbf k_1=(10^{-2},0,0)$, $\mathbf k_2=(1,1,0)$, $\mathbf k_3=(\pi,\pi/3,0)$ Å⁻¹: ¿cuál es el más afectado por el potencial periódico? (**$\mathbf k_3$**, está en $k_x=\pi/a$). **[P-2025-2S #4f]** — conceptual/numérica.

## extra.2 — Zener magnético
- Condición análoga con campo magnético a $eEaE_F/E_g^2>1$ (con $ak_F\sim1$). **[T-SS2020 #1]** — deducción.

## vib.1 a vib.6 — P-2026-1S (Parcial II 2026-1S, 20 selección múltiple; 19 de vibraciones + 1 de metales)
Transcripción completa en `guia_teoria_por_examen.md` §P-2026-1S (enunciado y las 5 opciones de cada pregunta, clave y justificación). Aquí, el índice por subtema, con la clave entre paréntesis:

- **vib.1 — Velocidad de fase/grupo y medios dispersivos:** **[P-2026-1S #1]** velocidad de grupo en un sólido (**b**, periodicidad como ω(q)) — conceptual; **[P-2026-1S #8]** medio dispersivo (**e**, $v_f\ne v_g$) — conceptual.
- **vib.2 — Cadena monoatómica, zona de Brillouin:** **[P-2026-1S #2]** ondas $6a$ y $6a/7$ (**c**, mismas oscilaciones; $q$ difiere en $G$) — conceptual/numérica; **[P-2026-1S #3]** $g(\omega)$ diverge en $\pi/a$ (**e**, $v_g=0$ en la frontera) — conceptual; **[P-2026-1S #7]** $\lambda=2a$ (**d**, átomos en contrafase) — conceptual.
- **vib.3 — Modos normales y ramas acústicas:** **[P-2026-1S #6]** cuerda vibrante como modelo (**c**, soluciones independientes que cumplen condiciones de frontera) — conceptual; **[P-2026-1S #9]** Bragg en vibraciones (**e**, naturaleza ondulatoria + red periódica) — conceptual; **[P-2026-1S #10]** modo longitudinal de mayor frecuencia (**c**, leyes de Newton) — conceptual.
- **vib.4 — Cadena diatómica:** **[P-2026-1S #4]** diferencia acústica/óptica (**c**, movimiento del centro de masa) — conceptual; **[P-2026-1S #5]** frecuencia en el gap (**a**, $q$ complejo) — conceptual; **[P-2026-1S #12]** $M\to m$ (**c**, la brecha se cierra) — conceptual; **[P-2026-1S #13]** $v_g$ en $q=\pi/a$ (**d**, cero en ambas) — conceptual; **[P-2026-1S #14]** masas↑ con $C$ fija (**a**, la rama óptica baja) — conceptual; **[P-2026-1S #15]** átomos que se mueven en la óptica en $\pi/a$, $M>m$ (**d**, solo los ligeros) — conceptual.
- **vib.5 — Umklapp y conductividad térmica de fonones:** **[P-2026-1S #16]** proceso U vs. N (**a**) — conceptual; **[P-2026-1S #17]** por qué U da resistencia a $T$ alta (**a**) — conceptual; **[P-2026-1S #18]** $q$ mínimo para U (**b**, $|q|\approx|G|/2$) — conceptual; **[P-2026-1S #19]** $\kappa(T)$ a $T\to0$, cristal finito (**a**, $\propto T^3$) — conceptual; **[P-2026-1S #20]** ópticos y $\kappa$ (**c**, $v_g\approx0$) — conceptual.
- **vib.6 — Definición de $E_F$ (metales):** **[P-2026-1S #11]** (**b**, energía del estado ocupado más alto a $T=0$) — conceptual. Ver también `fermi3d.1`.

*(La clave se dedujo por física. El estudiante original sacó 11/20 = 2.7; los 11 aciertos que cuadran con esa nota son #1, 3, 8, 9, 10, 11, 12, 14, 15, 18 y 20. En #5 la clave es **a** porque su respuesta marcada, la c, no suma entre esos 11; ambas opciones describen el mismo fenómeno.)*
