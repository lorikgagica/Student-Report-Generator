# Student Report Generator

import csv

# Step 1: Read student data, calculate averages, and highlight best student
def process_student_data(input_file, output_file):
    try:
        with open(input_file, 'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []
            math_scores = []
            science_scores = []
            english_scores = []

            best_student = None
            best_avg = -1

            for row in reader:
                name = row['Name']
                math = int(row['Math'])
                science = int(row['Science'])
                english = int(row['English'])
                average = round((math + science + english) / 3, 2)
                status = "Pass" if average >= 60 else "Fail"
                student_reports.append({
                    'Name': name,
                    'Math': math,
                    'Science': science,
                    'English': english,
                    'Average': average,
                    'Status': status
                })
                math_scores.append(math)
                science_scores.append(science)
                english_scores.append(english)
                if average > best_avg:
                    best_avg = average
                    best_student = name

            # Step 2: Write processed data to a new CSV and add subject averages
            with open(output_file, 'w', newline='') as outfile:
                fieldnames = ['Name', 'Math', 'Science', 'English', 'Average', 'Status', 'BestStudent']
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                for report in student_reports:
                    bs = "<<< BEST STUDENT" if report['Name'] == best_student else ""
                    row = report.copy()
                    row['BestStudent'] = bs
                    writer.writerow(row)

                # Write subject averages row at the end
                avg_math = round(sum(math_scores) / len(math_scores), 2)
                avg_sci = round(sum(science_scores) / len(science_scores), 2)
                avg_eng = round(sum(english_scores) / len(english_scores), 2)
                avg_row = {
                    'Name': 'SUBJECT_AVERAGE',
                    'Math': avg_math,
                    'Science': avg_sci,
                    'English': avg_eng,
                    'Average': '',
                    'Status': '',
                    'BestStudent': ''
                }
                writer.writerow(avg_row)
            print(f"Student report generated in {output_file} successfully.")

            # Step 3: User search functionality
            search_name = input("Search for a student by name: ").strip()
            found = False
            for report in student_reports:
                if report['Name'].lower() == search_name.lower():
                    print(f"\nFound: {report['Name']}, Math: {report['Math']}, Science: {report['Science']}, English: {report['English']}, Average: {report['Average']}, Status: {report['Status']}")
                    found = True
                    if report['Name'] == best_student:
                        print("This student is the BEST student.")
            if not found:
                print("Student not found.")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found")
    except KeyError:
        print("Error: Invalid column names in the input file")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main Program
input_file = 'students.csv'
output_file = 'student_report.csv'

process_student_data(input_file, output_file)