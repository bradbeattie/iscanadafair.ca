#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import shutil

env = Environment(
    loader=FileSystemLoader(["templates", "."]),
    autoescape=select_autoescape(['html', 'xml']),
    extensions=["jinja2_markdown.MarkdownExtension"],
)

FileSystemLoader("..")
for root, dirs, filenames in os.walk("content"):
    for filename in filenames:
        if not filename.endswith(".swp"):
            sourcepath = os.path.join(root, filename)
            targetpath = os.path.join("www", os.path.join(os.path.relpath(root, "content"), filename))
            os.makedirs(os.path.dirname(targetpath), exist_ok=True)
            with open(sourcepath) as f:
                if f.readline().startswith("{% extends"):
                    with open(targetpath, "w") as f:
                        f.write(env.get_template(sourcepath).render())
                else:
                    shutil.copyfile(sourcepath, targetpath)
