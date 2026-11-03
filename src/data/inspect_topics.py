import xml.etree.ElementTree as ET

file_path = "data/raw/topics2021.xml"

tree = ET.parse(file_path)
root = tree.getroot()

print("Root tag:")
print(root.tag)

print("\nNumber of topics:")
print(len(root))

print("\nFirst topic:")
print(root[0].attrib)

print("\nFirst topic text:")
print(ET.tostring(root[0], encoding="unicode")[:2000])