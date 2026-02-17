html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>My Web Page</title>
</head>
<body>

    <h1>Welcome to My Web Page</h1>

    <p>This is a simple web page created using Python program.</p>

    <img src="https://via.placeholder.com/250" alt="Sample Image">

    <h2>Ordered List</h2>
    <ol>
        <li>Python</li>
        <li>Java</li>
        <li>C++</li>
    </ol>

    <h2>Unordered List</h2>
    <ul>
        <li>HTML</li>
        <li>CSS</li>
        <li>JavaScript</li>
    </ul>

    <br>

    <a href="https://www.python.org">Visit Python Official Website</a>

</body>
</html>
"""
with open("webpage.html", "w") as file:
    file.write(html_content)

print("Web page created successfully!")
