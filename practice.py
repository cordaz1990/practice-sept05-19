def __lt__(self, other):
    #check the suits
    if self.suit < other.suit: return True
    if self.suit > other.suit: return False
    
    #suits are the sme ... check ranks
    return self.rank <other.rank


def __lt__(self, other):
    t1 = self.suit, self.rank
    t2 = other.suit, other.rank
    return t1 < t2
  
