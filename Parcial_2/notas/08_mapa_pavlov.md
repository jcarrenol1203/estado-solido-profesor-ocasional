# Mapa diapositivas 1-70 ↔ Pavlov y Khokhlov, *Física del estado sólido* (Mir, 1987)

> **Origen:** extraído una sola vez de `Diapositivas/pdf-fisica-del-estado-solido-p-v-pavplovpdf_compress.pdf` (181 págs). Ese PDF es una **copia abreviada y con OCR ruidoso**: faltan tramos del libro (p. ej. no está el §2.6 "Metales", p. 92, ni las pp. 194-199 ni 208-). Por eso se citan **página del libro** (la numeración impresa) y, entre paréntesis, la página del PDF (`pdf N`). **Verificado visualmente** (render a 130-200 dpi y lectura de la imagen, no del OCR) en pdf 88-95, 114-115 y 145-146, es decir, libro pp. 200-207, 235-236 y 286-287.
> **No releer el libro:** usar esta nota. Excepción: leer pocas páginas puntuales avisando antes.

El libro **no sigue el orden de las diapositivas**: no tiene un capítulo propio de "metales y electrón libre". El modelo de Drude-Sommerfeld aparece repartido en el cap. 6 (térmicas) y en el cap. 7 (eléctricas).

## Tabla por subtema (solo los que están en alcance, diapositivas 1-70)

| Subtema | Diapositivas | Pavlov (pág. libro / pdf) | Qué hay |
|---|---|---|---|
| metal.1 | 1-13 | §6.1, p. 200 (pdf 88) | Metal = iones que vibran + gas de e⁻ de valencia colectivizados. El §2.6 "Metales" (p. 92) **no está en la copia**. |
| gas1d.1 | 13-18 | — | No tratado (el libro pasa directo a 3D). |
| interac.1 | 19-23 | §7.1 "Clasificación de los sólidos por su conductibilidad", pp. 235-236 (pdf 114-115) | Rangos de $\sigma$ (metales $\sim10^4$-$10^6$ Ω⁻¹cm⁻¹, dieléctricos $<10^{-10}$); $\sigma(T)$ metales (7.2) vs. $\sigma_0e^{-\Delta E/k_BT}$ (7.1); modelos de Drude-Lorentz y Sommerfeld; aproximaciones de e⁻ **libres** (sin iones) e **independientes** (sin e⁻-e⁻) y por qué fallan. |
| drude.1, drude.2 | 24-37 | §7.1, pp. 235-236 (pdf 115) | Solo mención del modelo; la deducción $\sigma=Ne^2\tau/m^*$ **no está** en la copia. Usar las notas `01`. |
| drude.3 | 38-50 | §7.13, pp. 286-287 (pdf 145-146) | $\sigma=en\mu$ con $n$ casi constante (gas degenerado) ⇒ $\sigma(T)$ la fija $\mu(T)$; a $T$ alta dispersión por fonones, $\mu\propto1/T$ (7.164, en páginas que faltan) ⇒ $\rho\propto T$; a $T$ baja dominan las impurezas, $\mu$ independiente de $T$ ⇒ $\rho_{res}$ constante (fig. 7.24). **El libro no da la ley $\rho_{ph}\propto T^5$ de las diapositivas.** |
| cal.1 | 51-53 | §6.1, p. 200 (pdf 88) | Con Maxwell-Boltzmann el gas de e⁻ añadiría $\tfrac32 k_B$ por e⁻ (1.5× Dulong-Petit); el experimento no lo ve; a $T\to0$ los e⁻ dominan. |
| cal.2 | 53-61 | §6.1, pp. 201-206 (pdf 89-94) | Pauli; nivel de Fermi; $f(E)$ de Fermi-Dirac (p. 202); límite MB cuando $k_BT\gg E_F$; $T_F=E_F/k_B\approx5\times10^4$ K (gas degenerado hasta la fusión); solo e⁻ en $\sim k_BT$ de $E_F$ cuentan; $E_F(T)\approx E_F(0)[1-\tfrac{\pi^2}{12}(k_BT/E_F)^2]$ (6.57); $C_e\propto T$ (6.64) y $C_e/C_{clás}=\tfrac{\pi^2}{3}k_BT/E_F\sim10^{-2}$ a 300 K (6.65); $c_V=\gamma_eT+\gamma_DT^3$ (6.66) y $T_c\approx\Theta_D/10$ por debajo del cual dominan los e⁻ (6.67, p. 207). |
| fermi3d.1 | 62-67 | §6.1, pp. 202-204 (pdf 90-92) | $E=p^2/2m$; $N=\int 2D\,f\,dE$ (6.55); $E_F(0)=\tfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ (6.56). |
| fermi3d.2 | 68-70 | §6.1, pp. 203-206 (pdf 91-94) | Celdas de fase $(2\pi\hbar)^3/V$ en el espacio de impulsos (6.48-6.49); $N(E)=\tfrac{1}{(2\pi)^2}(2m/\hbar^2)^{3/2}E^{1/2}$ (6.53, fig. 6.10); energía: $U_e(T)=\tfrac25N(E_F)E_F^2\cdot E_F\!+\!\tfrac{\pi^2}{4}(k_BT)^2N(E_F)$ (6.62) y $U_e(T)=U_e^0+\tfrac{\pi^2}{6}(k_BT)^2N[E_F(0)]$ (6.63). |

Fuera de alcance pero en el libro: conductividad térmica y Wiedemann-Franz en §6.3 (pp. 211-216, pdf 99-104); Hall en §7.15 (pp. 292-293, pdf 151-152); bandas (Bloch, Kronig-Penney, zonas, masa efectiva) en §7.3-7.8 (pdf 118-129) → es el material de `extra.1`.

## Cuidado con el libro (verificado)

- **Ejemplo numérico de la p. 204 (pdf 92), leído en imagen a 200 dpi:** el libro dice $n=10^{29}$ m⁻³ y $E_F(0)\approx8\times10^{-19}$ J $=5$ eV (el exponente sale borroso). Esos dos datos **no son coherentes entre sí**: $n=10^{29}$ da $1.26\times10^{-18}$ J $=7.9$ eV, y $5$ eV corresponde a $n\approx5\times10^{28}$ m⁻³ (para $n=10^{28}$ saldría 1.7 eV). Es una errata o redondeo del libro, no del OCR. Usa los números de las notas.
- En p. 205 el libro toma $E_F(0)=5$ eV y $k_BT\approx0.03$ eV a 300 K (coherente con el ejemplo de 5 eV; solo el $n=10^{29}$ de p. 204 es el desajuste). La numeración de ecuaciones (6.xx) es la del libro, no la de las diapositivas.
- **Notación y una inconsistencia menor del libro:** $N(E)$ (6.53) es la densidad de estados **por espín y por volumen**; en (6.54)-(6.55) la usa con factor 2 explícito, pero en (6.58), (6.62)-(6.64) la usa **sin** el 2 y aun así llega a los resultados correctos ($C_e=\tfrac{\pi^2}{3}k_B^2N[E_F(0)]T=\tfrac{\pi^2}{2}k_Bn\,k_BT/E_F(0)$, que exige $N(E_F)=3n/2E_F$, o sea la DOS total). Si rehaces (6.62-6.64), usa la DOS total $D=3n/2E_F$ (nota `03`).
- Pavlov usa $E_F$ para la energía de Fermi y $T_F\approx5\times10^4$ K como temperatura de degeneración.

### Puntos clave para dominar este tema
- Saber en qué sección del Pavlov repasar cada subtema (tabla de arriba) y qué parte **no** viene en el libro (Drude, 1D, metales/cristal metálico).
- $C_e/C_{clás}=\tfrac{\pi^2}{3}k_BT/E_F\approx10^{-2}$ a 300 K (consistente con $C_e\approx\tfrac{\pi^2}{2}R\,T/T_F$ de la nota `02`).
