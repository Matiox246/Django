class FormValidMixins():
    def form_valid(self, form):    
        form.instance.user = self.request.user # Set the user to the logged-in user
        return super().form_valid(form)
