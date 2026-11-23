# P05 · Práctica resuelta: escalas astrofísicas y definición de $E_F$ (`extra.3`, `vib.6`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T05_astrofisica_y_definicion_EF.md`. Estos temas **no vienen de las diapositivas** (salen de exámenes). Constantes: $\hbar=1.0546\times10^{-34}$ J·s, $m=9.109\times10^{-31}$ kg, $c=2.998\times10^8$ m/s, $m_p=1.6726\times10^{-27}$ kg, $mc^2=0.511$ MeV. Datos estelares aproximados (no del PDF).

---

## P.extra.3.1 — Una enana blanca tipo Sirio B: ¿relativista o no? (numérico)

**Enunciado.** Estrella de $M=2.03\times10^{30}$ kg y $R=5.8\times10^6$ m, compuesta de núcleos con 2 nucleones por e⁻ ($N=M/2m_p$). Calcula $n$ y $E_F$ (a) no relativista, (b) ultrarrelativista y (c) con la relación relativista exacta. ¿Cuál vale?

**Solución.**

1. $N=\dfrac M{2m_p}=\dfrac{2.03\times10^{30}}{2\times1.6726\times10^{-27}}=6.07\times10^{56}$ e⁻.
2. $V=\tfrac43\pi R^3=8.17\times10^{20}$ m³ ⇒ $n=7.43\times10^{35}$ m⁻³.
3. $k_F=(3\pi^2n)^{1/3}=(2.20\times10^{37})^{1/3}=2.80\times10^{12}$ m⁻¹.
4. (a) No relativista: $E_F=\dfrac{\hbar^2k_F^2}{2m}=299$ keV.
5. (b) Ultrarrelativista: $E_F=\hbar ck_F=p_Fc=553$ keV.
6. Criterio: $p_Fc=553$ keV $\sim mc^2=511$ keV ⇒ **régimen intermedio**; ninguna de las dos aproximaciones vale.
7. (c) Exacta: $E_F^{cin}=\sqrt{(p_Fc)^2+(mc^2)^2}-mc^2=\sqrt{553^2+511^2}-511=753-511=242$ keV. Velocidad: $v_F/c=p_Fc/E=553/753=0.73$.

**Resultado.** $E_F=242$ keV (exacta); el límite no relativista sobreestima (299 keV, +24 %) y el ultrarrelativista también (553 keV, +130 %). Como $E_F/mc^2\approx0.5$ hay que usar la relación relativista. $T_F=E_F/k_B\approx2.8\times10^9$ K ≫ la temperatura de la estrella: el gas está **totalmente degenerado**.

---

## P.extra.3.2 — Pulsar y el límite ultrarrelativista (numérico + deducción)

**Enunciado.** (a) Deduce $E_F\approx\hbar c(3\pi^2n)^{1/3}$ para e⁻ ultrarrelativistas. (b) Aplícalo a un pulsar ($N=1.2\times10^{57}$, $R=10$ km) y comprueba que el límite no relativista falla.

**Solución.**

1. (a) El conteo de estados es el mismo ($k_F=(3\pi^2n)^{1/3}$, no depende de $E(k)$). Para $E\gg mc^2$: $E=pc=\hbar kc$ ⇒ $E_F=\hbar ck_F=\hbar c(3\pi^2n)^{1/3}$.
2. (b) $V=\tfrac43\pi(10^4)^3=4.19\times10^{12}$ m³ ⇒ $n=2.86\times10^{44}$ m⁻³ ⇒ $k_F=(3\pi^2n)^{1/3}=2.04\times10^{15}$ m⁻¹.
3. $E_F=\hbar ck_F=1.0546\times10^{-34}\times2.998\times10^8\times2.04\times10^{15}=6.4\times10^{-11}$ J $=4.0\times10^8$ eV.
4. Comprobación: $E_F/mc^2=4.0\times10^8/5.11\times10^5=790\gg1$ ⇒ ultrarrelativista ✔.
5. Con la fórmula no relativista saldría $1.6\times10^{11}$ eV (absurdo: $\gg mc^2$ ⇒ velocidad $\gg c$).

**Resultado.** $E_F\approx4\times10^8$ eV $\sim10^8$ eV (`T-2025-II #3c`), $E_F\propto n^{1/3}$ en vez de $n^{2/3}$.

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

- [ ] P.extra.3.1 Enana blanca: $E_F$ no relativista, ultrarrelativista y exacta
- [ ] P.extra.3.2 Pulsar y límite ultrarrelativista
- [ ] P.vib.6.1 Distinguir $E_F$, $\tfrac35E_F$, $\mu$ y $\phi$ (y `P-2026-1S #11`)
