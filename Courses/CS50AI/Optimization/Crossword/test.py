

for v1 in variables:
    for v2 in variables:

         if v1 == v2:
              continue
        
        cells1 = v1.cells
        cells2 = v2.cells
    
        for cell in cells1:
          if cell in cells2:
              overlaps.add(cell)