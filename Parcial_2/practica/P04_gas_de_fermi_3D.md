# P04 · Práctica resuelta: gas de Fermi 3D (`fermi3d.1`, `fermi3d.2`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T04_gas_de_fermi_3D.md`. Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $k_B=1.381\times10^{-23}$ J/K, 1 eV $=1.602\times10^{-19}$ J. Cada cifra se recalculó con Python. (Con estas constantes el $E_F$ del Cu sale 7.02 eV; los exámenes redondean a 7.05 eV.)

---

## P.fermi3d.1.2 — $E_F$, $T_F$ y $v_F$ desde la estructura cristalina (numérico)

**Enunciado.** Na (bcc, $a=4.225$ Å, $Z_v=1$), Cu (fcc, $a=3.61$ Å, $Z_v=1$) y Al (fcc, $a=4.05$ Å, $Z_v=3$), todos con $m^*=m_e$. Calcula $n$, $k_F$, $E_F$, $T_F$ y $v_F$. Compara el Na con la diap. 67.

**Solución.** $\hbar^2/2m=3.81$ eV·Å². Pasos para cada metal: (1) $n=Z_v\times(\text{átomos/celda})/a^3$; (2) $k_F=(3\pi^2n)^{1/3}$; (3) $E_F=\hbar^2k_F^2/2m$; (4) $T_F=E_F/k_B$; (5) $v_F=\hbar k_F/m$.

1. **Na:** $n=2/a^3=2.65\times10^{28}$ m⁻³; $k_F=(3\pi^2\times2.65\times10^{28})^{1/3}=9.23\times10^{9}$ m⁻¹ $=0.923$ Å⁻¹; $E_F=3.81\times0.923^2=3.24$ eV; $T_F=3.24/8.617\times10^{-5}=3.76\times10^4$ K; $v_F=1.07\times10^6$ m/s.
2. **Cu:** $n=4/a^3=8.50\times10^{28}$ m⁻³; $k_F=1.36$ Å⁻¹; $E_F=7.05$ eV; $T_F=8.18\times10^4$ K; $v_F=1.57\times10^6$ m/s.
3. **Al:** $n=12/a^3=1.81\times10^{29}$ m⁻³; $k_F=1.75$ Å⁻¹; $E_F=11.7$ eV; $T_F=1.35\times10^5$ K; $v_F=2.03\times10^6$ m/s.
4. Diap. 67 (Na): usa $N/V=3\times10^{22}$ cm⁻³ (redondeado) ⇒ $k_F\approx1$ Å⁻¹, $E_F\approx3.5$ eV, $T_F\approx40\,000$ K. Con el $n$ exacto de la celda ($2.65\times10^{22}$) sale 3.24 eV.

**Resultado.**

| Metal | $n$ (m⁻³) | $k_F$ (Å⁻¹) | $E_F$ (eV) | $T_F$ (K) | $v_F$ (m/s) |
|---|---|---|---|---|---|
| Na | $2.65\times10^{28}$ | 0.923 | 3.24 | $3.8\times10^4$ | $1.07\times10^6$ |
| Cu | $8.50\times10^{28}$ | 1.36 | 7.05 | $8.2\times10^4$ | $1.57\times10^6$ |
| Al | $1.81\times10^{29}$ | 1.75 | 11.7 | $1.35\times10^5$ | $2.03\times10^6$ |

Comprobación: $E_F\propto n^{2/3}$ ⇒ Al/Na: $(6.8)^{2/3}=3.6$ ✔.

---

## P.fermi3d.1.5 — Plata, potasio y litio desde la celda (numérico)

**Enunciado.** Ag (fcc, $a=4.09$ Å), K (bcc, 5.225 Å) y Li (bcc, 3.51 Å), 1 e⁻/átomo. Halla $E_F$, $T_F$, $v_F$ y $E_F/k_BT$ a 300 K.

**Solución.**

1. **Ag:** $n=4/a^3=5.85\times10^{28}$ m⁻³ ⇒ $k_F=1.20$ Å⁻¹ ⇒ $E_F=3.81\times1.20^2=5.49$ eV; $T_F=6.37\times10^4$ K; $v_F=1.39\times10^6$ m/s; $E_F/k_BT=5.49/0.02586=212$.
2. **K:** $n=2/a^3=1.40\times10^{28}$ m⁻³ ⇒ $k_F=0.746$ Å⁻¹ ⇒ $E_F=2.12$ eV; $T_F=2.46\times10^4$ K; $v_F=8.64\times10^5$ m/s; $E_F/k_BT=82$.
3. **Li:** $n=2/a^3=4.63\times10^{28}$ m⁻³ ⇒ $k_F=1.11$ Å⁻¹ ⇒ $E_F=4.70$ eV; $T_F=5.45\times10^4$ K; $v_F=1.29\times10^6$ m/s; $E_F/k_BT=182$.

**Resultado.** Ag: 5.49 eV, $6.4\times10^4$ K; K: 2.12 eV, $2.5\times10^4$ K; Li: 4.70 eV, $5.5\times10^4$ K. En los tres $E_F\gg k_BT$: gas degenerado a 300 K (coincide con `P-2025-01 #1, #2`).

---

## P.fermi3d.2.4 — $D(E_F)$ del cobre desde la celda (numérico)

**Enunciado.** Cu (fcc, $a=3.61$ Å). Halla $D(E_F)/V=3n/2E_F$ y cuántos estados caben en una franja $k_BT$ a 300 K.

**Solución.**

1. $n=4/a^3=8.50\times10^{28}$ m⁻³ y $E_F=7.05$ eV.
2. $D(E_F)/V=\dfrac{3n}{2E_F}=\dfrac{3\times8.50\times10^{28}}{2\times7.05}=1.81\times10^{28}$ eV⁻¹m⁻³.
3. Franja térmica: $D(E_F)k_BT/V=1.81\times10^{28}\times0.02586=4.7\times10^{26}$ m⁻³.
4. Fracción: $4.7\times10^{26}/8.50\times10^{28}=5.5\times10^{-3}\approx\tfrac32\,k_BT/E_F$.

**Resultado.** $D(E_F)/V=1.8\times10^{28}$ eV⁻¹m⁻³; solo ~0.5 % de los e⁻ están en la franja $k_BT$ de $E_F$ (diap. 57-58).

---

## Checklist de práctica (P04)

- [ ] P.fermi3d.1.2 $k_F$, $E_F$, $T_F$, $v_F$ de Na, Cu y Al
- [ ] P.fermi3d.1.5 Ag, K y Li desde la celda: $E_F$, $T_F$, $v_F$
- [ ] P.fermi3d.2.4 $D(E_F)$ del Cu desde la celda y e⁻ en la franja $k_BT$
