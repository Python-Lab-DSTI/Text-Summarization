# Text-Summarization

Text Summarization: Students’ Feedback 
 

 ## Context
 
 Student feedback is used widely in present in order to enhance the quality of teaching and learning process by improving the teacher-student relationship. Text summarization reduces reading time, helps to identify basic content quickly and accurately. There are three basis to segment text summarization:  

- Based on Input Type: Can be from single or multiple documents  

- Based on Purpose: Domain specific or generic summarization 

- Based on Output Type: Extractive or Abstractive Summarization 
 

## Objective

The best way is to read all the feedback and create a summary for the lecturers, students and the management to understand. Hence, we tried to create a system to summarizing all student feedback and giving an overall summary for teachers, lecturers, schools, universities, and all education systems. 
 
### Data Source
Feedback is collected from students as online forms as well as handwritten documents. In this project, we collated the data from online forms into CSVs and used it as a primary input source.  
 

 ### Our Methodology
 
 We focused on the extractive summarization as we are working in the context of feedback summarization. 
 We followed a 5-steps process for implementation: 
 
- Data exploratory 

- Importing & Cleaning Raw Data: Removing stop words, punctuations, contractions and make it lower case for consistency. 

- Preparation for text processing: Word and sentence tokenization to build a frequency table. 

- Summarization Algorithm: Using SPACY library for parsing and creating summary. 

- Performance evaluation: Calculating ROUGE score with our output and reference summary created by a human 
 

### Conclusions & Next Step

The rouge score suggests that the model could be further improved by using deep learning and transformer based models. Also, other evaluation metrics could be used like Bert to compare summaries. 
The scope could also be further broadened by scraping data from web like coursera reviews etc.  

 
