def traductor(secuencia): 
  """
  Función traductor realiza la traducción de nucleótidos a aminoácidos
  input: 
  secuencia: secuencia de nucleótidos
  output: 
  sencuecia: secuencia de nucleótidos codificantes
  péptido: secuencia de amino ácidos
  """
  seqc = secuencia[secuencia.find("ATG"):]
  peptido = ""
  for i in range(len(seqc)):
      i *= 3
      codon = seqc[i:i+3]
      if len(codon) < 3: # no reconoce como codon si hay 0,1,2 Nucleotidos
          break
      AmAc = codon_dictionary[codon] # cambiar por un código
      if AmAc =="_":
        break
      peptido += AmAc  #equivale al append
  return([seqc,peptido])


def gcp(secuencia):
   """
   gcp realiza el cálculo del porcentaje de contenido de Gc y Cs
   input: secuencia de nucléotidos
   output: porcentaje de gc
   """
   pgc = round(100*(secuencia.count("C") + secuencia.count("G"))/len(secuencia), 2)
   return pgc