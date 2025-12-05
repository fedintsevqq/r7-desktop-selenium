from sys import platform


if platform == "linux" or platform == "linux2":
    from resources.spreadsheet.ExpectedImagesLinux import ExpectedImagesLinux as ExpectedImages
elif platform == "darwin":
    from resources.spreadsheet.ExpectedImagesMac import ExpectedImagesMac as ExpectedImages
elif platform == "win32":
    from resources.spreadsheet.ExpectedImagesWindows import ExpectedImagesWindows as ExpectedImages
