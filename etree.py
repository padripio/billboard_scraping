from lxml import etree

root_attributes = {
    "class": "root",
}
branch1_attributes = {
    "id": "one",
    "class": "branch"
}
branch2_attributes = {
    "class": "branch",
    "id": "two"
}

# create a tree
root = etree.Element("mzizi", attrib=root_attributes)
# add 3 branches to the tree
branch1 = etree.SubElement(root, "stem", attrib=branch1_attributes)
branch1.text = "This is the first branch"
leaf1 = etree.SubElement(branch1, "leaf", )
leaf1.text = "this is a leaf"

branch2 = etree.SubElement(root, "stem", id="two")
branch2.text = "This is the second branch"
leaf2 = etree.SubElement(branch2, "leaf")
leaf2.text = "this is the second leaf"

branch3 = etree.SubElement(root, "stem", id="three")
branch3.text = "This is the third branch"
leaf3 = etree.SubElement(branch3, "leaf")
leaf3.text = "this is the third leaf"

# add 2 branches to each branch


# accessing the tree
tree_string = etree.tostring(root, pretty_print=True, method="HTML").decode()
# print(tree_string)
# access the branches
branch_1_path = root.xpath("//stem[contains(@id,'one')]")
branch2_path = root.xpath("//stem[contains(@class,'branch')]")
branches = root.xpath("//stem")
for branch in branches:
    branch_string = etree.tostring(branch, pretty_print=True, method="HTML").decode()
    # print(f"{branch_string}\n\n")
#b2 = etree.tostring(branch2_path, pretty_print=True, method='HTML').decode()
#print(b2)
for x in branch2_path:
    print(x.text)
branch2_string=etree.tostring(branch2,method="HTML",pretty_print=True).decode()
b2str=root.xpath("string()")
print(f"b2 {b2str}")
print(branch2_string)