algoritmo PERSONA estructura
    identificador : ENTERO	        
    edad : ENTERO	   
    identidad : IDENTIDAD	
    padre : ENTERO	
    madre : ENTERO
fin PERSONA

algoritmo edades	
# Selección de los identificadores de las personas por franja	
# de edades.
Entrada	
  familias : TABLA[PERSONA]	# El objetivo de la selección	 
  edad_min : ENTERO	# El límite de base de la selección	 
  edad_max : ENTERO	# El límite superior
Resultado : TABLA[ENTERO][1, 500]
precondición	
  familias ≠ NULO	 
  edad_min ≠ NULO ; edad_max ≠ NULO
constante	
  MIN : ENTERO ← índice_min(familias)	
  MAX : ENTERO ← índice_max(familias)	
  MIN_EDADES : ENTERO ← índice_min(Resultado)	
  MAX_EDADES : ENTERO ← índice_max(Resultado)	  
  INFINITO : ENTERO ← ENTERO_MIN		# El número entero más pequeño utilizable	
  HUERFANO : ENTERO ← INFINITO	  
  BORRADO : ENTERO ← HUERFANO + 1	    
  VACIO : ENTERO ← HUERFANO + 2
variable	
  i : ENTERO		# Índice de la siguiente celda a observar	
  j : ENTERO			# Índice siguiente celda de Resultado a inicializar
inicialización	
  i ← MIN ; j ← MIN_EDADES	
  Resultado[MIN_EDADES] ← VACIO	
  afirmación		
    i > MIN y j > MIN_EDADES =>		
    Las celdas de sub_tabla(Resultado, MIN_EDADES, j-1)		
    se inicializan con los identificadores de las celdas 		
    de sub_tabla(familias, MIN, i-1) donde los		
    identificadores no son ni BORRADO ni VACIO y la edad		
    está entre `edad_min' y `edad_max'
  realización	
    hasta que		
      familias[i].identificador = VACIO		
      o si no i > MAX
		  invariante			
        ???		
      variante de control			
        MAX -i + 1	
    repetir		
        si			
            familias[i].identificador ≠ BORRADO		    
          y entonces			
            edad_min ≤ familias[i].edad ≤ edad_max		
            
        entonces			
          Resultado[j] ← familias[i].identificador			
          j ← j + 1		
          
        fin si		
        i ← i + 1
	fin repetir
postcondición	
  # Resultado está VACIO cuando los límites de edades no están en	
  # orden	
  edad_min > edad_max => Resultado[1] = VACIO	
  (∀k ∈ ℤ)(		
    índice_min(Resultado) ≤ k ≤ índice_max(Resultado)		
    =>
		Resultado[k] es el identificador de una persona de edad		
    entre `edad_min' y `edad_max' años		
    )
fin edades

algoritmo envejecer	
# Envejece la población un año.
Entrada	
  familias : TABLA[PERSONA]
precondición	
  familias ≠ NULO
constante	
  MIN : ENTERO ← índice_min(familias)	
  MAX : ENTERO ← índice_max(familias)	  
    INFINITO : ENTERO ← ENTERO_MIN		
  # El número entero más pequeño utilizable	
  HUERFANO : ENTERO ← INFINITO	  
  BORRADO : ENTERO ← HUERFANO + 1	    
  VACIO : ENTERO ← HUERFANO + 2
variable	
  i : ENTERO	# Índice de la siguiente celda a tratar
  
inicialización	
  i ← MIN
realización	
  hasta que 		
      familias[i].identificador = VACIO 	    
    o si no		
      i > MAX		
      invariante		
        ???		
      variante de control			
        MAX – i + 1	
  repetir		
      si		    
        familias[i].identificador ≠ BORRADO		
      entonces		    
        familias[i].edad ← familias[i].edad + 1		
      fin si		
        i ← i + 1	
    fin repetir
postcondición	
  Se han incrementado todos los atributos `edad' de las celdas	ni VACIO ni BORRADO
fin envejecer