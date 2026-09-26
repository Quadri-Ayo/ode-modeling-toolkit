import numpy as np
from scipy.integrate import solve_ivp
from typing import Dict, List, Tuple, Any

class BaseODEModel:
    """
    An abstract base class for deterministic compartmental ODE models.
    
    This class handles the initialization of parameters and the numerical 
    integration wrapper. Subclasses must define the specific ODE system 
    by overriding the `equations` method.
    """
    def __init__(self, parameters: Dict[str, float], initial_conditions: List[float]):
        """
        Initializes the model with epidemic parameters and starting population states.
        
        Args:
            parameters: Dictionary containing transmission rates, recovery rates, etc.
            initial_conditions: List of initial values for each state variable.
        """
        self.params = parameters
        self.y0 = initial_conditions
        self.solution = None

    def equations(self, t: float, y: List[float]) -> List[float]:
        """
        The system of ordinary differential equations.
        
        Args:
            t: Time variable.
            y: List of current state variables (e.g., [S, E, I, R]).
            
        Returns:
            List of derivatives [dS/dt, dE/dt, dI/dt, ...]
        """
        raise NotImplementedError("Subclasses must implement the 'equations' method.")

    def solve(self, t_span: Tuple[float, float], t_eval: np.ndarray = None, method: str = 'RK45', **kwargs) -> Any:
        """
        Numerically integrates the ODE system.
        
        Args:
            t_span: Tuple of (start_time, end_time).
            t_eval: Specific time points to evaluate and store the solution.
            method: Integration method ('RK45', 'Radau', 'BDF', etc.).
            kwargs: Additional arguments to pass to scipy.integrate.solve_ivp.
            
        Returns:
            An ODESolution object containing time points (t) and state values (y).
        """
        self.solution = solve_ivp(
            fun=self.equations,
            t_span=t_span,
            y0=self.y0,
            t_eval=t_eval,
            method=method,
            **kwargs
        )
        
        if not self.solution.success:
            raise RuntimeError(f"ODE solver failed: {self.solution.message}")
            
        return self.solution