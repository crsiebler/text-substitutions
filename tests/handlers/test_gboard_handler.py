import io

from pysubstitutor.handlers.gboard_handler import GboardHandler
from pysubstitutor.models.text_substitution import TextSubstitution


def test_gboard_handler_read():
    """
    Tests the GboardHandler's read method with valid Gboard data.
    """
    gboard_data = (
        "# Gboard Dictionary version:1\n\nsmile\t😊\ten-US\nshrug\t¯\\_(ツ)_/¯\ten-US\n"
    )
    handler = GboardHandler()
    input_stream = io.StringIO(gboard_data)
    entries = handler.read(input_stream)

    assert len(entries) == 2
    assert entries[0] == TextSubstitution(shortcut="smile", phrase="😊")
    assert entries[1] == TextSubstitution(shortcut="shrug", phrase="¯\\_(ツ)_/¯")


def test_gboard_handler_read_empty():
    """
    Tests the GboardHandler's read method with empty Gboard data.
    """
    gboard_data = ""
    handler = GboardHandler()
    input_stream = io.StringIO(gboard_data)
    entries = handler.read(input_stream)

    assert len(entries) == 0


def test_gboard_handler_export():
    """
    Tests the GboardHandler's export method with valid data.
    """
    handler = GboardHandler()
    entries = [
        TextSubstitution(shortcut="smile", phrase="😊"),
        TextSubstitution(shortcut="shrug", phrase="¯\\_(ツ)_/¯"),
    ]
    output_stream = io.StringIO()
    handler.export(output_stream, entries)

    expected_output = (
        "# Gboard Dictionary version:1\n\nsmile\t😊\ten-US\nshrug\t¯\\_(ツ)_/¯\ten-US\n"
    )
    # Normalize line endings for comparison
    assert output_stream.getvalue().replace("\r\n", "\n") == expected_output
