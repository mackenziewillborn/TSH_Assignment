# TSH_Assignment
# BME547 Assignment 


## Program Specifications
* Read in the data from test_data text file.
* From the TSH results from each patient, diagnose whether the patient has:
  + "hyperthyroidism" as defined by any of their tests results being less than 1.0,
  + "hypothyroidism" as defined by any of their test results being greater than 4.0, or
  + "normal thyroid function" as defined by all of their test results being
  between 1.0 and 4.0, inclusive.
  + No single patient will have test results both above 4.0 and below 1.0,
  hence will only meet one of the diagnoses above.
* For each patient, create an output file named "FirstName-LastName.json".
The file should contain the following information in JSON format: 
  + First Name
  + Last Name
  + Age
  + Gender
  + Diagnosis
  + TSH (containing a list of all of the test results in low to high order)
* To create the above JSON output file, first create a dictionary with the keys
listed above and their corresponding values.  Then, using the `open` and `json`
commands, create and output the information.
* .html file found in docs/build/.html file corresponding to the index of the sphinx 
documentation website for this program 


## Grading Expectations
* Good git usage and workflow
* Meeting the above functional specifications
* Appropriate functional modularity
* Unit testing exists for your function(s) that determine the diagnosis, 
following appropriate nomenclature and comprehensiveness.
(For this assignment, unit tests are not required for input/output routines, or
string handling, unless you find them useful)
* Travis CI integration
* Conforms to PEP-8 Style Guide 
* Docstrings exist for all functions
* Appropriate use of virtual environments, including a `requirements.txt` or 
`environment.yml` file being present in your GitHub repository.
* Presence and content of README.md
* Final submission is pushed to GitHub by deadline and is tagged appropriately.
