import os

folderPath = r'D:\Development\nft-website-project-resources\dapps-codes\generative-art-nft-master\output\edition-D3\images'

fileSequence = 0

for filename in os.listdir(folderPath):
	os.rename(folderPath + '\\' + filename, folderPath + '\\'  + '000' + str(fileSequence) + '.png')
	fileSequence +=1

#for i in range(101):
#	print('{0:04d}'.format(i))
