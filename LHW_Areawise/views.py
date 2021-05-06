from django.shortcuts import render
import pandas as pd

def LHWAreawise(request):
    
        # read data                                                                                                  
	
    df = pd.read_csv("data/lhw_performance.csv")
    
    rs1 = df["Covered_UC"]
    rs2 = df["month"]
    rs3 = df["exp"]
     
    categories = list(rs1.index)
    categories = list(rs2.index)
    categories = list(rs3.index)
    
    

    
    Cov = list(rs1.values)
    month = list(rs2.values)
    exp = list(rs3.values)
    
    
    
    Cov = [int(i) for i in Cov]
    
    exp = [int(i) for i in exp]
    month = [str(i) for i in month]

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'exp':exp,'Cov': Cov,'month': month,'table_data':table_content}
    return render(request, 'LHW_Areawise.html', context=context)