import json
import shutil

cntB=0
cntM=0

for i in range(0, 36066):
    print(str(i*100/36066)+"        %")
    try:
        jsonFileName="ISIC-images\\UDA-1(1)\\ISIC_00"+str(i).zfill(5)+".json"
        with open(jsonFileName) as json_file:
            data = json.load(json_file)
            #print(data)
            benign_malignant=data["meta"]["clinical"]["benign_malignant"]
            if benign_malignant=="benign":
                try:
                    tiffFileName = "ISIC-images\\UDA-1(1)\\ISIC_00" + str(i).zfill(5) + ".jpg"
                    shutil.copy(tiffFileName, "ISIC-images\\benign")
                    cntB+=1
                except Exception as e:
                    pass
            if benign_malignant == "malignant":
                try:
                    tiffFileName = "ISIC-images\\UDA-1(1)\\ISIC_00" + str(i).zfill(5) + ".jpg"
                    shutil.copy(tiffFileName, "ISIC-images\\malignant")
                    cntM+=1
                except Exception as e:
                    pass
    except Exception as e:
        pass


print(cntB)
print(cntM)