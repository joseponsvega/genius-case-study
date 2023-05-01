# Genius Sheets Exercise

## School Files

`project_csv_file_1.csv` - The exam scores for the Calculus AB test.
`project_csv_file_2.csv` - The exam scores for the AP Biology test.
`project_text_file_1.txt` - A welcome letter from the principal of the school to parents, detailing which teacher is teaching each class
`project_text_file_2.txt` - A directory of each teacher and their contact information.

## To Install

Set up the appropriate environment variables for the Open AI key, etc. and then:
```
$ pip install .
```

## Sample Run

```
$ python genius.py "Based on the documents provided, what is the average exam grade in the class taught by Ethan Hawkes?"

The average exam grade in the class taught by Ethan Hawkes, Calculus AB, at Edison High School is 82, based on the documents provided. This is calculated from the exam grades of Jose Pons Vega (82), Trevor Jonas (44), and Alex Barbarian (95). Source: ./project_csv_file_2.csv, ./project_text_file_1.txt, and ./project_text_file_2.txt
```

```
$ python genius.py "Based on the documents provided, which class has the lowest average exam score?"

Calculus AB, taught by Ethan Hawkes, has the lowest average exam score, with an average of 70, out of the classes represented in the provided documents (AP Biology, taught by David French, and Calculus AB, taught by Ethan Hawkes).
```

```
$ python genius.py "Based on the documents provided, can you give me the email of the Calculus AB teacher?"

Yes, the email of the Calculus AB teacher Ethan Hawkes is ethan.hawkes@edison.edu. Sources: ./project_csv_file_2.csv, ./project_text_file_1.txt, ./project_text_file_2.txt
```

```
$  python genius.py "Based on the documents provided, which class has the lowest average exam score? What is the contact information for the teacher?"

Based on the documents provided, the class with the lowest average exam score is Calculus AB, with an average score of 72. The teacher of this class is Ethan Hawkes, and his contact information is provided in the documents as ethan.hawkes@edison.edu and 714-866-3333. The documents provided include a CSV file containing the class, student name, and exam grade for AP Biology, which had an average score of 94, and a text file containing the list of teachers and classes at Edison High School, as well as the contact information for each teacher. Source: ./project_csv_file_2.csv, ./project_csv_file_1.csv, ./project_text_file_1.txt, ./project_text_file_2.txt
```