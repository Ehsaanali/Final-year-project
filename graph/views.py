from django.shortcuts import render
import pandas as pd

def dashboard(request):
    
        # read data                                                                                                  
	
    df = pd.read_csv("data/tb.csv")
    rs = df.groupby("years")["Noofdeaths"].agg("sum")
    categories = list(rs.index)
    values = list(rs.values)
    values = [int(i) for i in values]
	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
	
    context = {"categories": categories, 'values': values, 'table_data':table_content}
    return render(request, 'dashboard.html', context=context)