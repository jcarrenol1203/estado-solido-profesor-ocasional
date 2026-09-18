# Cadena lineal diatómica 1D (sección 1.2)

> **Nota de origen:** cubre las páginas 142-153 del PDF. Es la derivación completa (única en todo el documento, no aparece antes de la página 101) de la cadena lineal diatómica: ecuaciones de movimiento, ramas acústica y óptica, dinámica de cada rama, la "zona prohibida" (gap) con ondas evanescentes, y el conteo de modos en la primera zona de Brillouin.

## Ecuaciones de movimiento

Cadena 1D con dos tipos de átomos alternados, masas $M_1$ y $M_2$ ($M_1<M_2$), con constante de fuerza $\alpha$ entre primeros vecinos. La **celda unitaria** contiene 2 átomos ($M_1$ y $M_2$), con longitud $2a$. Hay $2N$ átomos en la red ($N$ celdas unitarias). [p. 142]

Ecuaciones de movimiento (átomo par $2n$ = $M_1$, átomo impar $2n+1$ = $M_2$), acopladas:

$$(1)\quad M_2\frac{d^2u_{2n+1}}{dt^2} = -\alpha(2u_{2n+1}-u_{2n}-u_{2n+2})$$
$$(2)\quad M_1\frac{d^2u_{2n}}{dt^2} = -\alpha(2u_{2n}-u_{2n+1}-u_{2n-1})$$ [p. 142]

Existen $2N$ ecuaciones acopladas en total ($N$=número de celdas unitarias).

## Soluciones ondulatorias y ecuación secular

Se proponen soluciones tipo onda viajera, una amplitud distinta para cada subred:
$$u_{2n}(x,t) = A_1e^{i(q\cdot 2na-\omega t)}, \qquad u_{2n+1}(x,t) = A_2e^{i[q(2n+1)a-\omega t]}$$ [p. 143]

de donde $u_{2n+2}=u_{2n}e^{i2qa}$ y $u_{2n-1}=u_{2n+1}e^{-i2qa}$ (relación 1A). Sustituyendo en (1) y (2) se obtienen dos ecuaciones **homogéneas** en $u_{2n}$, $u_{2n+1}$: [p. 143]

$$(3)\quad (M_1\omega^2-2\alpha)u_{2n} + \alpha(1+e^{-i2qa})u_{2n+1} = 0$$
$$(4)\quad \alpha(1+e^{i2qa})u_{2n} + (M_2\omega^2-2\alpha)u_{2n+1} = 0$$

La solución trivial es $u_{2n}=u_{2n+1}=0$; para que existan **otras soluciones**, el determinante del sistema debe anularse. [p. 143, 144]

**Ecuación secular** (usando $1+\cos2qa=2\cos^2qa$):

$$(2\alpha-M_1\omega^2)(2\alpha-M_2\omega^2) - 4\alpha^2\cos^2qa = 0$$

que se reordena como una ecuación bicuadrática en $\omega$:

$$\omega^4 - \frac{2\alpha(M_1+M_2)}{M_1M_2}\omega^2 + \frac{4\alpha^2}{M_1M_2}\sin^2qa = 0$$ [p. 144]

Resolviendo esta cuadrática en $\omega^2$:

$$\boxed{\omega^2 = \alpha\left(\frac1{M_1}+\frac1{M_2}\right) \pm \alpha\sqrt{\left(\frac1{M_1}+\frac1{M_2}\right)^2 - \frac{4\sin^2qa}{M_1M_2}}}$$ [p. 144]

## Ramas acústica y óptica

Las dos raíces (signo $-$ y signo $+$) definen dos ramas de dispersión, separadas por un **gap** (zona prohibida): [p. 145]

- **Rama acústica** (signo $-$): en $q=0$, $\omega=0$.
- **Rama óptica** (signo $+$): en $q=0$,
$$\omega(0) = \left[2\alpha\left(\frac1{M_1}+\frac1{M_2}\right)\right]^{1/2}$$ [p. 145]

En el borde de zona $q=\pi/2a$ (ver más abajo, 1ª ZB para esta red): la rama acústica alcanza $\omega=(2\alpha/M_2)^{1/2}$ y la rama óptica alcanza $\omega=(2\alpha/M_1)^{1/2}$ (recordando $M_1<M_2$). Entre estos dos valores existe un **gap de frecuencias prohibidas** que ninguna rama alcanza. [p. 145]

### Límite de longitud de onda larga en la rama acústica

Para $q,\omega$ pequeños, se puede aproximar $\sin^2qa\approx(qa)^2$ en la ecuación bicuadrática, obteniéndose: [p. 146]

$$\omega \cong qa\sqrt{\frac{2\alpha}{M_1+M_2}} \qquad\Rightarrow\qquad v_p = \frac{\omega}{q} = a\sqrt{\frac{2\alpha}{M_1+M_2}}$$

Esta es la velocidad de fase de la rama acústica en el límite $q\to0$ (análoga a $v_s$ de una cadena monoatómica de masa promedio).

## Dinámica de cada rama: relación de amplitudes $A_2/A_1$

De las ecuaciones (1A) y (4):
$$\frac{u_{2n+1}}{u_{2n}} = \frac{\alpha(1+e^{i2qa})}{2\alpha-M_2\omega^2} = \frac{A_2}{A_1}e^{iqa} \;\Rightarrow\; \frac{A_2}{A_1} = \frac{\cos qa}{1-\dfrac{M_2\omega^2}{2\alpha}}$$ [p. 147]

**1. Rama acústica, límite $\lambda\gg a$ ($q\to0$):** $\cos qa\to1$ y $\omega\to0$ $\Rightarrow$
$$\frac{A_2}{A_1} = 1$$
Ambos átomos de la celda vibran **en fase y con igual amplitud** $\Rightarrow$ **movimiento de cuerpo rígido** (toda la celda se traslada junta, como en el límite $q\to0$ de la cadena monoatómica). [p. 147]

**2. Rama óptica, límite $q\to0$:** $\cos qa\to1$, y sustituyendo $\omega(0)=[2\alpha(1/M_1+1/M_2)]^{1/2}$ en la fórmula de $A_2/A_1$:
$$\frac{A_2}{A_1} = -\frac{M_1}{M_2}$$
Los dos átomos vibran **en contrafase** ($\pi$ fuera de fase), con amplitudes inversamente proporcionales a sus masas, de modo que el **centro de masa de la celda permanece fijo**. [p. 148]

**Interpretación física de "óptica"**: si los átomos de la celda tienen cargas opuestas (sólido iónico), este modo de vibración en contrafase genera un **momento dipolar oscilante** en cada celda, lo que produce **reflexión y absorción fuerte en el infrarrojo** (de ahí el nombre "óptica"). [p. 152]

## Zona prohibida (gap): ondas evanescentes con $q$ complejo

En el rango de frecuencias prohibido,
$$(2\alpha/M_2) < \omega^2 < (2\alpha/M_1) \qquad (*)$$
estas frecuencias **no se pueden propagar como vibraciones de red armónicas no amortiguadas**. [p. 149]

Reescribiendo la relación de dispersión:
$$\cos qa = \left[\left(1-\frac{M_1\omega^2}{2\alpha}\right)\left(1-\frac{M_2\omega^2}{2\alpha}\right)\right]^{1/2}$$

En el rango (*), uno de los factores es positivo (>1, ya que $M_1\omega^2/2\alpha<1$) y el otro es negativo (<1, ya que $M_2\omega^2/2\alpha>1$), de modo que el producto bajo la raíz es **negativo** $\Rightarrow \cos qa = i\delta$ con $\delta\in\mathbb R$ (imaginario puro) $\Rightarrow qa\notin\mathbb R$ ($q$ es complejo). [p. 149]

**Resolviendo $\cos(x+iy)=i\delta$:** usando $\cos(x+iy)=\cos x\cosh y - i\sin x\sinh y$, se separan parte real e imaginaria: [p. 150]
$$\cos x\cosh y = 0, \qquad \sin x\sinh y = -\delta$$
Como $\cosh y\neq0\;\forall y$, se requiere $\cos x=0 \Rightarrow x=\pm\pi/2 \Rightarrow \sin x=\pm1$. Sustituyendo en la segunda ecuación: $y=\mp\sinh^{-1}\delta$. Por tanto:
$$qa = x+iy = \pm\frac{\pi}{2} \mp i\sinh^{-1}\delta$$ [p. 150]

**Sustituyendo de vuelta en la solución ondulatoria** $u_{2n}=A_1e^{i[q(2n)a-\omega t]}$: [p. 151]
$$u_{2n} = \pm A_1 e^{-i\omega t}e^{\pm2n\sinh^{-1}\delta} = A_1e^{-i\omega t}e^{-2\kappa na}$$
con la **constante de atenuación**:
$$\kappa = \frac{1}{a}\sinh^{-1}\delta$$ [p. 151]

Es decir, en el gap la onda no se propaga: es una **oscilación amortiguada espacialmente** (decaimiento exponencial con $n$, análoga a una onda evanescente), no una onda armónica sostenida.

## Estimación numérica y simetría

Estimación numérica de $\omega$ en la rama óptica: $\omega\approx(2\alpha/M)^{1/2}\sim(2\times5\times10^3/10^{-23})^{1/2}\sim3\times10^{13}\,\text{s}^{-1}$. [p. 152]

$\omega(q)$ satisface las mismas propiedades de simetría que en el caso monoatómico, pero ahora con **periodo $\pi/a$** (en vez de $2\pi/a$), debido a que la celda unitaria tiene tamaño $2a$:
$$-\frac{\pi}{2a} < q < \frac{\pi}{2a} \;\equiv\; \text{primera zona de Brillouin para la red diatómica 1D}$$ [p. 152]

## Conteo de modos en la primera zona de Brillouin (red diatómica)

Con condiciones de frontera periódicas $q=n\cdot2\pi/L$: [p. 153]

- Longitud de la 1ª ZB: $2\left(\dfrac{\pi}{2a}\right) = \dfrac{\pi}{a}$
- Número de puntos $q$ dentro de la 1ª ZB: $\dfrac{\pi/a}{2\pi/L} = \dfrac{L}{2a} = N$ (número de celdas unitarias)
- **Número total de modos = $2N$** (2 ramas —acústica y óptica— por cada valor de $q$) $=$ número de grados de libertad del sistema ($2N$ átomos $\times$ 1 dimensión). [p. 153]

### Puntos clave para dominar este tema

- Puede plantear las dos ecuaciones de movimiento acopladas de la cadena diatómica y, sustituyendo soluciones de onda con amplitudes distintas $A_1$, $A_2$ para cada subred, llegar a la ecuación secular $(2\alpha-M_1\omega^2)(2\alpha-M_2\omega^2)-4\alpha^2\cos^2qa=0$.
- Puede resolver la ecuación bicuadrática resultante y mostrar que hay **dos ramas**: $\omega^2=\alpha(1/M_1+1/M_2)\pm\alpha\sqrt{(1/M_1+1/M_2)^2-4\sin^2(qa)/(M_1M_2)}$.
- Puede mostrar que en $q=0$ la rama acústica tiene $\omega=0$ mientras que la rama óptica tiene $\omega(0)=[2\alpha(1/M_1+1/M_2)]^{1/2}$ (finita) — este es el resultado distintivo del par acústica/óptica.
- Sabe interpretar físicamente cada rama en el límite $q\to0$: acústica $\Rightarrow A_2/A_1=1$ (átomos en fase, cuerpo rígido); óptica $\Rightarrow A_2/A_1=-M_1/M_2$ (átomos en contrafase, centro de masa fijo, genera momento dipolar oscilante y por eso absorbe en el infrarrojo).
- Puede explicar el origen matemático y físico de la **zona prohibida (gap)**: entre $(2\alpha/M_2)^{1/2}$ y $(2\alpha/M_1)^{1/2}$, $\cos qa$ se vuelve imaginario puro, $q$ es complejo ($qa=\pm\pi/2\mp i\sinh^{-1}\delta$), y la "onda" resultante decae exponencialmente en el espacio ($\kappa=\sinh^{-1}(\delta)/a$) en vez de propagarse.
- Sabe que la primera zona de Brillouin de la red diatómica es $-\pi/2a<q<\pi/2a$ (periodo $\pi/a$, la mitad que en la monoatómica, por la celda de tamaño $2a$), y que el número total de modos es $2N$ (N celdas unitarias × 2 ramas), igual al número de grados de libertad.
