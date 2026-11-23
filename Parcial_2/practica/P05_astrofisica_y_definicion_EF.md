# P05 · Práctica resuelta: escalas astrofísicas y definición de $E_F$ (`extra.3`, `vib.6`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T05_astrofisica_y_definicion_EF.md`. Estos temas **no vienen de las diapositivas** (salen de exámenes). Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $c=2.998\times10^8$ m/s, $m_p=1.6726\times10^{-27}$ kg, $mc^2=0.511$ MeV. Datos estelares aproximados (no del PDF).

---

## P.extra.3.1 — El Sol colapsado: $N$, $n$, $E_F$ y $T_F$ (numérico)

**Enunciado.** El Sol ($M=2\times10^{30}$ kg) colapsa a $R=7\times10^{8}$ m. Con un e⁻ por protón ($N=M/m_p$, $m_p=1.6726\times10^{-27}$ kg), halla $n$, $E_F$, $T_F$ y $v_F$ (no relativista). (Enunciado tipo `P-2025-2S #2`.)

**Solución.**

1. $N=M/m_p=1.20\times10^{57}$.
2. $V=\tfrac43\pi R^3=1.437\times10^{27}$ m³ ⇒ $n=N/V=8.32\times10^{29}$ m⁻³.
3. $k_F=(3\pi^2n)^{1/3}=2.91\times10^{10}$ m⁻¹.
4. $E_F=\hbar^2k_F^2/2m=5.17\times10^{-18}$ J $=32.3$ eV.
5. $T_F=E_F/k_B=3.74\times10^5$ K; $v_F=\hbar k_F/m=3.37\times10^6$ m/s.
6. Comprobación del régimen: $E_F/mc^2=6\times10^{-5}\ll1$ ⇒ la fórmula no relativista es válida.

**Resultado.** $n=8.3\times10^{29}$ m⁻³, $E_F=32$ eV, $T_F=3.7\times10^5$ K, $v_F=3.4\times10^6$ m/s. Si fuese $N=M/2m_p$: $n$ a la mitad ⇒ $E_F=2^{-2/3}\times32.3=20.3$ eV.

---

## P.vib.6.1 — Cuatro "$E_F$" que no son $E_F$ (conceptual + numérico)

**Enunciado.** Para el Cu a 300 K ($E_F=7.02$ eV), asigna un valor a: la energía del estado ocupado más alto a $T=0$, la energía media, $\mu(300)$ y la función trabajo ($\phi\approx4.7$ eV, dato externo). Resuelve `P-2026-1S #11`.

**Solución.**

1. $E_F$ (def.): energía del estado cuántico **ocupado más alto** en el estado fundamental ($T=0$): 7.02 eV.
2. Energía media: $\tfrac35E_F=4.21$ eV (opción a: *no*).
3. $\mu(300\text{ K})=E_F-7.8\times10^{-5}$ eV $\approx7.02$ eV: es el nivel con $f=\tfrac12$ (opción d); a $T=0$ coincide con $E_F$, a $T>0$ **no** es la definición de $E_F$.
4. Función trabajo $\phi=E_{vac}-E_F\approx4.7$ eV (el Cu): energía para *sacar* un e⁻ (opción e), medida desde $E_F$ al vacío.
5. Estado ocupado más bajo: $E=0$ (en $k=0$), opción c.

**Resultado.** Respuesta **b**. Los cuatro números son distintos (7.02, 4.21, ≈7.02 y 4.7 eV): $E_F$ es un **borde** en $T=0$, no un promedio, no una probabilidad ni una barrera de superficie.

---

## Checklist de práctica (P05)

- [ ] P.extra.3.1 Sol colapsado: $n$, $E_F$, $T_F$ y $v_F$
- [ ] P.vib.6.1 Distinguir $E_F$, $\tfrac35E_F$, $\mu$ y $\phi$ (y `P-2026-1S #11`)
