from typing import Sequence, Dict, List, Tuple, Set


def lower_join(seq: Sequence [str]) -> str:
    """Принимает на вход последовательность и создаёт из неё  
    строку в нижнем регистре."""
    return ''.join(seq).lower()
