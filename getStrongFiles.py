import csv
import sys

if __name__ == '__main__':
  allFilesName = sys.argv[1]
  strongFilesName = sys.argv[2]

  allFiles = open(allFilesName, 'rb')
  strengthFile = csv.reader(open('judgeGEMA.db', 'rb'), delimiter = '\t')
  strongFiles = open(strongFilesName, 'wb')
  
  strengthDict = {}

  for line in strengthFile:
    strengthSum = 0
    num = 0
    for score in line[1:]:
      if score != '-':
        strengthSum += int(score)
        num += 1
    if num > 0:
      strengthDict[line[0]] = float(strengthSum)/num
    else:
      strengthDict[line[0]] = 0


  for fileName in allFiles:
    id = fileName[4:6] + '-' + fileName[6:-6]
    print id
    if strengthDict[id] > 2.7: # value from 1 (weak) to 4 (strong)
      strongFiles.write('features_fbank/'+fileName[:-5]+'fbank\n')