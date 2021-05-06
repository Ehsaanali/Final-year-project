from django.shortcuts import render
import pandas as pd

def LHW_ReportsWise(request):
        # read data                                                                                                  
	
    df = pd.read_csv("data/LHW_Reports.csv")
    
    
    rs1 = df["Submitted_Reports"]

    rs2 = df["District"]
    rs = df["Due_Reports"]

    categories = list(rs.index)
   
    categories = list(rs1.index)
    
    categories2 = list(rs2.index)
    
    

    DR = list(rs.values)
    SR = list(rs1.values)
    Dis = list(rs2.values)
    
    
    DR = [int(i) for i in DR]
    SR = [int(i) for i in SR]
    Dis = [str(i) for i in Dis]

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories,'DR': DR, 'SR': SR,'Dis': Dis,'table_data':table_content}
    return render(request, 'LHW_ReportsWise.html', context=context)
