from google_images_download import google_images_download   

response = google_images_download.googleimagesdownload()   

arguments = {"keywords":"레드벨벳 슬기,레드벨벳 예리, 레드벨벳 조이, 레드벨벳 웬디","limit":20,"print_urls":True} 
paths = response.download(arguments)   
print(paths)  