import xml.etree.ElementTree as ET

tree = ET.parse("./data/xml_input.xml")  # -> ElementTree
root = tree.getroot()  # -> Element

# retrieve Elements by calling 'findall(elementname: str)'
for id_, investor in enumerate(root.findall('investor')):
  # get text value
  name = investor.text
  investor.text = name.upper()

  # set attribute value
  investor.set("id", str(id_))

# there are two way to create new elements
new_element = ET.fromstring("<investor>Allen Duff</investor>")
root.append(new_element)

another_element = ET.Element("investor")
another_element.text = "Peter Parker"
root.append(another_element)

# find a specific element
specific_element = root.find(".//investor[@id='4']")
print(specific_element.text, specific_element.get("id"))

tree.write("./data/xml_output.xml")