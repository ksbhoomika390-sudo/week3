html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Student Details</title>
</head>
<body>

    <h1>Student Details</h1>

    <table border="1">
        <tr>
            <th>USN</th>
            <th>Name</th>
            <th>Course</th>
            <th>Marks</th>
        </tr>

        <tr>
            <td>101</td>
            <td>Anu</td>
            <td>MCA</td>
            <td>85</td>
        </tr>

        <tr>
            <td>102</td>
            <td>Bhoomika</td>
            <td>MCA</td>
            <td>90</td>
        </tr>

        <tr>
            <td>103</td>
            <td>Charan</td>
            <td>MCA</td>
            <td>88</td>
        </tr>

    </table>

</body>
</html>
"""
with open("student_table.html", "w") as file:
    file.write(html_content)

print("Student table webpage created successfully!")
