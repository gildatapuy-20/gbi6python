def ecor1(seq, enzima):
  """
  Función ecor1 realiza cortes e imprime los fragmentos
  input: 
  secuencia : Secuencia de ADN o ARN.
  output: 
  sitios_corte: Lista de fragmentos extraídos de la secuencia y longitud de las mismas
  """
  sitios_corte = []
  secuencia = seq 
    
  while True:
        sitiocorte = secuencia.find(enzima)
        if sitiocorte == -1:
            break
        frag1 = secuencia[:sitiocorte + len(enzima)]
        frag2 = secuencia[sitiocorte + len(enzima):]
        sitios_corte.append((frag1, len(frag1)))
        secuencia = frag2
  sitios_corte.append((secuencia, len(secuencia))) 

  return ([sitios_corte])

