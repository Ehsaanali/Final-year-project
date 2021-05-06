from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DivisionSerializer
from .models import Division
import requests
from django.shortcuts import render
import pandas as pd
# Create your views here.
class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all().order_by('div_name')
    serializer_class = DivisionSerializer

def dashboard(request):
    response = requests.get('http://127.0.0.1:8000/Division')
    df = pd.read_csv("data/tb_division_report.csv")
    
    
   
    
    


    rs1 = df["CURED"]
    rs2 = df["Division"]
    rs = df["TREATMENT_COMPLETED"]
    rs3 = df["TREATMENT_FAILED"]
    rs4 = df["DIED"]
    rs5 = df.groupby("years")["Noofdeaths"].agg("sum")

    categories = list(rs.index)
   
    categories = list(rs1.index)
    
    categories = list(rs2.index)
    categories = list(rs3.index)
    categories = list(rs4.index) 
    categories = list(rs5.index)
    

    TC = list(rs.values)
    CURED = list(rs1.values)
    Div = list(rs2.values)
    TF = list(rs3.values)
    DIED = list(rs4.values)
    yearlydeath = list(rs5.values)
    
    
    TC = [int(i) for i in TC]
    TF = [int(i) for i in TF]
    CURED = [int(i) for i in CURED]
    Div = [str(i) for i in Div]
    DIED = [int(i) for i in DIED]
    
    yearlydeath = [int(i) for i in yearlydeath]

	
    table_content = df.to_html(index=None)
    table_content = table_content.replace("","")
    table_content = table_content.replace('class="dataframe"',"class='table table-striped'")
    table_content = table_content.replace('border="1"',"")
    data = response.json()
    context = {"categories": categories,'yearlydeath':yearlydeath, 'TC': TC, 'data':data,'CURED': CURED,'Div': Div,'TF':TF,'DIED': DIED,'table_data':table_content}
 
    return render(request,'dashboard.html', context=context)
