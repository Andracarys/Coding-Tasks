# Encontra el mayor de tres numeros

a = 100
b = 500
c = 200

mayor = max(a, b, c)
print(mayor)

# -----------------------------

lista = [a, b, c]
major = a  # mayor por defecto

for num in lista:
    if num > major:
        major = num

print(major)

###
