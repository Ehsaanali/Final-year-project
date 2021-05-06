from django.shortcuts import render
import pandas as pd

def Trends(request):
    
        # read data                                                                                                  
	
    df = pd.read_csv("data/trends_tb.csv")
    rs = df["Years"]
    rs1 = df["Banbhore"]
    rs2 = df["Karachi"]
    rs3 = df["Hyderabad"]
    rs4 = df["Larkana"]

   

    categories = list(rs.index)
   
    categories = list(rs1.index)
    
    categories = list(rs2.index)

    
    categories = list(rs3.index)
   
    categories = list(rs4.index)
    
    

    years = list(rs.values)
    banbhore = list(rs1.values)
    karachi = list(rs2.values)
    hyderabad = list(rs3.values)
    larkana = list(rs4.values)
    
    
    years = [int(i) for i in years]
    banbhore = [int(i) for i in banbhore]
    karachi = [int(i) for i in karachi]
    hyderabad = [int(i) for i in hyderabad]
    larkana = [int(i) for i in larkana]


	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories,'years': years, 'banbhore': banbhore,'karachi': karachi,'hyderabad': hyderabad,'larkana': larkana,'table_data':table_content}
    return render(request, 'Trends.html', context=context)
	
	
