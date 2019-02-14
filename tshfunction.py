def main():
    """Main Function

    The main function parses through the contents of the loaded file
    to create patient speciffic dictionaries.
    It also calls different modular functions from the script to
    create additional outputs for the dictionaries. Finally,
    the main function creates .json files to host each patients
    respective ditctionaries.

    :param data: test_data.txt

    :returns: .json files containing patient speciffic library"""

    import json

    data = open("test_data.txt", "r")
    contents = data.readlines()
    data.close()

    x = len(contents)

    count = 0
    while count <= (x-4):
        if count % 4 == 0:

            name = contents.pop(0)
            n = name.split(" ")
            firstname = n.pop(0)
            last = n.pop(0)
            lastname = last.rstrip()
            age = contents.pop(0)
            gender = contents.pop(0)
            tshlist = contents.pop(0)
            tsh = tshlist.split(",")
            tsh.remove('TSH')
            tshdata = [float(i) for i in tsh]
            sorttsh = sorted(tshdata)

            d = diagnosis(tshlist)
            p = create_dictionary(firstname, lastname, age, gender, d, sorttsh)

            out_file = open("{}-{}.json".format(firstname, lastname), "w")
            json.dump(p, out_file)
            out_file.close()

        count += 4


def diagnosis(tshlist):
    """Diagnosis Function

    This function takes the TSH Values as an input to determine
    the diagnosis of the respective patientself.
    If any values in the list are below 1.0 the patient has
    hyperthyroidism, if any are above 4.0 the patient has
    hypothyroidism, and otherwise they are normal.

    :param tsh: list of TSH Values directly from test_data.txt file.

    :returns: diagnosis of thyroid related disease."""

    tsh = tshlist.split(",")
    tsh.remove('TSH')
    tshdata = [float(i) for i in tsh]

    if min(tshdata) < 1.0:
        diagnosis = "Hyperthyroidism"
    elif max(tshdata) > 4.0:
        diagnosis = "Hypothyroidism"
    else:
        diagnosis = "Normal Thyroid Funciton"

    return diagnosis


def create_dictionary(firstname, lastname, age, gender, diagnosis, tshlist):
    """Create_Dictionary Function

    This function creates a patient speciffic dictionary. The dictionary
    will be found in the corresponding .json file.

    :param firstname: First name directly from test_data.txt file.
    :param lastname: Last name directly from test_data.txt file.
    :param age: Age directly from test_data.txt file.
    :param gender: Gender directly from test_data.txt file.
    :param diagnosis: Diagnosis determined by diagnosis() function.
    :param tshlist: TSH Values directly from test_data.txt file.

    :returns: Patient speciffic library"""

    patient = {"First Name": firstname,
               "Last Name": lastname,
               "Age": age,
               "Gender": gender,
               "Diagnosis": diagnosis,
               "TSH Values": tshlist,
               }

    return patient


if __name__ == "__main__":
    main()
