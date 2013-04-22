from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw
from google.appengine.api.urlfetch import fetch, GET
from bs4 import BeautifulSoup


def get_pypi_package_version(package):
    url = "https://pypi.python.org/pypi?:action=doap&name=%s" % package
    response = fetch(url, method=GET)
    if response.status_code != 200:
        return None
    soap = BeautifulSoup(response.content)
    return soap.release.version.revision.text


def version_image(name, version):
    if not version:
        version = "?.?.?"
    if not name:
        name = "????"
    image = Image.open("assets/version.png")
    font_bold = ImageFont.truetype("assets/DejaVuSans-Bold.ttf", 10)
    font = ImageFont.truetype("assets/DejaVuSans.ttf", 10)
    draw = ImageDraw.Draw(image)
    draw.text((5, 4), name, (255, 255, 255), font=font)
    draw.text((38, 4), version, (255, 255, 255), font=font_bold)
    return image
