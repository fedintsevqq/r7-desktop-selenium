from sys import platform


if platform == "linux" or platform == "linux2":
    from resources.presentation.ExpectedImagesLinux import ExpectedImagesLinux as ExpectedImages
elif platform == "darwin":
    from resources.presentation.ExpectedImagesMac import ExpectedImagesMac as ExpectedImages
elif platform == "win32":
    from resources.presentation.ExpectedImagesWindows import ExpectedImagesWindows as ExpectedImages
