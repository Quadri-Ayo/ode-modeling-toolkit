## How the Toolkit Works

The central design principle is to separate the **mathematical definition of a dynamical system** from the numerical procedure used to solve it.

Instead of rewriting an ODE solver for every model, a model is represented through its mathematical right-hand side:

$$
\frac{d\mathbf{x}}{dt}=f(t,\mathbf{x},\theta).
$$

The model definition can then be passed to a reusable numerical solver.

### Example: Logistic Growth Model

Consider the logistic growth equation

$$
\frac{dN}{dt}
=
rN\left(1-\frac{N}{K}\right),
$$

where:

* \(N(t)\) is the population size;
* \(r\) is the intrinsic growth rate;
* \(K\) is the carrying capacity.

The model can be represented computationally as:

```python
import numpy as np

def logistic_model(t, y, r, K):
    N = y[0]
    dNdt = r * N * (1 - N / K)

    return np.array([dNdt])
```

The mathematical structure is therefore expressed directly in the model function, while the numerical integration is handled independently.

For example:

```python
from scipy.integrate import solve_ivp

r = 0.5
K = 100
N0 = 10

solution = solve_ivp(
    fun=lambda t, y: logistic_model(t, y, r, K),
    t_span=(0, 30),
    y0=[N0],
    t_eval=np.linspace(0, 30, 300)
)
```

The same numerical workflow can then be applied to a different system without rewriting the integration procedure.

---

## From One Equation to a General Dynamical System

The toolkit is designed around the general form

$$
\frac{d\mathbf{x}}{dt}
=
f(t,\mathbf{x};\theta),
$$

where \(\mathbf{x}\in\mathbb{R}^n\).

For example, an SIR epidemic model is given by

$$
\frac{dS}{dt}=-\beta SI,
$$

$$
\frac{dI}{dt}=\beta SI-\gamma I,
$$

$$
\frac{dR}{dt}=\gamma I.
$$

The corresponding implementation can be written as:

```python
def sir_model(t, y, beta, gamma):
    S, I, R = y

    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I

    return np.array([dSdt, dIdt, dRdt])
```

The same solver infrastructure can then integrate both the logistic model and the SIR system.

This separation between **model definition** and **numerical integration** is the core abstraction of the toolkit.

---

## Why This Abstraction Matters

Without a reusable framework, each mathematical model requires a separate implementation of:

1. the differential equations;
2. numerical integration;
3. parameter handling;
4. solution storage;
5. visualization;
6. analysis.

The toolkit instead aims to provide reusable computational components:

```text
Mathematical model
       │
       ▼
  Model function
       │
       ▼
Reusable ODE solver
       │
       ▼
Numerical solution
       │
   ┌───┴────┐
   ▼        ▼
Analysis  Visualization
```

This makes it possible to change the mathematical model while retaining the computational workflow.

---

## Intended Extension to Research Models

The abstraction is particularly useful for compartmental models in epidemiology.

For example:

```python
def malaria_model(t, y, params):
    # model equations
    ...
    return dydt
```

The same computational pipeline can then be used for:

* SIR models;
* SEIR models;
* vector-host models;
* malaria transmission models;
* predator-prey systems;
* population dynamics;
* and other systems of ordinary differential equations.

The objective is therefore not to provide a collection of isolated scripts, but to develop a reusable computational framework for mathematical modelling.

---

## Reproducible Experiment

Each model should be accompanied by a reproducible experiment containing:

* model definition;
* parameter values;
* initial conditions;
* integration interval;
* numerical solver;
* visualization;
* and, where applicable, analytical comparison.

For models with known analytical solutions, numerical results can also be compared against the corresponding exact solution to assess numerical behaviour.

---

## Current Scope

The current implementation focuses on deterministic ODE systems and provides the foundation for additional modelling functionality.

Future extensions include:

* parameter sweeps;
* sensitivity analysis;
* equilibrium detection;
* stability analysis;
* uncertainty quantification;
* stochastic models;
* and integration with parameter-estimation workflows.

> **Status:** Active computational research project.
