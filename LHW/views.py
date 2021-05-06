from django.shortcuts import render
import pandas as pd

def LHW(request):
    """ view function for LHW app """
        # read data                                                                                                  
	
    df = pd.read_csv("data/lhw_test_division.csv")
    rs1 = df["Infant_Deaths"]
    rs = df["Neo_Natal_Deaths"]
    rs2 = df["Division"]
    rs3 = df["Total_Dileveries"]   

    categories = list(rs.index)
    categories1 = list(rs1.index)
    categories2 = list(rs2.index)
    categories3 = list(rs3.index)
    
    
    
    

    NND = list(rs.values)
    ID = list(rs1.values)
    DIV = list(rs2.values)
    TD = list(rs3.values)
    
    
    
    NND = [int(i) for i in NND]
    ID = [int(i) for i in ID]
    DIV = [str(i) for i in DIV] 
    TD = [int(i) for i in TD] 
    

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories,'NND': NND, 'ID': ID,'DIV': DIV,'TD':TD, 'table_data':table_content}
    return render(request, 'LHW.html', context=context)
	