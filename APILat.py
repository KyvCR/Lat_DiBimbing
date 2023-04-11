import requests
import json
import os

class Wilayahcuaca:
    def __init__(self, local):
        self.local = local
        self.url = "https://ibnux.github.io/BMKG-importer/cuaca/wilayah.json"
        self.provinsi = ['DKIJakarta', 'DIYogyakarta', 'JawaBarat', 'Bali', 'KalimantanSelatan']
        self.wilayahcauca = "https://ibnux.github.io/BMKG-importer/cuaca/"
        
        
        

    def wilayah(self):
        file_path = r"C:\Users\62812\Documents\Lat_py\BootcampDE"    
        #dir_name_propinsi = f"{lokasi['propinsi'].replace(' ', '_')}"
        
        response = requests.get(self.url)
        data = response.json()
        if data:
            dataWilayahTertentu = [cuacaList for cuacaList in data if cuacaList['propinsi'] in self.provinsi]
            hasilDataWilayah = json.dumps(dataWilayahTertentu, indent=4)
            #print(hasilDataWilayah)
            
            for lokasi in dataWilayahTertentu:
                response = requests.get(f"{self.wilayahcauca}{lokasi['id']}.json")
                dataLokasi = response.json()
                hasilData = json.dumps(dataLokasi, indent=4)

                for jamCuaca in dataLokasi:
                    isi_file = (f"jamCuaca \t : {jamCuaca['jamCuaca']}\nkodeCuaca \t : {jamCuaca['kodeCuaca']}\ncuaca \t\t : {jamCuaca['cuaca']}")
                    #print (isi_file)
            
                   

                    file_name = f"{lokasi['propinsi']}_{lokasi['kota']}_{jamCuaca['jamCuaca'].replace(':','').replace(' ','')}.json"
                    count = 1
                    while os.path.exists(file_name):
                        file_name = f"{lokasi['propinsi']}_{lokasi['kota']}_{jamCuaca['jamCuaca'].replace(':','').replace(' ','')}" + str(count)  +".json"
                        count += 1
                    file_path1 = os.path.join(file_path, file_name)
                   
                #

                    with open(file_name, 'x') as f:
                         f.write(isi_file) 

               
               
                                
                # for pathPropinsi in  dataWilayahTertentu:
                #    # print(lokasi['propinsi'], index)
                #     #for dir_ in range(len(jamCuaca)):
                #     #   print (f"propinsi \t : {lokasi['propinsi']} \nkota \t: {lokasi['kota']}\njamCuaca \t : {jamCuaca['jamCuaca']}\nkodeCuaca \t : {jamCuaca['kodeCuaca']}\ncuaca \t\t: {jamCuaca['cuaca']}")
                #    # print(pathPropinsi)
                #     if pathPropinsi['propinsi'] == self.provinsi[1]:
                #         # dir_name_propinsi = f"{pathPropinsi['propinsi'].replace(' ', '_')}{index}"
                #         # file_path = r"C:\Users\62812\Documents\Lay_py\BootcampDE"
                #         # propinsi_path = os.path.join(file_path, dir_name_propinsi)
                #         # os.mkdir(propinsi_path)
                        
                #         for pathKota in dataWilayahTertentu:
                #             # dir_name_kota = f"{pathKota['kota'].replace(' ', '_')}"
                #             # kota_path = os.path.join(propinsi_path, dir_name_kota)
                #             # os.mkdir(kota_path)
                        
                #             for jamCuaca in dataLokasi:
                #             #print("===============")                                                                                                               
                #             #print("++++++++++++++++++++")
                #             # dir_name_propinsi = f"{pathSimpan['propinsi'].replace(' ', '_')}{index}"
                #             # dir_name_kota = f"{pathSimpan['kota'].replace(' ', '_')}"
                #                 dir_jamCuaca = f"{jamCuaca['jamCuaca'].split(' ')[0].replace('-','')}"
                                
                                # isi_file = (f"propinsi \t : {pathPropinsi['propinsi']} \nkota \t: {pathKota['kota']}\njamCuaca \t : {jamCuaca['jamCuaca']}\nkodeCuaca \t : {jamCuaca['kodeCuaca']}\ncuaca \t\t: {jamCuaca['cuaca']}")
                                # print (isi_file)
                                
                                # file_path = r"C:\Users\62812\Documents\Lay_py\BootcampDE"
                                # propinsi_path = os.path.join(file_path, dir_name_propinsi)
                                # os.mkdir(propinsi_path)
                                # index += 1

                                # kota_path = os.path.join(propinsi_path, dir_name_kota)
                                # os.mkdir(kota_path)

                                # file_name = f"{jamCuaca['jamCuaca'].replace(':','').replace(' ','')}.json"
                                # # file_name = f"{jamCuaca['jamCuaca'].split(' ')[0].replace('-','')}.json"
                                # file_path1 = os.path.join(kota_path, file_name)
                    
                                # with open(file_path1, 'x') as f:
                                #     f.write(isi_file) 
                #print (pathPropinsi['propinsi'])

                    # else:
                    #     print("tidak masuk")
                    #     break

      
                    


test = Wilayahcuaca("document")
test.wilayah()