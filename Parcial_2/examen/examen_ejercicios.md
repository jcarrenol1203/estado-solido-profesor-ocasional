# Examen de ejercicios — Parcial 2 (sobre 5.0)

> Sin ayuda. Muestra el procedimiento (formula → sustitución → resultado con unidades). Usa las constantes de `examen/README.md`. Datos de tablas estándar incluidos en cada enunciado.

**EX.E.1 (0.5) — Magnesio.** Mg: divalente, $\rho=1.74$ g/cm³, $M=24.31$ g/mol; trátalo como gas de e⁻ libres ($m^*=m_e$). Halla (a) $n$ de e⁻ de conducción, (b) $k_F$, (c) $E_F$ en eV, (d) $T_F$, (e) $v_F$ y (f) la energía media por e⁻ a $T=0$.

**EX.E.2 (0.8) — Alambre de aluminio.** Alambre de Al de longitud 2 m y sección 0.5 mm² que lleva 3 A a 300 K. Datos: $\sigma=3.5\times10^7$ Ω⁻¹m⁻¹, $Z_v=3$, $n=1.81\times10^{29}$ m⁻³, $m^*=m_e$. Calcula (a) $R$, la caída de tensión y la potencia disipada, (b) $E$ y $J$, (c) $v_d$, (d) $\tau$, (e) $\ell=v_F\tau$ y cuántos parámetros de red ($a=4.05$ Å) representa, (f) la movilidad, (g) $v_d/v_F$.

**EX.E.3 (0.6) — Matthiessen en Al.** Una muestra de Al (mismos $n$ y $m^*$ del problema anterior) tiene $\rho(300\text{ K})=2.8\times10^{-8}$ Ω·m y $\rho(4\text{ K})=1.5\times10^{-10}$ Ω·m. Halla (a) $\rho_{imp}$ y $\rho_{ph}(300)$, (b) $\tau_{imp}$ y $\tau_{ph}(300)$ y los caminos libres correspondientes (con $v_F$), (c) la razón de resistividad residual, (d) $\rho(150\text{ K})$ **suponiendo** $T\gg\theta$ (¿es razonable esa suposición? di en qué condición lo es).

**EX.E.4 (0.8) — Potasio a baja temperatura.** K: $n=1.40\times10^{28}$ m⁻³ (1 e⁻/átomo), $m^*=m_e$, $\theta_D=91$ K. (a) $E_F$ y $T_F$. (b) $C_e$ molar a 10 K y a 300 K con la fórmula exacta, y la razón con $\tfrac32R$. (c) $\gamma$ en mJ/mol·K². (d) $C_{ph}=\tfrac{12\pi^4}{5}R(T/\theta_D)^3$ a 10 K y compárala con $C_e$. (e) $T$ a la cual $C_e=C_{ph}$.

**EX.E.5 (0.7) — Litio: presión y módulo.** Li: $n=4.7\times10^{28}$ m⁻³, $m^*=m_e$. (a) $E_F$ y $T_F$. (b) $D(E_F)$ por unidad de volumen en eV⁻¹m⁻³. (c) Energía por volumen $E_0/V$ a $T=0$ en GPa. (d) Presión $P$ y módulo $B=-V\,\partial P/\partial V$ (deduce las expresiones). (e) Si el volumen disminuye 1 %, ¿en cuánto cambia $E_F$ (en %)?

**EX.E.6 (0.7) — Gas de e⁻ bidimensional (deducción).** Un gas de $N$ e⁻ libres está confinado en un cuadrado de área $A=L^2$ con condiciones periódicas (densidad superficial $n_s=N/A$). (a) Deduce $k_F$ y $E_F$ en función de $n_s$ y $m^*$ (cuenta estados en el plano $\mathbf k$, con espín). (b) Deduce $D(\varepsilon)=dN/d\varepsilon$ y muestra que es **constante**. (c) Calcula $E_F$, $T_F$ y $v_F$ para $n_s=10^{16}$ m⁻² y $m^*=0.067\,m_e$ (GaAs). (d) Escribe cómo cambiaría $C_e$ frente al caso 3D (solo cualitativo: $C_e\propto D(E_F)T$).

**EX.E.7 (0.5) — Cadena de 8 e⁻.** Ocho e⁻ en una caja 1D de $L=1.5$ nm. (a) $\varepsilon_1$. (b) $n_F$ y $\varepsilon_F$. (c) Energía total del estado fundamental. (d) Energía y **longitud de onda** del fotón que promueve el e⁻ de más energía al primer nivel libre. (e) Comparación con $k_BT$ a 300 K.

**EX.E.8 (0.4) — Una enana blanca.** $M=1.2\times10^{30}$ kg, $R=9\times10^{6}$ m, 2 nucleones por e⁻ ($N=M/2m_p$). (a) $N$ y $n$. (b) $E_F$ no relativista y $T_F$. (c) ¿Es válido el tratamiento no relativista? Justifica con la razón $E_F/m_ec^2$ y, si hace falta, da la corrección.

---

## Checklist del examen de ejercicios

- [ ] EX.E.1 Magnesio: $n$, $k_F$, $E_F$, $T_F$, $v_F$ (`metal.1`, `fermi3d.1`) — 0.5
- [ ] EX.E.2 Alambre de Al (`drude.1`, `drude.2`) — 0.8
- [ ] EX.E.3 Matthiessen en Al (`drude.3`) — 0.6
- [ ] EX.E.4 Potasio a baja $T$ (`cal.2`) — 0.8
- [ ] EX.E.5 Litio: $D(E_F)$, $P$, $B$ (`fermi3d.2`) — 0.7
- [ ] EX.E.6 Gas de e⁻ 2D (`fermi3d.1`, `fermi3d.2`) — 0.7
- [ ] EX.E.7 Cadena de 8 e⁻ (`gas1d.1`) — 0.5
- [ ] EX.E.8 Enana blanca (`extra.3`) — 0.4
