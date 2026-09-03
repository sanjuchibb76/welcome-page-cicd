from pathlib import Path

def test_welcome_page_contains_welcome():
    content = Path(__file__).parent.joinpath("index.html").read_text()
    assert "Welcome" in content

if __name__ == "__main__":
    test_welcome_page_contains_welcome()
    print("PASS: welcome page test")
