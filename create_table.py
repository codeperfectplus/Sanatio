""" Automatic function create table for supported_country """
from sanatio.utils.utils import all_country
import os

output_dir = "docs/supported_country"
os.makedirs(output_dir, exist_ok=True)

def create_html_table(document_type):
    """" Create html table """
    table_body = ""
    for key, value in all_country.items():
        td_element = ""
        element1 = "<td>{}</td>".format(value["Name"])
        element2 = "<td>{}</td>".format(document_type)
        td_element += element1 + element2
        if all_country[key][document_type]["Regex"] == "":
            element3 = "<td>{}</td>".format("❌")
            td_element += element3
        else:
            element3 = "<td>{}</td>".format("✅")
            td_element += element3
        tr_element = "<tr>{}</tr>".format(td_element)
        table_body += tr_element

    final_table = f"""<table>
    <tr>
        <th>Country</th>
        <th>Document Type</th>
        <th>Supported</th>
    </tr>
    {table_body}
    </table>"""

    return final_table
    
def create_md_table(document_type):
    """ Create markdown table """
    table_body = ""
    for key, value in all_country.items():
        if all_country[key][document_type]["Regex"] == "":
            line = "| {} | {} |\n".format(value["Name"], "❌")
        else:
            line = "| {} | {} |\n".format(value["Name"], "✅")
        table_body += line


    final_table = f"""| Country | Document Type | Supported |\n| :---: | :---: | :---: |\n{table_body}"""
    with open('{}/{}.md'.format(output_dir, doc), 'w', encoding="utf-8") as f:
        f.write(final_table)
    return final_table

def create_rst_table(document_type):
    table_body = ""
    for key, value in all_country.items():
        if all_country[key][document_type]["Regex"] == "":
            line = "{} \t {}\n".format(value["Name"], "❌")
        else:
            line = "{} \t {}\n".format(value["Name"], "✅")
        table_body += line
        
    final_table = f"""====================  =========== \n Country               Document Type \n====================  =========== \n{table_body}====================  ==========="""
    pre_text  = f"""Supported Country for {document_type}\n================================\n"""
    final_text = pre_text + "\n" + final_table
    with open('{}/{}.rst'.format(output_dir, doc), 'w', encoding="utf-8") as f:
        f.write(final_text)    

    


docs = ["PostalCode", "MobileNumber", "PassportNumber" , "DrivingLicense"]

for doc in docs:
    final_table = create_rst_table(doc)
        
        
    
            


    
