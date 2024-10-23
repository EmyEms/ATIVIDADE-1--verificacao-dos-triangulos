def verificar_lal(l1_t1, l2_t1, ang_t1, l1_t2, l2_t2, ang_t2):
    return (l1_t1 / l1_t2 == l2_t1 / l2_t2) and (ang_t1 == ang_t2)

def verificar_aa(angs_t1, angs_t2):
    return sorted(angs_t1) == sorted(angs_t2)

def verificar_lll(lados_t1, lados_t2):
    proporcoes = [lados_t1[i] / lados_t2[i] for i in range(3)]
    return proporcoes[0] == proporcoes[1] == proporcoes[2]

# Dados de entrada
lados_t1 = [float(input("Lado a1: ")), float(input("Lado b1: ")), float(input("Lado c1: "))]
angulos_t1 = [float(input("Ângulo A1: ")), float(input("Ângulo B1: ")), float(input("Ângulo C1: "))]

lados_t2 = [float(input("Lado a2: ")), float(input("Lado b2: ")), float(input("Lado c2: "))]
angulos_t2 = [float(input("Ângulo A2: ")), float(input("Ângulo B2: ")), float(input("Ângulo C2: "))]

# Verificação de semelhança
if verificar_aa(angulos_t1, angulos_t2):
    print("Semelhantes pelo critério AA")
elif verificar_lll(lados_t1, lados_t2):
    print("Semelhantes pelo critério LLL")
elif verificar_lal(lados_t1[0], lados_t1[1], angulos_t1[1], lados_t2[0], lados_t2[1], angulos_t2[1]):
    print("Semelhantes pelo critério LAL")
else:
    print("Os triângulos não são semelhantes.")
