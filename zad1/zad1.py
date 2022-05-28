from stegano import lsbset
from stegano.lsbset import generators

secret_message = "Blabla"
secret_image = lsbset.hide("./100kb.png",secret_message,generators.eratosthenes())
secret_image.save("./100kb.png")

secret_message = "Blablablabla"
secret_image = lsbset.hide("./1mb.png",secret_message,generators.eratosthenes())
secret_image.save("./1mb.png")

secret_message = "Blablablablablablablabla"
secret_image = lsbset.hide("./10mb.png",secret_message,generators.eratosthenes())
secret_image.save("./10mb.png")