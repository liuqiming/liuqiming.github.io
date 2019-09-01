import os
import json
import codecs

template = """
<div class="card item col-lg-3 col-md-4 col-sm-6 col-12">
<h5 class="item-title">{title}</h5>
<img src="img/{name}" alt="image" />
<a href="img/{name}" data-lightbox="image-{number}" data-title="{description}" class="has-border">
</a>
<div class="card-body">
<h5 class="card-title">{title}</h5>
<p class="card-text">{description}</p>
</div>
</div>
"""


with codecs.open("products.json", "r", "utf-8") as pf:
    products = json.load(pf)
n = 1
with codecs.open("images.html", "w", "utf-8") as wf:
    for name in os.listdir("."):
        if name.endswith(".jpg"):
            print("write {}".format(name))
            title = name.rstrip(".jpg")
            description = ""
            if title in products:
                description = products[title]
            p = {
                "name": name,
                "title": title,
                "description": description,
                "number": n
            }
            parts = template.format(**p)
            wf.write(parts)
            n += 1


    