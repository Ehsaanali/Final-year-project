from django.shortcuts import render
import pandas as pd

def epi(request):
                                                                                                      
	
    df = pd.read_csv("data/epi_test.csv")
    rs = df["Infant_Immunization_started"]
    rs1 = df["Live_Births"]
    rs2 = df["District"]
    rs3 = df["No_of_Children_(12-23_months_of_age)_whose_immunization_was_completed"]
    rs4 = df["No_of_children_of_12-23_months_of_age"]

    categories = list(rs.index)
   
    categories = list(rs1.index)
    
    categories = list(rs2.index)
    
    categories = list(rs3.index)
    
    categories = list(rs4.index)
    
    

    Im = list(rs.values)
    Im1 = list(rs1.values)
    Im2 = list(rs2.values)
    immunization = list(rs3.values)
    Total = list(rs4.values)
    
    
    Im = [int(i) for i in Im]
    Im1 = [int(i) for i in Im1]
    Im2 = [str(i) for i in Im2]
    immunization = [int(i) for i in immunization]
    Total = [int(i) for i in Total]

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories,'Im': Im, 'Im1': Im1,'Im2': Im2,'immunization':immunization,'Total':Total, 'table_data':table_content}
    return render(request, 'epi.html', context=context)
	
