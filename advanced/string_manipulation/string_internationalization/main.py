import os
os.environ["LANG"] = "pt-br"

import gettext

def main():
    # Set up translation
    gettext.bindtextdomain('string_manipulation', 'locales')
    gettext.textdomain('string_manipulation')
    _ = gettext.gettext

    # Get localized greeting
    greeting = _("Hello, world!")

    # Print localized greeting
    print(greeting)

if __name__ == "__main__":
    main()
