"""
Quick-Calc: A Simple Calculator Application

This module provides core calculation functionality for the Quick-Calc application.
It implements the four basic arithmetic operations with proper error handling.
"""


class CalculationError(Exception):
    """Base exception for calculation errors."""
    pass


class DivisionByZeroError(CalculationError):
    """Raised when attempting to divide by zero."""
    pass


class Calculator:
    """
    A simple calculator that performs basic arithmetic operations.
    
    This class provides methods for addition, subtraction, multiplication,
    and division, with proper error handling for edge cases.
    """
    
    def __init__(self):
        """Initialize the calculator with zero as the starting value."""
        self.result = 0
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The sum of a and b
        """
        self.result = a + b
        return self.result
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract the second number from the first.
        
        Args:
            a: First number (minuend)
            b: Second number (subtrahend)
            
        Returns:
            The difference (a - b)
        """
        self.result = a - b
        return self.result
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            The product of a and b
        """
        self.result = a * b
        return self.result
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide the first number by the second.
        
        Args:
            a: First number (dividend)
            b: Second number (divisor)
            
        Returns:
            The quotient (a / b)
            
        Raises:
            DivisionByZeroError: If b is zero
        """
        if b == 0:
            raise DivisionByZeroError("Cannot divide by zero")
        self.result = a / b
        return self.result
    
    def clear(self) -> float:
        """
        Clear the calculator and reset to zero.
        
        Returns:
            Zero
        """
        self.result = 0
        return self.result
    
    def get_result(self) -> float:
        """
        Get the current result without modifying it.
        
        Returns:
            The current result
        """
        return self.result
