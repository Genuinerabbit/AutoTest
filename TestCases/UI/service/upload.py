import re

def uploadpagetest(page):
    page.goto("http://127.0.0.1/dvwa/index.php")
    page.get_by_role("link", name="File Upload").click()

    with page.expect_file_chooser() as fc_info:
        page.get_by_role("textbox").click()
    file_chooser = fc_info.value
    file_chooser.set_files(r"screenshot\login1.png")

    # page.get_by_role("textbox").set_input_files(r"screenshot\login1.png")
    page.get_by_role("button", name="Upload").click()
    assert page.get_by_text(re.compile("succesfully upload", re.IGNORECASE)).count() == 1
    assert "succesfully uploaded" in page.content()