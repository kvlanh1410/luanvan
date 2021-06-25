import numpy as np
import matplotlib.pyplot as plt
# SVM=[0.917, 0.925, 0.940, 0.944, 0.933, 0.943, 0.952, 0.940, 0.960, 0.937]
SVM=[0.905, 0.929, 0.933, 0.966, 0.962, 0.924, 0.962, 0.938, 0.943, 0.924]
KNN=[82.6,82.6,83.4,83.4,84.2,84.6,87.0,82.2,84.6,81.8]
for i in range(len(KNN)):
    KNN[i]=KNN[i]/100
# SGD=[0.933, 0.933, 0.929, 0.933, 0.913, 0.92, 0.940, 0.940, 0.968, 0.944
SGD=[0.924, 0.929, 0.933, 0.981, 0.957, 0.915, 0.966, 0.929, 0.948, 0.924]
# for i in range(len(SGD)):
#     SGD[i]=SGD[i]*100
SVM = np.array(SVM)
KNN = np.array(KNN)
SGD = np.array(SGD)
print(np.mean(SVM),np.mean(SGD),np.mean(KNN))
x=[1,2,3,4,5,6,7,8,9,10]
plt.plot(x, SVM, label = "SVM")
plt.plot(x, SGD, label = "Mạng Nơ-ron")
plt.plot(x, KNN, label = "KNN")
plt.xlim(1,10)
# plt.ylim(0,1)
plt.ylabel('Độ chính xác ')
# # naming the y axis
plt.xlabel('Vòng lặp')
# # giving a title to my graph
plt.title("Độ chính xác của 3 mô hình")
# plt.legend()
plt.show()
