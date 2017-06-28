#!/usr/bin/env python
from jinja2 import Environment, FileSystemLoader, select_autoescape
import os

env = Environment(
    loader=FileSystemLoader(["templates", "content"]),
    autoescape=select_autoescape(['html', 'xml'])
)

FileSystemLoader("..")
for filename in os.listdir("content"):
    if not filename.endswith(".swp"):
        with open(os.path.join("www", filename), "w") as f:
            f.write(env.get_template(filename).render())