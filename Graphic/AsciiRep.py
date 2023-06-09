from colorama import Fore, Back, Style


class AsciiRep:
    """
    This simple class stores the ANSI color, ANSI background color, and text.
    Helpful for expanding on terrain generation.
    """

    valid_text_colors = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']
    valid_bg_colors = ['BLACK', 'RED', 'GREEN', 'YELLOW', 'BLUE', 'MAGENTA', 'CYAN', 'WHITE']

    def __init__(self, text, text_color=None, bg_color=None):
        """
        Initialize an AsciiRep object with the given text, text_color, and bg_color.

        Args:
            text (str): The text to be displayed.
            text_color (str, optional): The ANSI color of the text. Defaults to None.
            bg_color (str, optional): The ANSI background color of the text. Defaults to None.
        """
        text_color = text_color.upper()
        bg_color = bg_color.upper()

        if text_color not in self.valid_text_colors:
            raise ValueError(f"Invalid text color: {text_color}")

        if bg_color not in self.valid_bg_colors:
            raise ValueError(f"Invalid background color: {bg_color}")

        self.text = text
        self.text_color = text_color
        self.bg_color = bg_color

    def with_text_color(self, text_color):
        self.text_color = text_color
        return self

    def with_bg_color(self, bg_color):
        self.bg_color = bg_color
        return self

    def __str__(self):
        """
        Return the text representation of the AsciiRep object, with ANSI color and background applied.

        Returns:
            str: The text representation with ANSI color and background.
        """
        text_color_code = getattr(Fore, self.text_color.upper(), '') if self.text_color else ''
        bg_color_code = getattr(Back, self.bg_color.upper(), '') if self.bg_color else ''

        styled_text = f"{text_color_code}{bg_color_code}{self.text}{Style.RESET_ALL}"
        return styled_text


# Example usage
if __name__ == '__main__':
    red_text = AsciiRep("Hello World!", text_color="red", bg_color="blue")
    my_text = AsciiRep("Hello World! v1.1").with_text_color("white").with_bg_color("black")

    # Print the text representations
    print(red_text)  # Prints: Hello, World! in red color
    print(my_text)
