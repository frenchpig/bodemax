from django.shortcuts import render

# Create your views here.

#definir pagina principal
def loadIndex(request):
  return render(request, 'index.html')

def loadAddProduct(request):
  return render(request, 'agregar-producto.html')