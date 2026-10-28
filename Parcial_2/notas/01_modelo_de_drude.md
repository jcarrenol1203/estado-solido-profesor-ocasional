# Conductividad eléctrica: modelo de Drude (bloque 1)

> **Nota de origen:** cubre las páginas 24-50 de `Diapositivas/Metales 2021.pdf`. Es el tratamiento clásico (cinético) de la conducción, con $m^*$ como masa efectiva (interacción e⁻-red) y $\tau$ como tiempo de relajación.

## 4. Ley de Ohm y ecuación de movimiento de Drude (`drude.1`)

**Relaciones macroscópicas** (alambre de longitud $L$, sección $A$): $I=V/R$, $J=I/A$, $E\,L=V$, $R=\rho L/A$, $\sigma=1/\rho$, y la **ley de Ohm** $\mathbf J=\sigma\mathbf E$. [p. 24-25]
- Es una realidad **experimental**, no una consecuencia de un principio fundamental: describe cómo se comportan conductores reales en rangos accesibles de $T$, $E$. Un modelo plausible debe llevar a la ley de Ohm y explicar por qué falla en condiciones extremas (campos muy altos destruyen el metal). [p. 25-26]

**Ecuación dinámica:** fuerza del campo $\mathbf F_0=-e\mathbf E$ y fricción $\mathbf F_{fric}\sim-m^*\mathbf v/\tau$ (colisión del e⁻ con el resto del medio; $\tau$ = tiempo de colisión). [p. 27]

$$m^*\frac{d\mathbf v}{dt}=-e\mathbf E-\frac{m^*\mathbf v}{\tau}$$

Teoría cinética: la colisión es un evento **instantáneo** (cambio abrupto de $\mathbf v$). Estado estacionario ($d\mathbf v/dt=0$): [p. 28]

$$\mathbf v_d=-\frac{e\tau}{m^*}\mathbf E\quad(\text{velocidad de deriva})$$

$\mathbf v_d$ se superpone a la velocidad aleatoria $v_r$ (térmica); $v_r\gg v_d$; $\tfrac12 m v_r^2=\tfrac32k_BT$. Con $E=0$ la velocidad neta es cero (distribución simétrica en $v_x$) y $I=0$; con $E\neq0$ la distribución se desplaza una cantidad $v_d$. [p. 29]

**Densidad de corriente:** los $N$ e⁻/volumen (carga $-e$) se mueven con $v_d$; en $dt$ cruzan un área $A$ los e⁻ del volumen $A\,v_d\,dt$. [p. 30]

$$\mathbf J=-Ne\,\mathbf v_d=\frac{Ne^2\tau}{m^*}\mathbf E\ \Rightarrow\ \boxed{\sigma=\frac{Ne^2\tau}{m^*}}$$

### Puntos clave para dominar este tema
- Escribir la ecuación de Drude $m^*\dot{\mathbf v}=-e\mathbf E-m^*\mathbf v/\tau$ y resolver el estacionario $v_d=-e\tau E/m^*$.
- Deducir $\mathbf J=-Nev_d$ y $\sigma=Ne^2\tau/m^*$ (ley de Ohm microscópica).
- Explicar que $v_r\gg v_d$, que $J$ neta viene solo de $v_d$, y que la ley de Ohm es empírica con rango de validez.
- Recordar $v_d=I/(neA)$ para un alambre (usado en `P-2025-01` y en el taller).

---

## 5. Tiempo de relajación, camino libre medio, movilidad (`drude.2`)

**Significado de $\tau$:** si se aplica $E$ por un tiempo largo y se apaga en $t=0$, la deriva decae: [p. 31]

$$m^*\frac{dv_d}{dt}=-\frac{m^*}{\tau}v_d\ \Rightarrow\ v_d(t)=v_{d,0}\,e^{-t/\tau}\qquad(\tau\sim10^{-14}\text{ s})$$

**Población de "sobrevivientes"** (sin colisión): la probabilidad de colisión en $dt$ es $dt/\tau$, entonces $dn=-\frac1\tau n(t)\,dt$ → $n(t)=n_0e^{-t/\tau}$. El tiempo promedio de supervivencia es $t_{av}=\int t\,e^{-t/\tau}dt/\int e^{-t/\tau}dt=\tau$. [p. 32-33]
- $1/\tau$ = frecuencia de colisión por partícula. Camino libre medio $\ell=v_r\tau$ ($\ell$ = distancia entre dos colisiones sucesivas). [p. 34]

$$\sigma=\frac{Ne^2\tau}{m^*}=\frac{Ne^2\ell}{m^*v_r}$$

**Movilidad** (velocidad por unidad de campo): [p. 34]

$$v=\mu E,\qquad \mu=\frac{e\tau}{m^*},\qquad \sigma=Ne\mu$$

**Tabla de órdenes de magnitud a ~300 K** [p. 35] (ej.): Na: $\sigma=2.11\times10^7\ \Omega^{-1}$m$^{-1}$, $N=2.5\times10^{28}$ m⁻³, $\tau=3.1\times10^{-14}$ s, $v_F=1.1\times10^6$ m/s, $\ell=350$ Å, $E_F=3.1$ eV (obs. 2.5), $m^*/m_0=1.2$. Cu: $\sigma=5.88\times10^7$, $N=8.45\times10^{28}$, $\tau=2.7\times10^{-14}$ s, $E_F=7$ eV, $m^*/m_0=1$.

**Metales vs. aislantes:** $\sigma_m\approx10^7\ \Omega^{-1}$m$^{-1}$ (Ag, 300 K), aislantes $\sigma_i\approx10^{-16}$: $\sigma_m/\sigma_i\approx10^{23}$; semiconductores $\sigma\sim1$. Explicación: $\sigma\propto N\tau/m^*$; en metales $N\sim10^{29}$ m⁻³ y $v_r\approx v_F\sim10^6$ m/s; en semiconductores $N\sim10^{20}$ y $v_r\approx10^4$ m/s (con $v_r=(3k_BT/m^*)^{1/2}$ y $m^*\sim0.2\,m_0$). [p. 36]

**Magnitudes típicas** [p. 36-37]: $v_r\approx v_F\sim10^6$ m/s; con $e\sim10^{-19}$ C, $\tau\sim10^{-14}$ s, $m^*\sim10^{-30}$ kg, $E\sim10$ V/m resulta $v_d\sim10^{-2}$ m/s, así $v_d/v_r\sim10^{-8}$.

**Efecto Joule:** la potencia absorbida por el sistema de e⁻ del campo es $W_{abs}=N F v_d=N(-eE)(-e\tau E/m^*)=\frac{Ne^2\tau}{m^*}E^2=\sigma E^2$; igualando la disipada: $\frac{dQ}{dt}=\mathbf J\cdot\mathbf E=\sigma E^2=\rho J^2$ → pérdida de potencia en un alambre $=I^2R$. [p. 37] (Problema `T-SS2020 #5`.)

### Puntos clave para dominar este tema
- Interpretar $\tau$: decaimiento $e^{-t/\tau}$, vida media de supervivencia, $1/\tau$ = frecuencia de colisión.
- Relacionar $\ell=v\tau$ y escribir $\sigma$ con $\ell$ y con la movilidad $\mu=e\tau/m^*$.
- Estimar órdenes de magnitud: $v_d\sim10^{-2}$ m/s vs. $v_r\sim10^6$ m/s; $\tau\sim10^{-14}$ s; $\ell\sim10^2$ Å.
- Explicar por qué $\sigma_m/\sigma_i\sim10^{23}$ ($N$ y $v_r$ muy distintos) y demostrar $P=\sigma E^2\Rightarrow I^2R$.

---

## 6. Origen de $\tau$: dispersión por la red, ondas de materia y regla de Matthiessen (`drude.3`)

**¿Qué colisiones destruyen $v_d$ (y $J$)?** Las interacciones e⁻-e⁻ **conservan** el momento total, por lo tanto conservan $J$: **no** pueden cambiar $v_d$. Solo cambian $v_d$ las colisiones e⁻-red (imperfecciones, fonones, impurezas), que no conservan el momento del e⁻. [p. 38-39]

**El problema experimental:** $\ell=v_r\tau\approx10^6\cdot10^{-14}=10^{-8}$ m $\approx10^2$ Å, es decir **$\ell>20a$** — mucho mayor que el espaciado atómico. Los iones no pueden estar "chocando" como bolas rígidas. [p. 39]

**Respuesta cuántica:** el e⁻ es una onda de materia, $\lambda_{e}=h/(m v_r)$. Una **red periódica perfecta no dispersa ni difracta** la onda (salvo cuando se cumple la condición de Bragg): cada ion absorbe energía de la onda y la re-emite en nueva dirección, pero la dirección/intensidad total no se modifica por interferencia constructiva (igual que Rx, neutrones, e⁻ en cristales). En un cristal perfecto $\tau\to\infty$. [p. 40-42]

**Causas reales de dispersión** ($\ell\sim10^2$ Å): vibración térmica de la red (**fonones**), e **imperfecciones estáticas** (impurezas, defectos cristalinos). Un fonón no transporta carga y no conserva $\mathbf p$: tras la colisión el e⁻ puede viajar en dirección opuesta, $J$ se revierte aunque el momento total (e⁻+fonón) se conserve. [p. 42-44]

**Regla de Matthiessen:** los mecanismos son independientes, las probabilidades de dispersión se suman: [p. 44-45]

$$\frac1\tau=\frac1{\tau_{ph}(T)}+\frac1{\tau_{imp}}\ \Rightarrow\ \rho=\frac{m^*}{Ne^2}\left(\frac1{\tau_{imp}}+\frac1{\tau_{ph}(T)}\right)=\rho_{imp}+\rho_{ph}(T)$$

Para $T\to0$: $\tau_{ph}\to\infty$ y $\rho\to\rho_{imp}=$ cte (**resistividad residual**, depende de la pureza). $\rho_{ph}(T)$ crece con $T$. [p. 45]

**Cálculos de $\tau_i$ y $\tau_{ph}$ (teoría cinética):** [p. 46-48]
- Impurezas (esfera rígida, sección eficaz $\sigma_i\sim\pi r^2$): $\ell_i=1/(N_i\sigma_i)$, $\tau_i=\ell_i/v_r=1/(N_i\sigma_iv_r)$ → $\rho_i\propto N_i$.
- Fonones: sección eficaz $\sigma_{ph}=\pi\langle x^2\rangle$ (área barrida por el ion que vibra con amplitud $x$), $\ell_{ph}=1/(N_{ion}\sigma_{ph})$. Con el oscilador armónico, $\tfrac12M\omega^2\langle x^2\rangle=\langle E\rangle$; usando Einstein, $\langle E\rangle=\hbar\omega/(e^{\hbar\omega/k_BT}-1)$, con $\theta_E=\hbar\omega/k_B$ resulta
  - $T\gg\theta_E$: $\rho_{ph}(T)\sim T/\theta_E\to\ \rho_{ph}\propto T$ (**lineal**).
  - $T\ll\theta_E$: $\rho_{ph}\sim e^{-\theta_E/T}$ (Einstein), pero el **experimento** da $\rho_{ph}\sim T^5$ → se necesita el **modelo de Debye** (movimiento acoplado de iones vecinos, no independientes). [p. 49]
- Comportamiento lineal a altas $T$ (Na: recta para $T\gtrsim$ ~20-100 K). [p. 43]

**Desviaciones de Matthiessen:** ej. **efecto Kondo** (Cu con impurezas de Fe: dispersión adicional de e⁻ por espín magnético; $\rho$ aumenta al bajar $T$). Otras: particularidades de la estructura de bandas. [p. 50]

### Puntos clave para dominar este tema
- Explicar por qué las colisiones e⁻-e⁻ no cambian $v_d$ ni $J$ (conservan el momento total) y cuáles sí (e⁻-red: fonones, impurezas).
- Resolver la paradoja $\ell\sim100$ Å $\gg a$: un cristal **perfecto** no dispersa las ondas de materia; solo las desviaciones de la periodicidad (condición de Bragg aparte).
- Enunciar y usar la **regla de Matthiessen** ($\rho=\rho_{imp}+\rho_{ph}(T)$, residual a $T\to0$).
- Dar los límites de $\rho_{ph}$: $\propto T$ a $T\gg\theta$, $\propto T^5$ experimental a $T\ll\theta$ (Debye), y por qué Einstein (exponencial) no basta.
- Mencionar el efecto Kondo como violación de Matthiessen.
- Mostrar (con equipartición clásica, $v\propto\sqrt T$) que $\rho\propto T^{3/2}$ si la dispersión fuese clásica (`T-2025-II #2`): con $\ell=1/(N\sigma_{ph})$ y $\sigma_{ph}\propto\langle x^2\rangle\propto T$ resulta $\rho\propto\sigma_{ph}\,v\propto T\cdot T^{1/2}=T^{3/2}$.
