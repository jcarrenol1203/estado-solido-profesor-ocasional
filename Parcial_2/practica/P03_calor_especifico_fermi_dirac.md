# P03 · Práctica resuelta: calor específico y Fermi-Dirac (`cal.1`, `cal.2`)

> Ejercicios **resueltos por Claude paso a paso**, ligados a `teoria/T03_calor_especifico_fermi_dirac.md`. $R=8.314$ J/mol·K, $k_B=8.617\times10^{-5}$ eV/K, $k_BT(300\text{ K})=0.02586$ eV. $E_F$ del Cu $=7.02$ eV ($n=8.45\times10^{28}$ m⁻³, $m^*=m_0$), del Na $=3.24$ eV ($n=2.65\times10^{28}$ m⁻³, $m^*=m_0$): se deducen en `P04`. Cada cifra se recalculó con Python.

---

## P.cal.1.1 — El fracaso clásico en números (numérico)

**Enunciado.** Calcula en J/mol·K y cal/mol·K el $C_e$ clásico, el $C_{total}$ clásico a $T$ alta y compáralos con $C_{total}\approx3R$.

**Solución.**

1. Equipartición: $\langle E\rangle=\tfrac32k_BT$ por e⁻ ⇒ $E_{mol}=\tfrac32N_Ak_BT=\tfrac32RT$ ⇒ $C_e=\tfrac32R=12.47$ J/mol·K $=2.98$ cal/mol·K.
2. Red (Dulong-Petit): $C_{red}=3R=24.94$ J/mol·K $=5.96$ cal/mol·K.
3. Clásico total: $3R+\tfrac32R=4.5R=37.4$ J/mol·K $=8.94$ cal/mol·K.
4. Experimento (diap. 53): $C_{total}\approx3R\approx6$ cal/mol·K (igual que un aislante).
5. Exceso clásico: $4.5R/3R=1.5$, es decir **50 % más** (Pavlov, p. 200: "1.5 veces mayor que la ley de Dulong y Petit").

**Resultado.** $C_e^{cl}=12.5$ J/mol·K, $C^{cl}_{tot}=37.4$ vs. experimental $\approx24.9$ J/mol·K. Falla la estadística MB; la contribución real es $\sim10^{-2}\times12.5$.

---

## P.cal.2.1 — Tabla de $f(E)$ y el límite de Maxwell-Boltzmann (numérico)

**Enunciado.** Calcula $f$ para $x=(E-\mu)/k_BT=-3,-1,0,1,3,5$ y compara con $e^{-x}$. Luego, para Cu a 300 K, halla $f$ a $E_F\pm0.1$ eV (con $\mu\approx E_F$).

**Solución.** $f=1/(e^x+1)$.

| $x$ | $f_{FD}$ | $e^{-x}$ (MB) |
|---|---|---|
| −3 | 0.9526 | — |
| −1 | 0.7311 | — |
| 0 | **0.5000** | 1 |
| 1 | 0.2689 | 0.3679 |
| 3 | 0.0474 | 0.0498 |
| 5 | 0.00669 | 0.00674 |

1. Simetría: $f(-x)=1-f(x)$ (0.9526 = 1 − 0.0474).
2. A $x=5$ el error de MB es 0.7 %; a $x=1$ es 37 % ⇒ la cola ($E-\mu\gtrsim5k_BT$) es MB (diap. 61; Pavlov 6.47).
3. Cu, 300 K: $x=\pm0.1/0.02586=\pm3.87$ ⇒ $f(E_F+0.1)=1/(e^{3.87}+1)=0.0205$ y $f(E_F-0.1)=0.9795$.

**Resultado.** $f(\mu)=\tfrac12$ y $f$ es antisimétrica alrededor de $\mu$; a 0.1 eV de $E_F$ ya solo 2 % de ocupación (arriba) / 2 % de huecos (abajo) a 300 K: la zona difusa mide unos $\pm0.1$ eV de un total de $E_F=7$ eV.

---

## P.cal.2.2 — $T_F$ y $C_e$ de Cu y Na a 300 K (numérico)

**Enunciado.** Halla $T_F$, $T/T_F$, $C_e$ (exacto $\tfrac{\pi^2}{2}RT/T_F$ y la estimación $2RT/T_F$ de la diap. 58) y $C_e/(\tfrac32R)$ para Cu y Na a 300 K.

**Solución.**

1. Cu: $T_F=E_F/k_B=7.02/8.617\times10^{-5}=8.15\times10^4$ K ⇒ $T/T_F=3.68\times10^{-3}$.
   - Exacto: $C_e=4.935\times8.314\times3.68\times10^{-3}=0.151$ J/mol·K.
   - Estimación $2RT/T_F=0.061$ J/mol·K (factor 2.5 menor: es solo un orden de magnitud).
   - $C_e/(\tfrac32R)=0.151/12.47=1.21\times10^{-2}$ ($=\tfrac{\pi^2}{3}T/T_F$ de Pavlov 6.65 ✔).
2. Na ($m^*=m_0$): $T_F=3.24/8.617\times10^{-5}=3.76\times10^4$ K ⇒ $T/T_F=7.98\times10^{-3}$.
   - $C_e=4.935\times8.314\times7.98\times10^{-3}=0.327$ J/mol·K; $C_e/(\tfrac32R)=2.6\times10^{-2}$.
3. Fracción de e⁻ "afectados" $\sim T/T_F$: Cu 0.37 %, Na 0.80 %.
4. $C_e/C_{red}$ (Cu) $=0.151/24.94=0.6\,\%$ a 300 K.

**Resultado.** Cu: $T_F=8.2\times10^4$ K, $C_e=0.15$ J/mol·K (1.2 % del clásico); Na: $T_F=3.8\times10^4$ K, $C_e=0.33$ J/mol·K (2.6 %). Coincide con `P-2025-2S #3` (0.0037 y 0.008, $T/T_F$).

---

## P.cal.2.4 — Separar $\gamma$ y $\beta$ de datos de $C(T)$ (numérico)

**Enunciado.** Datos (ejemplo): $C=0.75,\ 1.80,\ 3.45,\ 6.00$ mJ/mol·K a $T=1,2,3,4$ K. Usa $C/T=\gamma+\beta T^2$ y halla $\gamma$, $\beta$ y la $T$ donde $\gamma T=\beta T^3$.

**Solución.**

1. $C/T=0.750,\ 0.900,\ 1.150,\ 1.500$ para $T^2=1,4,9,16$ K².
2. Pendiente entre (1, 0.750) y (4, 0.900): $\beta=(0.900-0.750)/(4-1)=0.050$ mJ/mol·K⁴. Chequeo con (9, 1.150) y (16, 1.500): $(1.500-1.150)/7=0.050$ ✔ (recta).
3. Ordenada: $\gamma=0.750-0.050\times1=0.700$ mJ/mol·K².
4. Cruce: $\gamma T=\beta T^3\Rightarrow T=\sqrt{\gamma/\beta}=\sqrt{14}=3.74$ K. Por debajo domina el término electrónico (diap. 59; Pavlov $T_c\approx\Theta_D/10$, 6.67).

**Resultado.** $\gamma=0.70$ mJ/mol·K², $\beta=0.050$ mJ/mol·K⁴, $T_{cruce}=3.7$ K. En la gráfica $C/T$ vs. $T^2$ (diap. 59) $\gamma$ es la ordenada al origen y $\beta$ la pendiente.

---

## P.cal.2.7 — Ancho de la zona difusa (numérico, variante)

**Enunciado.** ¿Cuánto vale $\Delta E$ entre $f=99\,\%$ y $f=1\,\%$ a 300 K? (La versión 90 %-10 % de `T-2025-II #1` está resuelta en `examenes_resueltos/`.)

**Solución.**

1. $f=0.99\Rightarrow e^{x}=1/0.99-1=0.0101\Rightarrow x=-\ln99=-4.595$; $f=0.01\Rightarrow x=+4.595$.
2. $\Delta E=2\ln99\ k_BT=9.19\,k_BT=9.19\times0.02586=0.238$ eV.

**Resultado.** $\Delta E_{99\to1}=9.19\,k_BT=0.238$ eV a 300 K ($\ll E_F=7$ eV): la "cola" afecta una franja estrecha.

---

## P.cal.2.8 — Potasio y litio desde la celda: $E_F$, $T_F$, $C_e$, $\gamma$ (numérico)

**Enunciado.** K (bcc, $a=5.225$ Å) y Li (bcc, $a=3.51$ Å), 1 e⁻/átomo, $m^*=m_e$. Halla $n$, $E_F$, $T_F$, $C_e$ a 300 K ($C_e=\tfrac{\pi^2}{2}R\,T/T_F$), $C_e/(\tfrac32R)$ y $\gamma=C_e/T$.

**Solución.** $n=2/a^3$ (bcc), $E_F=\dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$, $T_F=E_F/k_B$.

1. K: $n=1.40\times10^{28}$ m⁻³ ⇒ $E_F=2.12$ eV ⇒ $T_F=2.46\times10^4$ K ⇒ $T/T_F=0.0122$.
   - $C_e=4.935\times8.314\times0.0122=0.500$ J/mol·K; $C_e/(\tfrac32R)=0.500/12.47=0.040$.
   - $\gamma=\pi^2R/(2T_F)=4.935\times8.314/2.46\times10^4=1.67\times10^{-3}$ J/mol·K² $=1.67$ mJ/mol·K².
2. Li: $n=4.63\times10^{28}$ m⁻³ ⇒ $E_F=4.70$ eV ⇒ $T_F=5.45\times10^4$ K ⇒ $T/T_F=0.0055$.
   - $C_e=4.935\times8.314\times0.0055=0.226$ J/mol·K; $C_e/(\tfrac32R)=0.018$; $\gamma=0.75$ mJ/mol·K².

**Resultado.**

| Metal | $n$ (m⁻³) | $E_F$ (eV) | $T_F$ (K) | $C_e$(300 K) (J/mol·K) | $C_e/\tfrac32R$ | $\gamma$ (mJ/mol·K²) |
|---|---|---|---|---|---|---|
| K | $1.40\times10^{28}$ | 2.12 | $2.46\times10^4$ | 0.50 | 4.0 % | 1.67 |
| Li | $4.63\times10^{28}$ | 4.70 | $5.45\times10^4$ | 0.23 | 1.8 % | 0.75 |

Menor $n$ ⇒ menor $E_F$ ⇒ menor $T_F$ ⇒ mayor $C_e$ (efecto $\propto1/T_F$).

---

## Checklist de práctica (P03)

- [ ] P.cal.1.1 $C_e$ y $C_{total}$ clásicos vs. experimento
- [ ] P.cal.2.1 Tabla de $f(E)$ y límite de MB; $f$ a $E_F\pm0.1$ eV
- [ ] P.cal.2.2 $T_F$, $T/T_F$ y $C_e$ de Cu y Na a 300 K
- [ ] P.cal.2.4 Separar $\gamma$ y $\beta$ de datos de $C/T$ vs. $T^2$
- [ ] P.cal.2.7 Ancho 99 %→1 % de $f(E)$
- [ ] P.cal.2.8 K y Li desde la celda bcc: $E_F$, $T_F$, $C_e$ y $\gamma$
