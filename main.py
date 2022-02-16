from protein import Protein
from ligand import Ligand
from complex import Complex

def main():
  p1 = Protein()
  l1 = Ligand()
  p2 = Protein()
  l2 = Ligand()

  complex = Complex()
  c2 = Complex()
  complex.add(p1)
  complex.add(l1)
  complex.add(p2)
  c2.add(p1)
  c2.add(complex)

  print (c2.operation())


if __name__ == '__main__':
  main()
  