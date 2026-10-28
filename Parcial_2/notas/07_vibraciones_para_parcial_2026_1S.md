# Vibraciones de red que cayeron en el Parcial II (2026-1S) (bloque 7)

> **Nota de origen:** este archivo **no** sale de `Metales 2021.pdf`. El examen `P-2026-1S` ("Parcial II (S I 2026)", 20 preguntas de selección múltiple, nota del estudiante 11/20) mezcla 19 preguntas de vibraciones de red con 1 de metales (#11). La teoría completa está en `Parcial_1/notas/` (cadena monoatómica `01b`, diatómica `02`, fonones y calor específico `03`, conductividad térmica y Umklapp `06`); aquí va el resumen mínimo para resolver cada pregunta, sin citas `[p. N]`. La clave de respuestas se dedujo por física; ver `examenes/guia_teoria_por_examen.md` §P-2026-1S para el enunciado completo de cada pregunta.

Notación: $C$ constante de fuerza entre primeros vecinos, $a$ parámetro de red, $q$ vector de onda, $G=2\pi/a$ vector de red recíproca, primera zona de Brillouin $-\pi/a<q\le\pi/a$.

## 22. Velocidad de fase, velocidad de grupo y medios dispersivos (`vib.1`)

- $v_f=\omega/q$ (fase) y $v_g=d\omega/dq$ (grupo, velocidad de la energía). **Medio dispersivo** ⇔ $\omega(q)$ no es lineal ⇔ $v_f\ne v_g$. En un medio no dispersivo ($\omega=v_sq$) coinciden.
- En un sólido $\omega(q)$ es **periódica** en $q$ con periodo $G=2\pi/a$ → $v_g(q)$ también es periódica y con la misma periodicidad (`P-2026-1S #1`).
- A $q$ pequeño $v_g\to v_s$ (velocidad del sonido, no cero). La velocidad del sonido sale de la **primera** derivada de $\omega(q)$ a $q\to0$ (pendiente inicial), no de la segunda.
- Cadena monoatómica: $\omega=2\sqrt{C/M}\,|\sin(qa/2)|$, $v_g=a\sqrt{C/M}\cos(qa/2)$, $v_g(\pi/a)=0$.

### Puntos clave para dominar este tema
- Definir $v_f$ y $v_g$ y por qué $v_f\ne v_g$ define un medio dispersivo (`#8`).
- Saber que $v_g(q)$ hereda la periodicidad de $\omega(q)$ (`#1`) y que $v_g\to v_s$ cuando $q\to0$.

---

## 23. Cadena monoatómica: zona de Brillouin, equivalencia de ondas y $\lambda_{min}=2a$ (`vib.2`)

- Los desplazamientos solo se evalúan en los nodos $x_n=na$: $u_n=Ae^{i(qna-\omega t)}$. Dos $q$ que difieren en $G=2\pi/a$ dan **el mismo** $u_n$ para todo $n$ (aliasing). Por eso basta la primera ZB.
- $\lambda=6a$ ⇒ $q_1=2\pi/6a=\pi/3a$; $\lambda=6a/7$ ⇒ $q_2=7\pi/3a=q_1+2\pi/a$. Representan **el mismo movimiento atómico** (mismas oscilaciones, en fase) (`#2`).
- Longitud de onda mínima físicamente distinguible: $\lambda=2a$ ($q=\pi/a$): cada átomo oscila **en contrafase** con sus vecinos (`#7`).
- Densidad de estados 1D: $g(\omega)\propto1/|v_g|$; en $q=\pi/a$, $v_g=0$ ⇒ $g(\omega)$ **diverge** (singularidad de van Hove, ondas estacionarias) (`#3`).

### Puntos clave para dominar este tema
- Explicar el aliasing: $q$ y $q+G$ son físicamente equivalentes; por eso $\lambda=6a$ y $6a/7$ son la misma onda en la red.
- En $q=\pi/a$: $\lambda=2a$, vecinos en contrafase, $v_g=0$, $g(\omega)\to\infty$.

---

## 24. Modos normales, condiciones de frontera y mecánica de las ramas (`vib.3`)

- **Cuántos modos** hay en un sólido finito: se cuentan imponiendo condiciones de frontera (fijas o periódicas) a las soluciones de la ecuación de onda; la analogía con la **cuerda vibrante** vale porque la ecuación diferencial y las condiciones de frontera admiten el mismo conjunto de soluciones independientes (ondas estacionarias), no porque las velocidades sean parecidas (`#6`). Con $N$ átomos hay $N$ valores de $q$ por rama ($3N$ modos en 3D).
- **Condición de Bragg y ondas elásticas:** la red es **periódica** y el campo acústico tiene **naturaleza ondulatoria**; ambas cosas juntas dan reflexión de Bragg/difracción $2a\sin\theta=n\lambda$, aquí en la frontera de zona $q=\pi/a$ (`#9`). No requiere que fonón y fotón tengan energías comparables ni que el campo acústico sea electromagnético.
- **3 ramas acústicas en 3D** (1 longitudinal, 2 transversales): $\omega_L>\omega_T$ porque las fuerzas restauradoras de compresión (longitudinal) son mayores que las de cizalladura (transversal): se explica con las **leyes de Newton** (fuerzas elásticas) (`#10`).

### Puntos clave para dominar este tema
- Contar modos con condiciones de frontera; justificar la analogía cuerda-sólido por la ecuación diferencial y las condiciones de frontera.
- Explicar por qué aparece Bragg: onda + periodicidad.
- Explicar $\omega_L>\omega_T$ desde constantes de fuerza (mecánica clásica).

---

## 25. Cadena diatómica: ramas, gap y borde de zona (`vib.4`)

Masas $M>m$, constante $C$, parámetro $a$ (distancia entre vecinos):

$$\omega^2=C\left(\frac1M+\frac1m\right)\pm C\sqrt{\left(\frac1M+\frac1m\right)^2-\frac{4\sin^2(qa)}{Mm}}$$

(con $a$ = separación entre vecinos y celda de longitud $2a$, zona $|q|\le\pi/2a$; revisa la convención en `Parcial_1/notas/02_cadena_diatomica.md`).

- $q=0$: acústica $\omega=0$; óptica $\omega=\sqrt{2C(1/M+1/m)}$.
- Borde de zona: acústica $\omega_A=\sqrt{2C/M}$ (máxima de la rama), óptica $\omega_O=\sqrt{2C/m}$ (mínima de la rama). **Brecha** $=\sqrt{2C/m}-\sqrt{2C/M}$, $v_g=0$ en **ambas** ramas (`#13`).
- **Diferencia principal acústica/óptica:** en la acústica el **centro de masa se mueve** (átomos en fase a $q\to0$); en la óptica el centro de masa permanece fijo (átomos en contrafase) (`#4`).
- **Frecuencia en la brecha:** el $q$ es **complejo** ($q=q_r+i\kappa$): la onda se atenúa (evanescente); la descripción más precisa es "vector de onda complejo", y "onda amortiguada" es su consecuencia (`#5`).
- **$M\to m$:** la brecha se cierra ($\omega_A=\omega_O$ en el borde): **se estrecha y desaparece cuando $M=m$**; la cadena equivale a una monoatómica de celda más pequeña (`#12`).
- **Masas ↑ con $C$ fija:** todas las $\omega\propto1/\sqrt{\text{masa}}$ **disminuyen** (`#14`).
- **Borde de zona, rama óptica con $M>m$:** a $\omega_O=\sqrt{2C/m}$ se mueven **solo los átomos ligeros $m$**, los pesados $M$ quedan inmóviles (en la acústica, al revés: solo los pesados) (`#15`).

### Puntos clave para dominar este tema
- Escribir $\omega_A=\sqrt{2C/M}$, $\omega_O=\sqrt{2C/m}$ en el borde y $v_g=0$ en ambas.
- Distinguir ramas por movimiento del centro de masa; explicar qué átomo se mueve en cada rama del borde de zona.
- Predecir el efecto de $M\to m$ (gap cierra) y de escalar masas ($\omega\propto M^{-1/2}$).
- Interpretar la onda con $\omega$ en la brecha (decaimiento exponencial, $q$ complejo).

---

## 26. Procesos Umklapp y conductividad térmica de fonones (`vib.5`)

- **Proceso normal (N):** $\mathbf q_1+\mathbf q_2=\mathbf q_3$, conserva el momento cristalino y **no** da resistencia térmica. **Proceso Umklapp (U):** $\mathbf q_1+\mathbf q_2=\mathbf q_3+\mathbf G$ con $\mathbf G\ne0$; el momento cristalino cambia en un vector de red recíproca, el flujo de fonones se reorienta (puede invertirse) (`#16`).
- Para que ocurra un U hacen falta fonones con $|\mathbf q|\gtrsim|\mathbf G|/2$ (de orden $\pi/a$), es decir con energía de orden $k_B\Theta_D/2$: están poblados solo a $T$ moderada/alta; a $T\to0$ los U se **congelan** ($\propto e^{-\Theta/2T}$) (`#18`, `#17`).
- Por eso los U son los que dan **resistencia térmica en aislantes puros a $T$ altas** ($\kappa\propto1/T$): reorientan el flujo neto de energía y, por tanto, impiden el flujo de calor (`#17`).
- **$T\to0$, cristal finito:** $\ell$ queda limitado por el tamaño de la muestra (dispersión en la frontera), constante; $\kappa=\tfrac13C_v v\ell\propto C_v\propto T^3$ (`#19`). Máximo de $\kappa$ a $T\sim\Theta_D/20$.
- **Modos ópticos:** contribuyen poco porque su $v_g=d\omega/dq$ es muy pequeña o casi nula (rama casi plana) (`#20`).

### Puntos clave para dominar este tema
- Definir N vs. U (conservación de $\hbar\mathbf q$ módulo $\hbar\mathbf G$) y por qué solo U da resistencia.
- Dar el criterio $|q|\gtrsim|G|/2$ y su consecuencia con $T$ (U congelados a baja $T$).
- Conocer $\kappa\propto T^3$ (muy baja $T$, tamaño finito), pico intermedio y $\kappa\propto1/T$ (alta $T$, U dominantes).
- Explicar la poca contribución de los ópticos ($v_g\approx0$).

---

## 27. Pregunta del parcial sobre metales: definición de $E_F$ (`vib.6`)

$E_F$ a $T=0$ K es la energía del **estado cuántico ocupado más alto** del estado fundamental del gas de electrones (no la energía promedio, no el nivel de ocupación 0.5 —esa es $\mu(T>0)$—, no la función trabajo $\phi$) (`P-2026-1S #11`). Teoría: `fermi3d.1` y `cal.2` en `03_gas_de_fermi_3D.md` y `02_estadistica_fermi_calor_especifico.md`.

### Puntos clave para dominar este tema
- Definir $E_F$ como el nivel ocupado más alto a $T=0$ y distinguirlo de $\mu(T)$, de la energía media ($\tfrac35E_F$) y de la función trabajo.
