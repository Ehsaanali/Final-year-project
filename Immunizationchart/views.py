from django.shortcuts import render
import pandas as pd

def Immunizationchart(request):
    """ view function for sales app """
        # read data                                                                                                  
	
    df = pd.read_csv("data/epi_test.csv")
    rs = df["Infant_Immunization_started"]
    
    rs1 = df["Live_Births"]

    rs2 = df["District"]

    categories = list(rs.index)
   
    categories = list(rs1.index)
    
    categories2 = list(rs2.index)
    
    

    Im = list(rs.values)
    Im1 = list(rs1.values)
    Im2 = list(rs2.values)
    
    
    Im = [int(i) for i in Im]
    Im1 = [int(i) for i in Im1]
    Im2 = [str(i) for i in Im2]

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories,'Im': Im, 'Im1': Im1,'Im2': Im2,'table_data':table_content}
    return render(request, 'Immunizationchart.html', context=context)
	
