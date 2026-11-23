# P02 · Práctica resuelta: modelo de Drude (`drude.1`, `drude.2`, `drude.3`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T02_modelo_de_drude.md`. Constantes como en `P01`; datos del Cu: $\sigma=5.88\times10^7$ Ω⁻¹m⁻¹, $n=8.45\times10^{28}$ m⁻³, $m^*=m_0$, $v_F=1.57\times10^6$ m/s, $a=3.61$ Å. Cada cifra se recalculó con Python.

---

## P.drude.1.1 — Deducir $\sigma=Ne^2\tau/m^*$ (deducción)

**Enunciado.** Parte de la ecuación de Drude y llega a la ley de Ohm microscópica (diap. 27-30; Pavlov §6.3, 6.92-6.96).

**Solución.**

1. Ecuación de movimiento (fuerza del campo + fricción de las colisiones): $m^*\dot{\mathbf v}=-e\mathbf E-m^*\mathbf v/\tau$.
2. Estado estacionario, $\dot{\mathbf v}=0$: $-e\mathbf E=m^*\mathbf v/\tau\Rightarrow\mathbf v_d=-\dfrac{e\tau}{m^*}\mathbf E$.
3. Densidad de corriente: en $dt$ cruzan un área $A\perp$ flujo los $N(Av_ddt)$ e⁻ del volumen $Av_ddt$, cada uno con carga $-e$ ⇒ $dI=-NeAv_d\Rightarrow\mathbf J=-Ne\mathbf v_d$.
4. Sustituyendo: $\mathbf J=-Ne\left(-\dfrac{e\tau}{m^*}\mathbf E\right)=\dfrac{Ne^2\tau}{m^*}\mathbf E$.
5. Comparando con $\mathbf J=\sigma\mathbf E$: $\boxed{\sigma=Ne^2\tau/m^*}$.
6. Pavlov llega a lo mismo: $\langle v\rangle=(eE/m)\tau$ (6.93) ⇒ $j=ne^2\tau E/m$ (6.94) ⇒ $\sigma=ne^2\tau/m$ (6.96).

**Resultado.** $\sigma=Ne^2\tau/m^*$ (signo de $e$ irrelevante: $e^2$). Es una relación **lineal**: ley de Ohm. Pavlov usa la distribución de Maxwell (6.92), pero el resultado solo depende de $\tau$ y $\langle v\rangle$, no de la forma de la distribución.

---

## P.drude.1.2 — $\tau$, $\ell$ y $\mu$ del cobre (numérico)

**Enunciado.** Con los datos del Cu halla $\tau$, el camino libre medio $\ell=v_F\tau$ (¿cuántos parámetros de red?) y la movilidad.

**Solución.**

1. $\tau=\dfrac{\sigma m^*}{Ne^2}=\dfrac{5.88\times10^7\times9.109\times10^{-31}}{8.45\times10^{28}\times(1.602\times10^{-19})^2}=\dfrac{5.356\times10^{-23}}{2.169\times10^{-9}}=2.47\times10^{-14}$ s.
2. $\ell=v_F\tau=1.57\times10^6\times2.47\times10^{-14}=3.88\times10^{-8}$ m $=388$ Å.
3. $\ell/a=388/3.61=107$ parámetros de red.
4. $\mu=e\tau/m^*=\dfrac{1.602\times10^{-19}\times2.47\times10^{-14}}{9.109\times10^{-31}}=4.34\times10^{-3}$ m²/V·s $=43$ cm²/V·s. Chequeo: $\sigma=Ne\mu=8.45\times10^{28}\times1.602\times10^{-19}\times4.34\times10^{-3}=5.88\times10^7$ ✔.

**Resultado.** $\tau=2.5\times10^{-14}$ s, $\ell\approx390$ Å $\approx107\,a$, $\mu=4.3\times10^{-3}$ m²/V·s. La diap. 35 trae $\tau=2.7\times10^{-14}$ s y $\ell=420$ Å (valores redondeados; 8 % de diferencia).

---

## P.drude.1.3 — Velocidad de deriva vs. velocidad aleatoria (numérico)

**Enunciado.** (a) Alambre de Cu de 1 mm² con 1 A: $E$, $v_d$, $v_d/v_F$. (b) Na con $E=10$ V/m ($m^*=1.2m_0$, $\tau=3.1\times10^{-14}$ s, diap. 35): $v_d$.

**Solución.**

1. (a) $J=I/A=1/10^{-6}=10^6$ A/m². $E=J/\sigma=10^6/5.88\times10^7=1.70\times10^{-2}$ V/m.
2. $v_d=J/(ne)=10^6/(8.45\times10^{28}\times1.602\times10^{-19})=7.39\times10^{-5}$ m/s $=0.074$ mm/s.
3. $v_d/v_F=7.39\times10^{-5}/1.57\times10^6=4.7\times10^{-11}$.
4. (b) $v_d=\dfrac{e\tau E}{m^*}=\dfrac{1.602\times10^{-19}\times3.1\times10^{-14}\times10}{1.2\times9.109\times10^{-31}}=4.5\times10^{-2}$ m/s; $v_d/v_F=4.5\times10^{-2}/1.07\times10^6=4\times10^{-8}$.

**Resultado.** (a) $v_d\approx0.07$ mm/s, $v_d/v_F\sim5\times10^{-11}$; (b) $v_d\approx4.5\times10^{-2}$ m/s. En ambos $v_d\ll v_r$: la corriente es un **pequeño desplazamiento** de la distribución (diap. 29). *(El $E=10$ V/m de la diap. 36 es altísimo para un metal: en Cu daría $J=5.9\times10^8$ A/m²; sirve solo como orden de magnitud.)*

---

## P.drude.2.1 — Población de sobrevivientes (deducción)

**Enunciado.** Demuestra $n(t)=n_0e^{-t/\tau}$ y que el tiempo medio sin colisión es $\tau$ (diap. 32-33).

**Solución.**

1. Probabilidad de colisión de una partícula en $dt$: $dt/\tau$. Cambio de la población que sigue sin chocar: $dn=-\dfrac{n(t)}{\tau}dt$.
2. $\dfrac{dn}{n}=-\dfrac{dt}{\tau}\Rightarrow\ln n=-t/\tau+c\Rightarrow n(t)=n_0e^{-t/\tau}$.
3. Tiempo medio: $t_{av}=\dfrac{\int_0^\infty t\,e^{-t/\tau}dt}{\int_0^\infty e^{-t/\tau}dt}$. El denominador es $\tau$. El numerador (por partes): $\int_0^\infty te^{-t/\tau}dt=\tau^2$. ⇒ $t_{av}=\tau^2/\tau=\tau$.
4. $\ell=v_rt_{av}=v_r\tau$ (diap. 34) y $1/\tau$ = colisiones por partícula y segundo ($\sim10^{14}$ s⁻¹).

**Resultado.** $n(t)=n_0e^{-t/\tau}$ y $t_{av}=\tau$. Interpretación: $\tau$ es a la vez la constante de decaimiento y el tiempo medio entre colisiones.

---

## P.drude.2.2 — Efecto Joule (numérico + deducción)

**Enunciado.** Cable de Cu de 10 m y 1 mm² con 5 A: (a) $R$ y $P$; (b) verifica $P=\sigma E^2\times$volumen.

**Solución.**

1. $R=\dfrac{L}{\sigma A}=\dfrac{10}{5.88\times10^7\times10^{-6}}=0.170$ Ω; $P=I^2R=25\times0.170=4.25$ W.
2. (b) $J=5/10^{-6}=5\times10^6$ A/m²; $E=J/\sigma=0.0850$ V/m; $\sigma E^2=5.88\times10^7\times(0.0850)^2=4.25\times10^5$ W/m³; volumen $=10\times10^{-6}=10^{-5}$ m³ ⇒ $P=4.25$ W ✔.
3. Deducción general (diap. 37): potencia que el campo cede a los e⁻: $W=N\,F\,v_d=N(-eE)\left(-\dfrac{e\tau E}{m^*}\right)=\dfrac{Ne^2\tau}{m^*}E^2=\sigma E^2$ por unidad de volumen; en el alambre $P=\sigma E^2AL=\dfrac{(EL)^2}{L/\sigma A}=\dfrac{V^2}{R}=I^2R$.

**Resultado.** $R=0.17$ Ω, $P=4.25$ W, y $\mathbf J\cdot\mathbf E=\rho J^2$ por unidad de volumen. La energía ganada entre choques se disipa **en la red** (los choques no conservan la energía del gas de e⁻).

---

## P.drude.2.3 — ¿Por qué $\sigma_m/\sigma_{sc}\sim10^7$? (numérico, estimación)

**Enunciado.** Usa $\sigma=Ne^2\ell/(m^*v_r)$ con los datos de la diap. 36 para comparar un metal ($N=10^{29}$ m⁻³, $v_r\sim10^6$ m/s) con un semiconductor ($N=10^{20}$ m⁻³, $v_r\sim10^4$ m/s, $\sigma\approx1$ Ω⁻¹m⁻¹).

**Solución.**

1. Con $\ell$ y $m^*$ comparables: $\dfrac{\sigma_m}{\sigma_{sc}}=\dfrac{N_m}{N_{sc}}\cdot\dfrac{v_{sc}}{v_m}=10^{9}\cdot10^{-2}=10^{7}$.
2. Coincide con el cociente de la diapositiva: $\sigma_m\approx10^7$ vs. $\sigma_{sc}\approx1$ ⇒ $10^7$ ✔.
3. Para el **aislante** ($\sigma_i\sim10^{-16}$, cociente $10^{23}$): con la misma fórmula y $v_i\sim10^4$ haría falta $N_i\approx10^{29}\cdot10^{-2}/10^{23}=10^4$ m⁻³ (estimación mía): casi **ningún** portador libre. La diapositiva no desglosa el $10^{23}$.

**Resultado.** $10^7$ entre metal y semiconductor sale de $N$ ($10^9$) y $v_r$ ($10^{-2}$). El factor $10^{23}$ con el aislante exige además $N$ prácticamente nulo; por eso la teoría clásica del e⁻ libre no explica por qué hay aislantes (diap. 26; Pavlov p. 236).

---

## P.drude.3.1 — La paradoja del camino libre (numérico)

**Enunciado.** Si los e⁻ chocaran como bolas con los iones (sección eficaz $\pi r^2$, $r_{Cu^+}\approx0.96$ Å, valor estándar), ¿qué $\ell$ y $\tau$ saldrían? Compáralos con el experimental.

**Solución.**

1. Clásico: $\ell=\dfrac1{N_{ion}\sigma}=\dfrac1{8.45\times10^{28}\times\pi(0.96\times10^{-10})^2}=4.1\times10^{-10}$ m $=4.1$ Å $\approx a$.
2. $\tau_{cl}=\ell/v_F=4.1\times10^{-10}/1.57\times10^6=2.6\times10^{-16}$ s.
3. Experimental (P.drude.1.2): $\ell=388$ Å, $\tau=2.5\times10^{-14}$ s.
4. Cociente: $388/4.1\approx95$.
5. Resolución cuántica (diap. 40-42): el e⁻ es una onda $\lambda=h/m^*v_r$ en una red **periódica**; una red perfecta no dispersa (interferencia), solo lo hacen vibraciones, impurezas y defectos.

**Resultado.** El choque clásico con iones daría $\ell\approx4$ Å, ~100 veces menor que lo observado: los e⁻ no "chocan con los iones", sino que se dispersan por las **desviaciones de la periodicidad**.

---

## P.drude.3.2 — Matthiessen con números (numérico)

**Enunciado.** Una muestra de Cu tiene $\rho(300\text{ K})=1.70\times10^{-8}$ Ω·m y $\rho(T\to0)=2\times10^{-10}$ Ω·m (datos de ejemplo). Halla $\rho_{imp}$, $\rho_{ph}(300)$, la razón de resistividad residual, $\tau_{imp}$, $\ell_{imp}$ y, suponiendo $\rho_{ph}\propto T$, $\rho(100\text{ K})$.

**Solución.**

1. $\rho_{imp}=2\times10^{-10}$ Ω·m (Matthiessen: $\rho=\rho_{imp}+\rho_{ph}(T)$, y $\rho_{ph}\to0$ si $T\to0$).
2. $\rho_{ph}(300)=1.70\times10^{-8}-2\times10^{-10}=1.68\times10^{-8}$ Ω·m.
3. Razón residual: $1.70\times10^{-8}/2\times10^{-10}=85$.
4. $\tau_{imp}=\dfrac{m^*}{Ne^2\rho_{imp}}=\dfrac{9.109\times10^{-31}}{8.45\times10^{28}(1.602\times10^{-19})^2\times2\times10^{-10}}=2.1\times10^{-12}$ s; $\ell_{imp}=v_F\tau_{imp}=3.3\ \mu$m.
5. $\rho(100)=\rho_{imp}+\rho_{ph}(300)\dfrac{100}{300}=2\times10^{-10}+5.6\times10^{-9}=5.8\times10^{-9}$ Ω·m, con $\tau(100)=7.2\times10^{-14}$ s.

**Resultado.** $\rho_{imp}=2\times10^{-10}$, $\rho_{ph}(300)=1.68\times10^{-8}$ Ω·m, razón 85, $\ell_{imp}=3.3\ \mu$m, $\rho(100)=5.8\times10^{-9}$ Ω·m **solo si** $T\gg\theta$ en ese rango (la proporcionalidad lineal falla para $T\lesssim\theta$, donde el experimento da $T^5$; diap. 49).

---

## P.drude.3.3 — Por qué $\rho_{ph}\propto T$ (deducción)

**Enunciado.** Con las diap. 46-48 y Pavlov §7.13 (p. 287), justifica $\rho_{ph}\propto T$ a $T\gg\theta$ y distingue del caso clásico $\propto T^{3/2}$.

**Solución.**

1. Sección eficaz del ion que vibra: $\Omega_{ion}\approx\pi\langle x^2\rangle$ (diap. 47).
2. Equipartición ($T\gg\theta_E$): $\tfrac12M\omega^2\langle x^2\rangle=k_BT\Rightarrow\langle x^2\rangle\propto T$ ⇒ $\Omega_{ion}\propto T$.
3. $\ell_{ph}=1/(N_{ion}\Omega_{ion})\propto1/T$.
4. $\tau_{ph}=\ell_{ph}/v$. En un metal degenerado la velocidad relevante es $v_F$, **independiente de $T$** ⇒ $\tau_{ph}\propto1/T$.
5. $\rho_{ph}=m^*/(Ne^2\tau_{ph})\propto T$ ✔. Pavlov (§7.13, p. 287): $n$ ≈ cte (gas degenerado), $\mu\propto1/T$ por dispersión en fonones ⇒ $\rho\propto T$.
6. Si el gas fuese **clásico** ($v\propto T^{1/2}$): $\rho\propto\Omega\,v\propto T\cdot T^{1/2}=T^{3/2}$ (`T-2025-II #2`, resuelto en `examenes_resueltos/`).

**Resultado.** $\rho_{ph}\propto T$ con gas de Fermi; $T^{3/2}$ con gas clásico; el experimento (lineal) apoya el gas de Fermi.

---

## Checklist de práctica (P02)

- [ ] P.drude.1.1 Deducir $\sigma=Ne^2\tau/m^*$ desde la ecuación de Drude
- [ ] P.drude.1.2 $\tau$, $\ell$ y $\mu$ del Cu a partir de $\sigma$
- [ ] P.drude.1.3 $v_d$ vs. $v_F$ en un alambre y en el Na
- [ ] P.drude.2.1 Deducir $n(t)=n_0e^{-t/\tau}$ y $t_{av}=\tau$
- [ ] P.drude.2.2 Efecto Joule: $R$, $P=I^2R$ y verificación con $\sigma E^2$
- [ ] P.drude.2.3 Estimar $\sigma_m/\sigma_{sc}$ con $N$ y $v_r$
- [ ] P.drude.3.1 Paradoja del camino libre: choque clásico vs. experimento
- [ ] P.drude.3.2 Regla de Matthiessen con números
- [ ] P.drude.3.3 Deducir $\rho_{ph}\propto T$ (y $T^{3/2}$ clásico)
