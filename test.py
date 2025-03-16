import time
import random
from progressbar import *

progressbar = ProgressBar()

messages = ["loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
            "loading", "uploading", "downloading", "unzipping", "zipping", "processing", "compiling",
]
length = len(messages)

progressbar.prep()
for idx, msg in enumerate(messages):
    progressbar.display(idx, length, msg)
    time.sleep(random.uniform(0.25, 1.5))
progressbar.end_display()
