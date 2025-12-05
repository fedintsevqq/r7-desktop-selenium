from sys import platform


if platform == "linux" or platform == "linux2":
    from resources.document.ExpectedImagesLinux import ExpectedImagesLinux as ExpectedImages
elif platform == "darwin":
    from resources.document.ExpectedImagesMac import ExpectedImagesMac as ExpectedImages
elif platform == "win32":
    from resources.document.ExpectedImagesWindows import ExpectedImagesWindows as ExpectedImages
