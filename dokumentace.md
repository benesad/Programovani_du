# Domácí úkol č. 1
## Zobrazení
Tento program slouží jako nástroj na zobrazení sítě zadaného geografického 
zobrazení a přepočet uživatelem zadaných bodůzeměpisné šířky a délky podle 
vzorců definovaných pro každé zvlášť.

## Seznam zobrazení
- `Or` - Ortografická projekce
- `Ma` - Marinovo zobrazení
- `Lk` - Lambertovo zobrazení kuželové
- `Sa` - Sansonovo zobrazení

## Jak to funguje?
Program vyzve uživatele, který si následně vybere jaké zobrazení chce použít.  
Po zvolení se zeptá na měřítko, které uživatel preferuje. Fuknce je nastavena tak, 
aby uživatel zadal jen měřítko v celočíselném formátu bez nutnosti psát cokoliv jiného. 
Bude-li chtít uživatel `100 000 000`, stačí napsat 100000000.  
Dále je možnost zvolit poloměr Země se kterým má program počítat, případně
lze použít defaultní `6371,11 km`.
