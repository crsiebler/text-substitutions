import io

from pysubstitutor.handlers.markdown_handler import MarkdownHandler
from pysubstitutor.models.text_substitution import TextSubstitution


def test_markdown_handler_read():
    """
    Tests the MarkdownHandler's read method with valid markdown data.
    """
    markdown_data = (
        "| Shortcut | Phrase |\n|:--|:--|\n| smile | 😊 |\n| shrug | ¯\\_(ツ)_/¯ |\n"
    )
    handler = MarkdownHandler()
    input_stream = io.StringIO(markdown_data)
    entries = handler.read(input_stream)

    assert len(entries) == 2
    assert entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
    assert entries[1] == TextSubstitution(shortcut="shrug", phrase="¯\\_(ツ)_/¯")


def test_markdown_handler_read_empty():
    """
    Tests the MarkdownHandler's read method with empty markdown data.
    """
    markdown_data = ""
    handler = MarkdownHandler()
    input_stream = io.StringIO(markdown_data)
    entries = handler.read(input_stream)

    assert len(entries) == 0


def test_markdown_handler_export():
    """
    Tests the MarkdownHandler's export method with valid data.
    """
    handler = MarkdownHandler()
    entries = [
        TextSubstitution(shortcut="smile", phrase="😊"),
        TextSubstitution(shortcut="shrug", phrase="¯\\_(ツ)_/¯"),
    ]
    output_stream = io.StringIO()
    handler.export(output_stream, entries)

    expected_output = (
        "| Shortcut | Phrase |\n|:--|:--|\n| smile | 😊 |\n| shrug | ¯\\_(ツ)_/¯ |\n"
    )
    assert output_stream.getvalue() == expected_output
