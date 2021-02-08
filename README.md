# Urban Sound Classification using Machine Learning

The Urban Sound Classification project looks at a dataset composed by J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research" generated in 2014.  We took the dataset and ran it through librosa libraries to convert the wav files into MFCC files.  The Mel-Frequency Cepstral Coefficients (MFCC) is a way of capturing the spectrun of the voice (phoneme) so that it can be used in voice recognition and machine learning.  From the MFCCs we built models through 2 different Machine Learning techniques (Sequential deep learning and Support Vector Machine).  The initial thought was that the Sequential deep learning model would provide the best model.  The following information provides a view of our process and what results we came up with. The detailed process and results are explained at the page [https://ejlee127.github.io/UrbanSoundML/](https://ejlee127.github.io/UrbanSoundML/)

## Team members:

* Niral Patel
* Eunjeong Lee
* Bill Pezzullo
* Abby Pearson
* Teshanee Williams

## Process:

We attacked the project by understanding sound and analyzing what happens in ML when looking at the pure data.  What we found is that the data was too complex to work effectively in the models and the condition of overfitting was ocurring.  
To resolve the problems, we carried out four experiments by constructing three types of sample data from the sound files.
The works are organized as following:

* Colab Notebooks/ : python codes for data processing and training experiment
	
* Data/ : csv, json files of three types of MFCC data
	
* Jupyter Notebooks/ : python codes for extracting sound features
	
* Results/ : the training accuracy results for each experiment

The overall diagram for the coding is as following:
![Diagram](Images/Sound-Data-Overall-Processing.jpeg)


### Data sources:

[J. Salamon, C. Jacoby and J. P. Bello, "A Dataset and Taxonomy for Urban Sound Research", 22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014](https://urbansounddataset.weebly.com/urbansound8k.html)

[J. Salamon, C. Jacoby and J. P. Bello, "Paper", 22nd ACM International Conference on Multimedia, Orlando USA, Nov. 2014](http://www.justinsalamon.com/uploads/4/3/9/4/4394963/salamon_urbansound_acmmm14.pdf)


[Urban Sound Classification by Ricky Kim](https://towardsdatascience.com/urban-sound-classification-part-1-99137c6335f9)

[YouTube video on Sampling](https://www.youtube.com/watch?v=yWqrx08UeUs&feature=youtu.be)

[YouTube Python series on Deep Learning with sound](https://www.youtube.com/watch?v=Oa_d-zaUti8)

