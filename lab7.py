import numpy as np

def massiv_yarat_ve_yaz(fayl_adi, n):
    # n x n ölçüsündə təsadüfi ədədi massiv yaradırıq
    A = np.random.randint(1, 10, (n, n))
    
    # Massivi fayla yazırıq
    with open(fayl_adi, 'w') as f:
        for row in A:
            f.write(' '.join(map(str, row)) + '\n')
    
    return A

def fayldan_oxu_ve_yeni_fayl_yaz(input_fayl_adi, output_fayl_adi):
    # Fayldan oxuyuruq
    with open(input_fayl_adi, 'r') as f:
        lines = f.readlines()
    
    # Fayldan oxunan massiv
    A = [list(map(int, line.split())) for line in lines]
    A = np.array(A)
    
    # Yeni massivin elementlərini iki dəfə artırırıq
    yeni_A = A * 2
    
    # Yeni fayla yazırıq
    with open(output_fayl_adi, 'w') as f:
        for row in yeni_A:
            f.write(' '.join(map(str, row)) + '\n')
    
    # Elementlərin cəm hesablanır
    toplam = np.sum(yeni_A)
    
    return yeni_A, toplam

# Fayl adları
input_fayl_adi = 'massiv.txt'
output_fayl_adi = 'yeni_massiv.txt'

# ədədi massiv ölçüsünü daxil edirik
n = int(input("n ölçüsünü daxil edin: "))

# Massivi yaradıb fayla yazırıq
A = massiv_yarat_ve_yaz(input_fayl_adi, n)

# Fayldan oxuyub yeni massiv yaradıb, cəmini hesablayırıq
yeni_A, toplam = fayldan_oxu_ve_yeni_fayl_yaz(input_fayl_adi, output_fayl_adi)

print("\nYeni massiv:")
print(yeni_A)

print(f"\nYeni massivin cəmi: {toplam}")
