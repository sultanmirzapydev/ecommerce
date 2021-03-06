
from django.views.generic  import ListView, DetailView 
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product


class ProductListView(ListView):
	queryset = Product.objects.all()
	template_name = 'products/list.html'

	#def get_context_data(self, *args, **kwargs):
	#	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	#	print(context)
	#	return context






def Product_list_view(request):
	queryset = Product.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
	queryset = Product.objects.all()
	template_name = 'products/detail.html'

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		#context['abc'] = 123
		return context

		def get_object(self, *args, **kwargs):
			request = self.request
			pk = self.kwargs.get('pk')
			instance = Product.objects.get_by_id(pk)
			if instance is None:
				raise Http404('product does not exist')

			return instance


def Product_detail_view(request, pk):
	#instance = Product.objects.get(pk=pk)
	#instance = get_object_or_404(Product, pk=pk)

	instance = Product.objects.get_by_id(pk)

	if instance is None:
		raise Http404('product does not exist')

	#qs = Product.objects.filter(id=pk)

	#print(qs)
	#if qs.exists() and qs.count() == 1:
	#	instance = qs.first()
	#else:
	#	raise Http404('Product does not exist')

	
	context = {
		'object': instance
	}

	return render(request, 'products/detail.html', context)