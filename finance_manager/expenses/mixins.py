from django.http import Http404

class FieldMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            self.fields = [
                'amount', 'date', 'description', 'category'
            ]
        elif request.user.is_author:
            self.fields = [
                'amount','description', 'category'
            ]
        else:
            raise Http404("You not allowed to see this page")
        return super().dispatch(request, *args, **kwargs)