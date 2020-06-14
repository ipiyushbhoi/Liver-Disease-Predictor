import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Age':26, 
							'Gender':1, 
							'Total_Bilirubin':0.9, 
							'Direct_Bilirubin':0.3,
							'Alkaline_Phosphotase':202,
							'Alamine_Aminotransferase':14,
							'Aspartate_Aminotransferase':11,
							'Total_Protiens':6.7,
							'Albumin':3.6,
							'Albumin_and_Globulin_Ratio':1.1
							})


print(r.json())