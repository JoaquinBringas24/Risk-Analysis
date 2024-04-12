import ctypes 
import os
os.chdir("./")


def woe(good:float, bad:float):
    
    """ Calculate the Weight of Evidence
    
    Parameters:
    good (float): The percentage of customers that payed the loan.
    
    bad (float): The percentage of custumers that did not payed the loan.
    
    Returns:
    float WoE.
    """
    
    clibrary = ctypes.CDLL('F:/Python/proyectos/Risk_Analysis/functions.dll')
    func = clibrary.WoE
    func.argtypes = [ctypes.c_double, ctypes.c_double]
    func.restype = ctypes.c_double
    
    return func(good, bad)
    
        


if __name__ == "__main__":
    None