# Guía de teoría por examen — Parcial 2

> Guía autocontenida por archivo de `Talleres_Parciales/`: enunciado resumido, teoría con página de `Diapositivas/Metales 2021.pdf` (`[p. N]`) o nota de apoyo, fórmula clave y resultado. Si hay conflicto con `banco_preguntas.md`, manda esta guía. Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $k_B=1.381\times10^{-23}$ J/K, $1\text{ eV}=1.602\times10^{-19}$ J.

Fórmula maestra: $E_F=\dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$, $k_F=(3\pi^2n)^{1/3}$, $v_F=\hbar k_F/m$, $T_F=E_F/k_B$ [p. 66-67].

## P-2025-01 — Parcial II (2025-01)

1. **$E_F(\text{Li})=4.72$ eV → $n$.** Invertir: $n=\frac1{3\pi^2}(2mE_F/\hbar^2)^{3/2}=4.66\times10^{28}$ m⁻³. Verificar con $n=Z\rho N_A/M=0.534\cdot6.022\times10^{23}/6.941=4.63\times10^{22}$ cm⁻³ ✔. [p. 10, 66]
2. **Plata, $n=5.86\times10^{28}$ m⁻³:** $E_F=5.50$ eV ($T_F=6.4\times10^4$ K); a 300 K $k_BT=25.9$ meV → $E_F/k_BT\approx213$: los e⁻ son altamente degenerados. [p. 66, 56]
3. (a) $\bar E_{T=0}=\tfrac35E_F=4.5$ eV con $E_F=7.5$ eV; a 100 K la corrección térmica es $\sim(\pi^2/4)(k_BT)^2/E_F\approx2\times10^{-5}$ eV (despreciable) → cuántica ≈ 4.5 eV; clásica $\tfrac32k_BT=0.0129$ eV (350× menor). [p. 68-71] (b) $n=4\times10^{28}$ m⁻³: $E_F=4.27$ eV, $v_F=1.2\times10^6$ m/s. [p. 66-67]
4. **Conceptuales:**
   - (a) Hall: invertir $\mathbf B$ **cambia el signo de $V_H$** ($E_H=-J_xB/Ne$); la magnetorresistencia **no cambia de signo** (es par en $B$; en e⁻ libres es nula). [p. 88-91]
   - (b) $T_F\sim5\times10^4$ K: a 300 K solo $T/T_F\sim10^{-2}$ de los e⁻ se excita ⇒ $C_e=\tfrac{\pi^2}{2}R\,T/T_F\approx1\%$ del clásico $\tfrac32R$; $C_e\propto T$. [p. 53-59]
   - (c) Gas de Fermi vs. aire: ambos sin interacción fuerte y ocupan todo el volumen; difieren en estadística (FD vs. MB), $E(T=0)=\tfrac35E_F\neq0$ (aire: 0), densidad ($10^{29}$ vs. $10^{25}$ m⁻³), carga (plasma denso vs. neutro). [p. 19-23]
   - (d) Wiedemann-Franz $K/\sigma=LT$ es de e⁻; la alúmina tiene $K$ alta por **fonones** y $\sigma\approx0$ (sin e⁻ libres). [p. 80-83]
   - (e) Termoiónica: e⁻ de la cola de FD con $E\ge E_F+\phi$ escapan por agitación térmica ($J=AT^2e^{-\phi/k_BT}$). [p. 92-104]
   - (f) e⁻-e⁻ conservan el momento total → no cambian $v_d$ ni $J$; solo e⁻-red (fonones, impurezas). [p. 38-39]
   - (g) La cuantización viene del **confinamiento**/condiciones de frontera: $\psi(0)=\psi(L)=0$ ⇒ $k=n\pi/L$. [p. 13-16]

## P-2025-2S — Parcial II (2025-2S) · solución manuscrita (3.3/5)

1. **Camino libre medio Cu** ($\tau=10^{-9}$ s, fcc $a=3.61$ Å): $n=4/a^3=8.50\times10^{28}$ m⁻³ → $v_F=1.57\times10^6$ m/s → $\ell=v_F\tau=1.6\times10^{-3}$ m. (Error en la solución: usar $v_{térmico}$.) [p. 34, 78]
2. **Sol colapsado** ($M=2\times10^{30}$ kg, $R=7\times10^8$ m, $N=M/m_p=1.2\times10^{57}$): $n=8.3\times10^{29}$ m⁻³ → $E_F=32.3$ eV, $T_F=3.74\times10^5$ K, $v_F=3.37\times10^6$ m/s, $\langle v\rangle=\tfrac34v_F=2.53\times10^6$ m/s. [p. 66-67]
3. **Fracción excitada** $\sim T/T_F$: Cu ($E_F=7.05$ eV, $T_F=8.2\times10^4$ K) 0.0037; Na ($E_F=3.2$ eV, $T_F=3.7\times10^4$ K) 0.008. [p. 55-59]
4. (a) gas de Fermi vs. aire (ver `P-2025-01 #4c`). (b) 1D con e⁻ casi libres: hay gaps en $k=n\pi/a$ → conductor (banda semillena) o aislante/semiconductor (bandas llenas); en 3D los gaps pueden solaparse en energía. (c) grafito vs. diamante: gap grande en diamante (sp³); π/π* solapadas en grafito. (d) alcalinos: 1 e⁻ s, seudopotencial débil, SF casi esférica. (e) **No**: par ⇒ aislante solo si las bandas no se solapan (ej. divalentes). (f) **$\mathbf k_3=(\pi,\pi/3,0)$**, sobre $k_x=\pi/a$ (plano de Bragg). Teoría: `notas/06` (`extra.1`).

## T-2025-II — Taller II (2025-II)

1. FD pasa de 90 % a 10 %: $(E-\mu)/k_BT=\mp\ln9$ → $\Delta E=2\ln9\,k_BT=4.39\,k_BT$ (0.114 eV a 300 K). [p. 55-56]
2. Resistividad clásica $\propto T^{3/2}$: $\rho=m/(Ne^2\tau)$, $\tau=\ell/v$, $v\propto T^{1/2}$ y $\ell=1/(N\sigma_{ph})$ con $\sigma_{ph}\propto\langle x^2\rangle\propto T$ ⇒ $\rho\propto T\cdot T^{1/2}=T^{3/2}$. [p. 46-48]
3. Estrella: (a) $N=M/m_p=1.2\times10^{57}$; enana blanca $R=2\times10^9$ cm: $E_F\approx4\times10^4$ eV. (b) $E=\hbar kc$, $E_F=\hbar c(3\pi^2N/V)^{1/3}$. (c) Pulsar $R=10$ km: $E_F\sim4\times10^8\approx10^8$ eV. `notas/06` (`extra.3`).
4. $B$ para una órbita ciclotrónica: $\omega_c\tau\ge1$ → $B\ge m/(e\tau)=0.019$ T ($0.12$ T con $2\pi$). [p. 84-87]
5. $B=-V(\partial P/\partial V)=\tfrac23nE_F$ (con $P=-\partial E_0/\partial V=\tfrac25nE_F$, $E_F\propto V^{-2/3}$): Al 226 GPa (exp. 76), K 3.2 (2.81), Cs 1.5 (1.43), Cu 64 (134) → buen acuerdo en alcalinos. [p. 66-71]
6. $v_d=I/(neA)=20/(8.45\times10^{28}\cdot1.6\times10^{-19}\cdot2\times10^{-6})=7.4\times10^{-4}$ m/s; $v_d/v_F=4.7\times10^{-10}$. [p. 36-37, 77]
7. $P=\tfrac25nE_F=\tfrac23E_0/V$ a $T=0$. [p. 68-71]
8. $C_{red}(300\text{ K})\approx3R$ ($\theta_D=300$ K); $C_e=\tfrac{\pi^2}{2}R\,T/T_F=0.0085\cdot3R$ ($T_F\approx5.8\times10^4$ K) → $C_e/C_{red}\approx0.85\%$. Iguales cuando $\tfrac{\pi^2}{2}R\,T/T_F=\tfrac{12\pi^4}{5}R(T/\theta_D)^3$ → $T\approx3$ K. [p. 53-59]

## T-SS2020 — Taller II (SS2020)

1. Zener magnético: sustituir $eE\to ev_FB$ y $ak_F\sim1$ ⇒ $\hbar\omega_cE_F\gtrsim E_g^2$. `notas/06` (`extra.2`).
2. Cu $n=8.45\times10^{28}$: $E_F=7.05$ eV, $v_F=1.57\times10^6$ m/s. [p. 66-67]
3. He³ ($\rho=0.081$ g/cm³, $n=1.62\times10^{28}$ m⁻³, masa del átomo $M=5.0\times10^{-27}$ kg): $E_F=4.2\times10^{-4}$ eV, $T_F=4.9$ K. [p. 66]
4. $T_F$: Cu 81 000 K ($T/T_F=0.0037$), Na (con $n=2.65\times10^{28}$, $m^*=1.2m_0$) 31 000 K (0.0096), Ag 64 000 K (0.0047). [p. 66-67]
5. Potencia: $P=\mathbf J\cdot\mathbf E\cdot AL=\sigma E^2AL=\frac{V^2}{R}=I^2R$ (con $V=EL$, $R=L/\sigma A$). [p. 37]
6. $E_F\propto V^{-2/3}\propto\ell^{-2}$ ⇒ $\Delta E_F/E_F=-2\alpha\Delta T=-2(1.5\times10^{-6})(300)=-9\times10^{-4}=-0.09\,\%$. [p. 66]

## P-2026-1S — Parcial II (S I 2026), 20 preguntas de selección múltiple (11/20 = 2.7)

Transcripción de las 4 fotos ampliadas. **Clave deducida por física** (la hoja trae la respuesta marcada del estudiante, no una clave oficial): los 11 aciertos que cuadran con la nota son #1, 3, 8, 9, 10, 11, 12, 14, 15, 18 y 20. Teoría de apoyo: `notas/07_vibraciones_para_parcial_2026_1S.md` (vib.1-vib.5) y `Parcial_1/notas/`. "Est." = opción marcada por el estudiante.

**1. (vib.1)** Una de las principales propiedades de la velocidad de grupo de una onda en un sólido es: a. su valor igual a cero para vectores de onda pequeños; b. su periodicidad similar a la de la relación de dispersión; c. su valor alto en medios dispersivos; d. su variación lineal con el vector de onda; e. su variación cuadrática con el vector de onda. → **b** (Est. b ✔). $v_g=d\omega/dq$ hereda el periodo $2\pi/a$ de $\omega(q)$; a es falsa ($v_g\to v_s$ a $q\to0$).

**2. (vib.2)** Cadena lineal monoatómica que puede transportar dos ondas con $\lambda=6a$ y $6a/7$. Dinámicamente representan: a. oscilaciones 180° fuera de fase; b. oscilaciones 90° fuera de fase; c. oscilaciones en fase; d. una onda estacionaria; e. un pulso. → **c** (Est. b ✘). $q_2=7\pi/3a=q_1+2\pi/a$: mismos desplazamientos en todos los nodos.

**3. (vib.2)** En una cadena monoatómica $g(\omega)$ diverge cuando $q=\pi/a$. Se atribuye a: a. el comportamiento lineal de $\omega(q)$ al acercarse a este valor; b. la interferencia constructiva de la onda incidente y la reflejada; c. la dispersión de la onda en la frontera; d. un número muy grande de estados en un rango pequeño de frecuencia; e. el valor cero de la velocidad de grupo en la frontera. → **e** (Est. e ✔). $g\propto1/v_g$ y $v_g(\pi/a)=0$ (d es consecuencia, e es la causa).

**4. (vib.4)** En una cadena lineal diatómica, la diferencia principal entre la rama acústica y la óptica radica en: a. la masa de los iones constituyentes; b. la diferencia entre las constantes elásticas atómicas para los dos iones; c. el movimiento del centro de masa; d. la diferencia en los valores de la carga eléctrica de los átomos en la celda unitaria; e. la diferencia en las velocidades de grupo para los dos modos. → **c** (Est. e ✘). Acústica: el centro de masa se mueve; óptica: queda fijo.

**5. (vib.4)** Una onda con frecuencia dentro del rango prohibido de una cadena lineal monoatómica: a. se propaga como onda con vector de onda complejo; b. se propaga con la velocidad del sonido; c. se propaga como una onda amortiguada; d. como onda plana pero con velocidad alta; e. como onda plana pero doblando la frecuencia. → **a** (Est. c ✘). Para $\omega>\omega_{max}$ el $q$ es complejo (decaimiento evanescente); c es su descripción coloquial. Ambigua: se deja **a** por consistencia con la nota 11/20.

**6. (vib.3)** El número de modos normales de vibración posibles en un sólido se puede determinar tomando la cuerda vibrante como modelo. Es válido porque: a. una cuerda tiene la misma estructura que el sólido; b. la velocidad de propagación de las ondas en una cuerda es similar a esa en el sólido; c. es posible encontrar un número de soluciones independientes de la ecuación diferencial de la cuerda que satisfagan las condiciones de frontera; d. las ecuaciones diferenciales que rigen la oscilación de la cuerda y del sólido son de orden diferente; e. las condiciones de frontera para el sólido y la cuerda son diferentes. → **c** (Est. b ✘).

**7. (vib.2)** Dinámicamente, una longitud máxima $\lambda=2a$ implica que: a. los átomos oscilan en fase; b. las oscilaciones deben ser longitudinales; c. las oscilaciones deben corresponder a un modo óptico; d. los átomos oscilan en contrafase; e. los átomos no oscilan. → **d** (Est. c ✘). (La nota habla de "máxima" por la mínima física $\lambda=2a$ en $q=\pi/a$.)

**8. (vib.1)** Un medio dispersivo está caracterizado por: a. ser un medio con una densidad alta; b. la velocidad de grupo es cero; c. la velocidad de fase es cero; d. la velocidad de grupo es igual a la de fase; e. la velocidad de fase es diferente que la velocidad de grupo. → **e** (Est. e ✔).

**9. (vib.3)** La condición de Bragg aparece en el contexto de las vibraciones de red debido a: a. el campo acústico es de la misma naturaleza que el campo electromagnético; b. la energía de un fonón es comparable a la energía de un fotón; c. la red es periódica; d. el campo acústico tiene naturaleza ondulatoria; e. el campo acústico tiene naturaleza ondulatoria y la red es periódica. → **e** (Est. e ✔).

**10. (vib.3)** Para una red monoatómica unidimensional se encuentran tres modos de oscilación acústicos (dos transversales y uno longitudinal). La frecuencia del longitudinal es mayor que la de los transversales. Se explica de manera simple basándose en: a. las reglas de la mecánica cuántica; b. la configuración de carga de los iones; c. las leyes de la mecánica de Newton; d. las masas de los iones; e. ninguna de las anteriores. → **c** (Est. c ✔).

**11. (vib.6 / fermi3d.1)** Metal a $T=0$ K, ¿cómo se define $E_F$ en términos de la ocupación de los estados electrónicos? a. energía promedio de todos los electrones de conducción; b. energía del estado cuántico ocupado más alto en el estado fundamental del gas de electrones; c. energía del estado cuántico ocupado más bajo en el estado fundamental; d. nivel de energía donde la probabilidad de encontrar un electrón es exactamente 0.5; e. energía mínima requerida para remover el electrón completamente del metal. → **b** (Est. b ✔). d es $\mu(T>0)$; e es la función trabajo.

**12. (vib.4)** ¿Cómo cambia el ancho de la brecha de frecuencia prohibida si las dos masas $M$ y $m$ se aproximan a valores iguales ($M\to m$)? a. permanece constante porque depende solo de la constante de fuerza $C$; b. permanece constante porque el sólido como tal es eléctricamente neutro; c. se estrecha y desaparece por completo cuando $M=m$; d. la rama acústica absorbe completamente la rama óptica; e. se expande hasta su ancho máximo posible. → **c** (Est. c ✔). Brecha $=\sqrt{2C/m}-\sqrt{2C/M}\to0$.

**13. (vib.4)** ¿Cuál es la velocidad de grupo de los modos fonónicos en el límite de la zona de Brillouin ($q=\pi/a$)? a. igual a la velocidad del sonido en el material; b. cero para la rama acústica, pero máxima para la rama óptica; c. cero para la rama óptica, pero máxima para la rama acústica; d. cero para ambas ramas, acústica y óptica; e. infinita, porque se rompe la condición de onda estacionaria. → **d** (Est. b ✘).

**14. (vib.4)** Para una constante de fuerza $C$ fija, si se aumenta simultáneamente la masa de ambos átomos, ¿cómo se ven afectadas las frecuencias de la rama óptica? a. las frecuencias en toda la rama óptica disminuyen; b. aumentan debido a la inercia añadida; c. permanecen inalteradas porque la relación de masas se mantiene constante; d. la rama óptica se desplaza hacia arriba, mientras que la acústica hacia abajo; e. la rama óptica se desplaza hacia abajo, mientras que la acústica hacia arriba. → **a** (Est. a ✔). $\omega\propto1/\sqrt{\text{masa}}$ en ambas ramas.

**15. (vib.4)** En el límite de la zona de Brillouin ($q=\pi/a$), ¿qué átomos se mueven en la rama óptica si $M>m$? a. ambos con amplitudes iguales y desfasados; b. todos permanecen inmóviles; c. solo los más pesados ($M$) se mueven, los ligeros ($m$) inmóviles; d. solo los más ligeros ($m$) se mueven, los pesados ($M$) inmóviles; e. ambos con amplitudes iguales y en fase. → **d** (Est. d ✔).

**16. (vib.5)** ¿Qué distingue un proceso Umklapp (U) de un proceso normal (N) en la dispersión fonón-fonón? a. el momento total del cristal se conserva en los N, pero cambia en un vector de red recíproca distinto de cero en los U; b. los N involucran fonones acústicos, mientras que los U solo ópticos; c. los U ocurren solo en el cero absoluto, mientras que los N predominan a altas temperaturas; d. la energía se conserva en los N, pero se pierde en la red en los U; e. estrictamente, los dos procesos son iguales porque ambos ocurren en la primera zona de Brillouin. → **a** (Est. c ✘).

**17. (vib.5)** ¿Por qué los procesos Umklapp son en gran medida responsables de la resistencia térmica en aislantes puros a altas temperaturas? a. porque pueden redirigir el flujo neto de energía (flujo de fonones) y, por lo tanto, impedir el flujo de calor; b. porque reducen la frecuencia de todos los fonones a cero; c. porque reducen la velocidad del sonido en el cristal a cero; d. porque convierten los fonones en electrones, que son conductores de calor menos eficientes; e. en realidad los procesos Umklapp ocurren a temperaturas bajas. → **a** (Est. e ✘).

**18. (vib.5)** ¿Qué energía o vector de onda mínimo se requiere típicamente para que ocurra un proceso de inversión de polaridad? (el límite de la 1ZB está en $q=\pi/a$) a. el vector de onda debe ser exactamente cero; b. los fonones involucrados deben tener vectores de onda del orden de la mitad del vector de red recíproca ($|q|\approx|G|/2$); c. es suficiente que un fonón tenga un vector de onda cercano a cero; d. los fonones deben ser ópticos con energía máxima; e. los fonones deben ser ópticos con energía mínima. → **b** (Est. b ✔).

**19. (vib.5)** A temperaturas muy bajas (cercanas a 0 K), ¿cómo depende la conductividad térmica $\kappa$ de un cristal aislante puro de tamaño finito de la temperatura? a. $\kappa\propto T^3$; b. $\kappa\propto T^2$; c. $\kappa\propto T$; d. $\kappa\propto1/T$; e. no hay dependencia con $T$. → **a** (Est. d ✘). $\ell$ fija por el tamaño, $C_v\propto T^3$.

**20. (vib.5)** ¿Por qué los modos de fonones ópticos suelen contribuir mucho menos a la conductividad térmica total de un cristal que los acústicos? a. los ópticos no pueden experimentar dispersión de Umklapp; b. solo pueden existir en materiales conductores de electricidad; c. tienen una velocidad de grupo muy pequeña o casi nula; d. poseen una carga térmica negativa que anula el flujo de calor; e. ninguna de las anteriores. → **c** (Est. c ✔).

## Pastel — lo más frecuente

1. **$E_F, T_F, v_F$ desde $n$** (en 4/4 exámenes).
2. **$T/T_F$ y $C_e=\tfrac{\pi^2}{2}R\,T/T_F$.**
3. **Gas de Fermi vs. gas clásico / aire.**
4. **Bandas casi libres** (aislante vs. conductor, zona de Brillouin).
5. $v_d$, $\ell$, $\tau$ en Drude; Hall; W-F; termoiónica.
