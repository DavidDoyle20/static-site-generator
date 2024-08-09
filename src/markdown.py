import re

#returns a tuple containing the alternate text and the link
def extract_markdown_images(text):
    return(re.findall(r"!\[(.*?)\]\((.*?)\)",text))
def extract_markdown_links(text):
    return(re.findall(r"\[(.*?)\]\((.*?)\)", text))