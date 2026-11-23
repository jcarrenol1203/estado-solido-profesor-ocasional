# P04 · Práctica resuelta: gas de Fermi 3D (`fermi3d.1`, `fermi3d.2`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T04_gas_de_fermi_3D.md`. Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $k_B=1.381\times10^{-23}$ J/K, 1 eV $=1.602\times10^{-19}$ J. Cada cifra se recalculó con Python. (Con estas constantes el $E_F$ del Cu sale 7.02 eV; los exámenes redondean a 7.05 eV.)

---

## P.fermi3d.1.1 — Deducir $k_F$, $E_F$ y $v_F$ (deducción)

**Enunciado.** Con condiciones periódicas en un cubo de lado $L$, deduce $k_F=(3\pi^2N/V)^{1/3}$ (diap. 62-66; Pavlov 6.48-6.56).

**Solución.**

1. Ondas planas $\psi_{\mathbf k}=e^{i\mathbf k\cdot\mathbf r}$; $\psi(x+L)=\psi(x)\Rightarrow e^{ik_xL}=1\Rightarrow k_x=2\pi n_x/L$, $n_x\in\mathbb Z$ (idem $y,z$).
2. Cada terna $(n_x,n_y,n_z)$ ocupa en el espacio $\mathbf k$ un volumen $(2\pi/L)^3=8\pi^3/V$.
3. Estado fundamental: se llenan los $\mathbf k$ de menor energía ⇒ esfera de radio $k_F$ (energía $\varepsilon=\hbar^2k^2/2m$ crece con $|\mathbf k|$).
4. Número de ternas dentro de la esfera: $\dfrac{\tfrac43\pi k_F^3}{8\pi^3/V}=\dfrac{Vk_F^3}{6\pi^2}$.
5. Cada terna aloja **2 e⁻** (espín ↑↓): $N=2\dfrac{Vk_F^3}{6\pi^2}=\dfrac{Vk_F^3}{3\pi^2}$ ⇒ $k_F=\left(3\pi^2\dfrac NV\right)^{1/3}$.
6. $E_F=\dfrac{\hbar^2k_F^2}{2m}=\dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ y $v_F=\dfrac{\hbar k_F}{m}$ (de $\mathbf p=\hbar\mathbf k=m\mathbf v$).

**Resultado.** $k_F=(3\pi^2n)^{1/3}$, $E_F=\dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$, $v_F=\dfrac{\hbar}{m}(3\pi^2n)^{1/3}$: dependen **solo** de $n$. Pavlov obtiene lo mismo con celdas de fase $(2\pi\hbar)^3/V$ y $N=\int2VN(E)f\,dE$ (6.55-6.56).

---

## P.fermi3d.1.2 — $E_F$, $T_F$, $v_F$ del Na, Cu y Al (numérico)

**Enunciado.** Calcula $k_F$, $E_F$, $T_F$ y $v_F$ para Na (bcc, $a=4.225$ Å, 1 e⁻/átomo), Cu ($8.45\times10^{28}$ m⁻³) y Al ($Z_v=3$, $n=1.81\times10^{29}$ m⁻³). Compara con la diap. 67.

**Solución.** $\hbar^2/2m=6.104\times10^{-39}$ J·m² $=3.81$ eV·Å².

1. **Na:** $n=2/a^3=2/(4.225\times10^{-10})^3=2.65\times10^{28}$ m⁻³. $3\pi^2n=7.85\times10^{29}$ ⇒ $k_F=9.22\times10^{9}$ m⁻¹ $=0.922$ Å⁻¹. $E_F=3.81\times0.922^2=3.24$ eV; $T_F=3.24/8.617\times10^{-5}=3.76\times10^4$ K; $v_F=\hbar k_F/m=1.07\times10^6$ m/s.
2. **Cu:** $3\pi^2n=2.50\times10^{30}$ ⇒ $k_F=1.36\times10^{10}$ m⁻¹ ⇒ $E_F=7.02$ eV, $T_F=8.15\times10^4$ K, $v_F=1.57\times10^6$ m/s.
3. **Al:** $3\pi^2n=5.36\times10^{30}$ ⇒ $k_F=1.75\times10^{10}$ m⁻¹ ⇒ $E_F=11.7$ eV, $T_F=1.35\times10^5$ K, $v_F=2.03\times10^6$ m/s.
4. Diap. 67 (Na): $N/V=3\times10^{22}$ cm⁻³ (redondeado), $k_F\approx10^8$ cm⁻¹, $E_F\approx3.5$ eV, $T_F\approx40\,000$ K. Con **su** $n=3\times10^{28}$ m⁻³: $k_F=0.961$ Å⁻¹, $E_F=3.52$ eV ✔; la diferencia con 3.24 eV viene de redondear $n$ ($3$ vs. $2.65$).

**Resultado.**

| Metal | $n$ (m⁻³) | $k_F$ (Å⁻¹) | $E_F$ (eV) | $T_F$ (K) | $v_F$ (m/s) |
|---|---|---|---|---|---|
| Na | $2.65\times10^{28}$ | 0.922 | 3.24 | $3.8\times10^4$ | $1.07\times10^6$ |
| Cu | $8.45\times10^{28}$ | 1.36 | 7.02 | $8.2\times10^4$ | $1.57\times10^6$ |
| Al | $1.81\times10^{29}$ | 1.75 | 11.7 | $1.35\times10^5$ | $2.03\times10^6$ |

$E_F\propto n^{2/3}$ (Al/Na: $(6.8)^{2/3}=3.6$ ✔).

---

## P.fermi3d.1.3 — $\langle v\rangle=\tfrac34v_F$ y $\langle E\rangle=\tfrac35E_F$ (deducción)

**Enunciado.** Demuestra ambos promedios a $T=0$ (se usan en `P-2025-2S #2` y `P-2025-01 #3a`).

**Solución.** A $T=0$ los e⁻ están uniformes en la esfera $0\le k\le k_F$ ⇒ el peso es el volumen de la cascarilla $4\pi k^2dk$.

1. $\langle v\rangle=\dfrac{\int_0^{k_F}\frac{\hbar k}{m}k^2dk}{\int_0^{k_F}k^2dk}=\dfrac\hbar m\cdot\dfrac{k_F^4/4}{k_F^3/3}=\dfrac34\dfrac{\hbar k_F}{m}=\dfrac34v_F$.
2. $\langle E\rangle=\dfrac{\int_0^{k_F}\frac{\hbar^2k^2}{2m}k^2dk}{\int_0^{k_F}k^2dk}=\dfrac{\hbar^2}{2m}\cdot\dfrac{k_F^5/5}{k_F^3/3}=\dfrac35\dfrac{\hbar^2k_F^2}{2m}=\dfrac35E_F$.
3. Chequeo con $D(\varepsilon)\propto\varepsilon^{1/2}$: $\langle E\rangle=\dfrac{\int_0^{E_F}\varepsilon^{3/2}d\varepsilon}{\int_0^{E_F}\varepsilon^{1/2}d\varepsilon}=\dfrac{\frac25E_F^{5/2}}{\frac23E_F^{3/2}}=\dfrac35E_F$ ✔.

**Resultado.** $\langle v\rangle=\tfrac34v_F$ (no $v_F/2$) y $\langle E\rangle=\tfrac35E_F$ (no $\tfrac12E_F$). En el Cu: $\langle v\rangle=1.18\times10^6$ m/s y $\langle E\rangle=4.21$ eV.

---

## P.fermi3d.1.4 — Condiciones periódicas vs. paredes rígidas y densidad de $\mathbf k$ (numérico + conceptual)

**Enunciado.** (a) Muestra que con paredes rígidas ($n_i>0$, $k_i=n_i\pi/L$) se obtiene el mismo $k_F$. (b) Para $L=1$ cm, ¿cuántos estados caben a lo largo del radio de la esfera de Cu? (c) ¿Qué ventaja tienen las periódicas?

**Solución.**

1. (a) Paredes rígidas: $k_i=n_i\pi/L$ con $n_i=1,2,\dots$ ⇒ volumen por estado $(\pi/L)^3$ pero **solo el octante** $k_i>0$: $N=2\cdot\dfrac{\frac18\cdot\frac43\pi k_F^3}{(\pi/L)^3}=2\cdot\dfrac{\pi k_F^3/6}{\pi^3/V}=\dfrac{Vk_F^3}{3\pi^2}$ ✔ el mismo $k_F$.
2. (b) $\Delta k=2\pi/L=2\pi/10^{-2}=6.3\times10^2$ m⁻¹; $k_F/\Delta k=1.36\times10^{10}/6.3\times10^2=2.2\times10^7$ estados a lo largo del radio ⇒ $\mathbf k$ es un **cuasi-continuo**.
3. (c) Periódicas (diap. 63): (1) se puede suponer un cristal infinito; (2) se desprecia la influencia de las fronteras; las soluciones son ondas **viajeras** que transportan corriente ($\hbar\mathbf k\neq0$), a diferencia de las estacionarias (suma de $\pm k$, momento neto 0).

**Resultado.** Mismo $N(k_F)$ con ambas condiciones; el espaciado $\Delta k\sim10^{3}$ m⁻¹ es despreciable frente a $k_F\sim10^{10}$ m⁻¹.

---

## P.fermi3d.2.1 — Deducir $D(\varepsilon)$ y $D(E_F)=3N/2E_F$ (deducción)

**Enunciado.** A partir de $N(\varepsilon)$ halla $D(\varepsilon)$ (diap. 68-69; Pavlov 6.53).

**Solución.**

1. Número de estados con energía $\le\varepsilon$: $k(\varepsilon)=\sqrt{2m\varepsilon}/\hbar$ en $N=\dfrac{Vk^3}{3\pi^2}$ ⇒ $N(\varepsilon)=\dfrac V{3\pi^2}\left(\dfrac{2m\varepsilon}{\hbar^2}\right)^{3/2}$.
2. $D(\varepsilon)=\dfrac{dN}{d\varepsilon}=\dfrac V{2\pi^2}\left(\dfrac{2m}{\hbar^2}\right)^{3/2}\varepsilon^{1/2}$ (incluye el factor 2 de espín).
3. Atajo: $N\propto\varepsilon^{3/2}\Rightarrow\ln N=\tfrac32\ln\varepsilon+c\Rightarrow\dfrac{dN}{N}=\dfrac32\dfrac{d\varepsilon}{\varepsilon}\Rightarrow D(E_F)=\dfrac{dN}{d\varepsilon}\Big|_{E_F}=\dfrac{3N}{2E_F}$.
4. Consistencia con Pavlov (6.53): $N(E)=\frac1{(2\pi)^2}(2m/\hbar^2)^{3/2}E^{1/2}$ por espín y por volumen; multiplicando por $2V$ se recupera $D(\varepsilon)$ de la diapositiva ✔.

**Resultado.** $D(\varepsilon)\propto\varepsilon^{1/2}$, $D(E_F)=3N/2E_F$.

---

## P.fermi3d.2.2 — $D(E_F)$ del Cu y cuántos estados hay en $k_BT$ (numérico)

**Enunciado.** Calcula $D(E_F)$ por unidad de volumen para el Cu y el número de e⁻ en una franja $k_BT$ a 300 K.

**Solución.**

1. $D(E_F)/V=\dfrac{3n}{2E_F}=\dfrac{3\times8.45\times10^{28}}{2\times7.02}=1.80\times10^{28}$ eV⁻¹m⁻³.
2. Estados en la franja: $D(E_F)k_BT/V=1.80\times10^{28}\times0.02586=4.7\times10^{26}$ m⁻³.
3. Fracción: $4.7\times10^{26}/8.45\times10^{28}=5.5\times10^{-3}=\tfrac32\dfrac{k_BT}{E_F}$ ✔ (≈ $T/T_F=3.7\times10^{-3}$ de la estimación de la diap. 57, mismo orden).

**Resultado.** $D(E_F)/V=1.8\times10^{28}$ eV⁻¹m⁻³; solo ~0.5 % de los e⁻ caen en la franja térmica ⇒ $C_e$ pequeño. Y $C_e=\tfrac{\pi^2}{3}k_B^2D(E_F)T$ (Pavlov 6.64) enlaza `fermi3d.2` con `cal.2`.

---

## P.fermi3d.2.3 — $E_0$, $P$ y $B$ del Cu (deducción + numérico)

**Enunciado.** Deduce $E_0=\tfrac35NE_F$, $P=\tfrac25nE_F$ y $B=\tfrac23nE_F$ y evalúalos para Cu.

**Solución.**

1. $E_0=\int_0^{E_F}\varepsilon D\,d\varepsilon$ con $D=\tfrac32\dfrac N{E_F^{3/2}}\varepsilon^{1/2}$ (de $D(\varepsilon)=\tfrac32N\varepsilon^{1/2}/E_F^{3/2}$): $E_0=\tfrac32\dfrac N{E_F^{3/2}}\cdot\tfrac25E_F^{5/2}=\tfrac35NE_F$.
2. $E_F\propto V^{-2/3}\Rightarrow E_0\propto V^{-2/3}$ ⇒ $P=-\dfrac{\partial E_0}{\partial V}=\dfrac23\dfrac{E_0}V=\dfrac25nE_F$.
3. $P\propto V^{-5/3}$ ⇒ $B=-V\dfrac{\partial P}{\partial V}=\dfrac53P=\dfrac23nE_F$.
4. Cu: $E_0/N=4.21$ eV ⇒ por mol $E_0=4.21\times96.485=407$ kJ/mol (vs. $\tfrac32RT=3.7$ kJ/mol clásico a 300 K: 109 veces menor).
5. $P=0.4\times8.45\times10^{28}\times7.02\times1.602\times10^{-19}=3.80\times10^{10}$ Pa $=38.0$ GPa; $B=\tfrac53P=63.4$ GPa.

**Resultado.** $E_0=\tfrac35NE_F$ (407 kJ/mol en Cu), $P=38$ GPa, $B=63$ GPa (el experimento da ≈134 GPa: el modelo libre acierta el orden; `T-2025-II #5`). Es la **presión de degeneración**: existe a $T=0$ por Pauli.

---

## Checklist de práctica (P04)

- [ ] P.fermi3d.1.1 Deducir $k_F$, $E_F$, $v_F$ contando estados
- [ ] P.fermi3d.1.2 $k_F$, $E_F$, $T_F$, $v_F$ de Na, Cu y Al
- [ ] P.fermi3d.1.3 Deducir $\langle v\rangle=\tfrac34v_F$ y $\langle E\rangle=\tfrac35E_F$
- [ ] P.fermi3d.1.4 Paredes rígidas vs. periódicas y espaciado de $\mathbf k$
- [ ] P.fermi3d.2.1 Deducir $D(\varepsilon)$ y $D(E_F)=3N/2E_F$
- [ ] P.fermi3d.2.2 $D(E_F)$ del Cu y e⁻ en la franja $k_BT$
- [ ] P.fermi3d.2.3 $E_0$, $P$ y $B$ del Cu
