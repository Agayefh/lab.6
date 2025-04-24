import numpy as np

def geometri_orta(sutun):
    # Sütundakı müsbət elementləri seçirik
    positif_elements = [elem for elem in sutun if elem > 0]
    
    # Əgər müsbət elementlər varsa, həndəsi ortanı tapırıq
    if len(positif_elements) > 0:
        product = np.prod(positif_elements)
        return product ** (1 / len(positif_elements))
    else:
        return 0  # Əgər heç bir müsbət element yoxdursa, sıfır qaytarırıq

def baş_diaqonalı_yenilə(matrix):
    n = matrix.shape[0]  # Matrisi A(n,n) olaraq qəbul edirik
    for i in range(n):
        # i-ci sütundakı müsbət elementlərin həndəsi ortasını tapırıq
        geometri_ortası = geometri_orta(matrix[:, i])
        # Həndəsi ortanı baş diaqonala yazırıq
        matrix[i, i] = geometri_ortası
    return matrix

# Matrisin ölçüsünü (n,n) daxil edirik
n = int(input("n ölçüsünü daxil edin: "))

# n x n ölçüsündə təsadüfi matris yaradırıq
A = np.random.randint(-10, 10, (n, n))
print("Əvvəlki Matris:")
print(A)

# Baş diaqonaldakı elementləri yeniləyirik
A_yenilənmiş = baş_diaqonalı_yenilə(A)

print("\nYenilənmiş Matris:")
print(A_yenilənmiş)
