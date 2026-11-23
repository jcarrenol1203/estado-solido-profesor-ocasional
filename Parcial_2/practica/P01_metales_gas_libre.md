# P01 · Práctica resuelta: metales, gas 1D e interacciones (`metal.1`, `gas1d.1`, `interac.1`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T01_metales_gas_libre.md`. Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $e=1.602\times10^{-19}$ C, $k_B=1.381\times10^{-23}$ J/K, $N_A=6.022\times10^{23}$, 1 eV $=1.602\times10^{-19}$ J, $a_0=0.529$ Å. Densidades y masas atómicas: tablas estándar (no están en el PDF). Cada cifra fue recalculada con Python.

---

## P.metal.1.1 — Concentración de e⁻ de conducción (numérico)

**Enunciado.** Calcula $N$ (e⁻/cm³) para Cu ($Z_v=1$, $\rho=8.96$ g/cm³, $M=63.55$), Al ($Z_v=3$, 2.70, 26.98), Mg ($Z_v=2$, 1.74, 24.31) y Na ($Z_v=1$, 0.971, 22.99). ¿Cuál es el más denso en e⁻?

**Solución.** Fórmula de la diap. 10: $N=Z_vN_A\rho/M$.

1. Cu: $\rho/M=8.96/63.55=0.1410$ mol/cm³ ⇒ $N=1\times6.022\times10^{23}\times0.1410=8.49\times10^{22}$ cm⁻³ $=8.49\times10^{28}$ m⁻³.
2. Al: $\rho/M=2.70/26.98=0.1001$ ⇒ $N=3\times6.022\times10^{23}\times0.1001=1.81\times10^{23}$ cm⁻³.
3. Mg: $1.74/24.31=0.07158$ ⇒ $N=2\times6.022\times10^{23}\times0.07158=8.62\times10^{22}$ cm⁻³.
4. Na: $0.971/22.99=0.04223$ ⇒ $N=2.54\times10^{22}$ cm⁻³.

**Resultado.** Al ($1.81\times10^{23}$) > Mg ($8.62\times10^{22}$) ≈ Cu ($8.49\times10^{22}$) > Na ($2.54\times10^{22}$) cm⁻³. El Al gana por tener **3** e⁻ de valencia, no por ser más denso. *(Cu ≈ $8.45\times10^{28}$ m⁻³ de la diap. 35; Na real $2.5\times10^{28}$.)*

---

## P.metal.1.2 — ¿Cuánto del cristal ocupan los iones? (numérico, **diapositiva inconsistente**)

**Enunciado.** Na: bcc, $a=4.2$ Å (2 átomos/celda), radio del Na⁺ libre 0.98 Å. Halla la fracción de volumen ocupada por los iones y compárala con "≈15 %" de la diap. 7.

**Solución.**

1. Volumen de un ion: $V_{ion}=\tfrac43\pi(0.98)^3=3.94$ Å³ (la diapositiva dice 3.9 Å³ ✔).
2. Volumen de la celda: $a^3=4.2^3=74.1$ Å³ con 2 iones.
3. Fracción: $\dfrac{2\times3.94}{74.1}=0.106\approx10.6\,\%$. (Con $a=4.225$ Å: 10.5 %.)

**Resultado y comentario.** ≈ **10.5 %**, no 15 %. La diapositiva 7 da 15 %; con **sus propios datos** no cuadra (haría falta $r\approx1.1$ Å). Es un valor redondeado/inconsistente de la diapositiva: el mensaje físico no cambia (los iones ocupan una fracción pequeña, ~10-15 %, y el resto es el mar de e⁻), pero en un examen usa tu cálculo.

---

## P.metal.1.4 — $n$ desde la estructura cristalina y el parámetro de red (numérico)

**Enunciado.** Calcula la concentración de e⁻ de conducción $n=N/V$ de Na (bcc, $a=4.225$ Å, $Z_v=1$), K (bcc, 5.225 Å, 1), Li (bcc, 3.51 Å, 1), Cu (fcc, 3.61 Å, 1), Ag (fcc, 4.09 Å, 1) y Al (fcc, 4.05 Å, 3).

**Solución.** Átomos por celda cúbica: **bcc → 2**, **fcc → 4** (diap. 7-10: alcalinos bcc, nobles fcc). Volumen de la celda $a^3$.

1. $n=\dfrac{Z_v\times(\text{átomos/celda})}{a^3}$.
2. Na: $\dfrac{2}{(4.225\times10^{-10})^3}=\dfrac{2}{7.542\times10^{-29}}=2.65\times10^{28}$ m⁻³.
3. K: $\dfrac{2}{(5.225\times10^{-10})^3}=1.40\times10^{28}$ m⁻³.
4. Li: $\dfrac{2}{(3.51\times10^{-10})^3}=4.63\times10^{28}$ m⁻³.
5. Cu: $\dfrac{4}{(3.61\times10^{-10})^3}=8.50\times10^{28}$ m⁻³.
6. Ag: $\dfrac{4}{(4.09\times10^{-10})^3}=5.85\times10^{28}$ m⁻³.
7. Al: $\dfrac{3\times4}{(4.05\times10^{-10})^3}=1.81\times10^{29}$ m⁻³ (trivalente: ×3).

**Resultado.**

| Metal | estructura | $a$ (Å) | $Z_v$ | $n$ (m⁻³) |
|---|---|---|---|---|
| Na | bcc | 4.225 | 1 | $2.65\times10^{28}$ |
| K | bcc | 5.225 | 1 | $1.40\times10^{28}$ |
| Li | bcc | 3.51 | 1 | $4.63\times10^{28}$ |
| Cu | fcc | 3.61 | 1 | $8.50\times10^{28}$ |
| Ag | fcc | 4.09 | 1 | $5.85\times10^{28}$ |
| Al | fcc | 4.05 | 3 | $1.81\times10^{29}$ |

Con la densidad (diap. 10) sale lo mismo: Na $2.54\times10^{22}$ cm⁻³ (real, a 300 K con $\rho=0.971$) vs. $2.65\times10^{22}$ de la celda a baja $T$.

---

## P.gas1d.1.2 — $N=6$ e⁻ en $L=1$ nm (numérico)

**Enunciado.** Seis e⁻ en una caja 1D de $L=1$ nm. Halla $\varepsilon_1$, $\varepsilon_F$ y la energía mínima de excitación.

**Solución.**

1. $\varepsilon_1=\dfrac{\pi^2\hbar^2}{2mL^2}=\dfrac{\pi^2(1.0546\times10^{-34})^2}{2(9.109\times10^{-31})(10^{-9})^2}=6.025\times10^{-20}$ J $=0.376$ eV.
2. Pauli: 2 e⁻ por nivel ⇒ $2n_F=6\Rightarrow n_F=3$ (ocupados $n=1,2,3$).
3. $\varepsilon_F=\varepsilon_3=9\varepsilon_1=3.38$ eV.
4. Excitación mínima: un e⁻ de $n=3$ pasa a $n=4$ (el primer nivel vacío): $\Delta\varepsilon=\varepsilon_4-\varepsilon_3=(16-9)\varepsilon_1=7\varepsilon_1=2.63$ eV.
5. Energía total del estado fundamental: $E=2(1+4+9)\varepsilon_1=28\varepsilon_1=10.5$ eV.

**Resultado.** $\varepsilon_1=0.376$ eV, $\varepsilon_F=3.38$ eV, $\Delta\varepsilon_{min}=2.63$ eV, $E_0=10.5$ eV.

---

## P.gas1d.1.3 — Cadena de $N=10$ e⁻ y degeneración (numérico + conceptual)

**Enunciado.** Diez e⁻ en $L=2$ nm. (a) $\varepsilon_F$. (b) Excitación mínima y comparación con $k_BT$ a 300 K. (c) ¿Qué cambia si $N=5$?

**Solución.**

1. $\varepsilon_1=\pi^2\hbar^2/2mL^2=0.0940$ eV (el de 1 nm dividido entre 4).
2. (a) $n_F=N/2=5$ ⇒ $\varepsilon_F=25\varepsilon_1=2.35$ eV, $T_F=\varepsilon_F/k_B=2.35/8.617\times10^{-5}=2.7\times10^4$ K.
3. (b) $5\to6$: $\Delta\varepsilon=(36-25)\varepsilon_1=11\varepsilon_1=1.03$ eV $\gg k_BT=0.0259$ eV (factor 40) ⇒ a 300 K el gas está **degenerado**: los e⁻ no pueden absorber $k_BT$ salvo los de $n\approx n_F$ (Pauli), igual que en 3D.
4. (c) $N=5$ (impar): ocupados $n=1,2$ completos y **un** e⁻ en $n=3$ (espín arriba o abajo: nivel degenerado de espín). $2n_F=N$ ya no es exacta; $n_F=3$, $\varepsilon_F=9\varepsilon_1$ y el estado fundamental tiene degeneración 2.

**Resultado.** $\varepsilon_F=2.35$ eV, excitación 1.03 eV ($\sim40\,k_BT$); con $N$ impar la condición es $n_F=(N+1)/2$.

---

## P.interac.1.1 — ¿Es realmente débil la interacción e⁻-e⁻? (numérico + conceptual)

**Enunciado.** Estima la energía de Coulomb entre dos e⁻ separados $r_s$ en Na y compárala con $E_F$. ¿Cómo se justifica entonces el modelo (diap. 20-22)?

**Solución.**

1. $r_s=(3/4\pi n)^{1/3}=2.08$ Å, con $n=2/a^3$ del Na (P.metal.1.4).
2. $\dfrac{e^2}{4\pi\varepsilon_0r_s}=\dfrac{1.440\ \text{eV·nm}}{0.208\ \text{nm}}=6.9$ eV.
3. $E_F(\text{Na})=3.24$ eV ⇒ el Coulomb **desnudo** es $\approx2\times E_F$: **no** es pequeño.
4. Por eso la diapositiva no dice "los e⁻ están lejos"; dice que la interacción **efectiva** es débil por: (i) **Pauli** (hueco de Fermi, $r\sim1$ Å: dos e⁻ del mismo espín no se acercan), (ii) **energía mínima** (se separan) y (iii) el **apantallamiento**: cada e⁻ viaja con su hueco positivo (diap. 22), neutro a distancia ⇒ interacción entre "e⁻ + hueco" ≪.
5. Con los iones: $U_{neto}$ = **seudopotencial** apantallado, débil en alcalinos (diap. 20).

**Resultado.** Coulomb desnudo ≈ 6.9 eV > $E_F$; se resuelve por apantallamiento y Pauli. Pavlov (§7.1, p. 236) lo llama las dos aproximaciones (e⁻ libres, e⁻ independientes) y señala que su origen es la dificultad principal de Drude-Sommerfeld.

---

## P.interac.1.2 — Gas de e⁻ vs. aire (numérico + conceptual)

**Enunciado.** Compara el gas de e⁻ del Cu con aire a 300 K: densidad, estadística, energía a $T=0$.

**Solución.**

1. Densidad: $n_e=8.45\times10^{28}$ m⁻³; aire $\approx2.5\times10^{25}$ m⁻³ ⇒ razón $\approx3\times10^3$ (la diap. 23 usa $10^{29}$ vs. $10^{25}$ ⇒ $10^4$).
2. Estadística: aire = Maxwell-Boltzmann ($k_BT=0.026$ eV $\gg$ cualquier $T_F$ de moléculas); e⁻ = Fermi-Dirac con $E_F=7.0$ eV $\gg k_BT$ ($T_F=8\times10^4$ K): **degenerado**.
3. Energía por partícula a $T=0$: aire → 0 (todas en reposo); e⁻ → $\tfrac35E_F=4.2$ eV $\neq0$ (Pauli obliga a llenar niveles).
4. Carga: moléculas neutras vs. e⁻ con $q=-e$ ⇒ **plasma denso** (neutralizado por los iones).
5. Analogías: ambos llenan todo el volumen y se tratan como libres (sin interacción fuerte).

**Resultado.** Misma imagen ("gas libre"), pero degenerado, 3-4 órdenes más denso, cargado y con $E(0)\neq0$ (`P-2025-01 #4c`, `P-2025-2S #4a`).

---

## Checklist de práctica (P01)

- [ ] P.metal.1.1 Concentración $N=Z_vN_A\rho/M$ de Cu, Al, Mg, Na
- [ ] P.metal.1.2 Fracción de volumen de los iones en Na (y la inconsistencia de la diap. 7)
- [ ] P.metal.1.4 $n=N/V$ desde la estructura (bcc/fcc) y $a$ de Na, K, Li, Cu, Ag, Al
- [ ] P.gas1d.1.2 $N=6$ e⁻ en 1 nm: $\varepsilon_F$ y excitación mínima
- [ ] P.gas1d.1.3 $N=10$ e⁻ en 2 nm, degeneración y caso $N$ impar
- [ ] P.interac.1.1 Coulomb desnudo vs. $E_F$ y por qué el modelo funciona
- [ ] P.interac.1.2 Gas de e⁻ vs. aire con números
