import json
import os
import matplotlib.pyplot as plt

def plot_history(history,figname):
  fig, axs = plt.subplots(2,figsize=(20,10))

  # create the accuracy subplot
  axs[0].plot(history['history']["accuracy"],label="train accuracy")
  axs[0].plot(history['history']["val_accuracy"],label="test accuracy")
  axs[0].set_ylabel("Accuracy")
  axs[0].legend(loc="best")
  axs[0].set_title("accuracy eval")
  axs[0].set_ylim(0, 1)

  # create error subplot
#   axs[1].plot(history.history["loss"],label="train error")
#   axs[1].plot(history.history["val_loss"],label="test error")
#   axs[1].set_ylabel("Error")
#   axs[1].set_xlabel("Epoch")
#   axs[1].legend(loc="best")
#   axs[1].set_title("Error eval")
  # axs[1].set_ylim(0, 1)

  fig.savefig(figname)

  plt.show()
  return


filepath = 'sound-learning/new'

# select a filename
# filename = input("Enter filename:"   )

for dirpath, dirnames, filenames in os.walk(filepath):
    # print(dirpath, dirnames, filenames)
    # if dirpath is filepath:
    for file in filenames:
        filen = file.split('2',1)
        if filen[0] != 'example': continue

        f = open(dirpath + "/" + file,'r')

        data = json.loads(f.read())
        index = 0

        index2 = 0
        saved = 100
        saved2 = 100

        # print(data)
        for i, row in enumerate(data): 
            # print('parameters',row['parameters'])
            # print('Final Acc',row['finalAcc'])
            # print('Final Val',row['finalVal'])
            test = dirpath.split("test")
            
            if test[-1] == '3':
                model_history = {'history': {'accuracy' : row['finalAccData'],
                                            'val_accuracy' : row['finalValData']}}
                # print(model_history)
                filen2 = filen[1].split('.')
                imageName = 'neuron' + str(row['parameters'][0][0]) + 'drop' + str(int(row['parameters'][0][1]*10))\
                     + 'epoch' + str(row['parameters'][0][2]) + 'batch' + str(row['parameters'][0][3])
                imageName = 'sound-learning/new/foldertest3/' + filen2[0] + imageName 
                plot_history(model_history,imageName)
            # else:
            diff = abs(row['finalAcc']-row['finalVal'])
    
            if saved > diff and row['finalVal'] >=.45: 
                index = i
                saved = diff

            diff2 = abs(row['report']['accuracy']-row['finalVal'])
            if saved2 > diff2 and row['finalVal'] >=.45: 
                index2 = i
                saved2 = diff2


        print(dirpath,file)

        print('parameters',data[index]['parameters'])
        print('Train accuracy',data[index]['finalAcc'])
        print('Final Val',data[index]['finalVal'])
        print('test accuracy',data[index]['report']['accuracy'])

        print('parameters',data[index2]['parameters'])
        print('Train accuracy',data[index2]['finalAcc'])
        print('Final Val',data[index2]['finalVal'])
        print('test accuracy',data[index2]['report']['accuracy'])

        print(saved)

        f.close()


        # stop = input("hit return to continue")

        # if stop != '':
        #     break





